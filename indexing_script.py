import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv() # Load environment variables from .env file

# Qdrant configuration
QDRANT_URL = "https://63e9de2a-8a61-4e24-a204-ec23d83e394e.us-east4-0.gcp.cloud.qdrant.io"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.g4YrQIS00Km_6PgkHuP_r4te_zqkXNWxZJBhCkymtNA"
QDRANT_COLLECTION_NAME = "docusaurus_book_rag"

# Google GenAI configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

EMBEDDING_MODEL = "text-embedding-004"

# Docusaurus documentation path
DOCS_PATH = "./AI-native-book/docs/"

def load_documents(path: str):
    """Loads markdown documents from the specified path."""
    loader = DirectoryLoader(
        path,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"autodetect_encoding": True}
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from {path}")
    return documents

def split_documents(documents):
    """Splits documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")
    return chunks

def generate_embeddings(chunks):
    """Generates embeddings for document chunks using Google GenAI."""
    print("Generating embeddings...")
    embeddings_model = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GEMINI_API_KEY
    )
    # Langchain's Qdrant integration expects embeddings directly, not chunk objects
    # We will get page_content and create embeddings
    texts = [chunk.page_content for chunk in chunks]
    embeddings = embeddings_model.embed_documents(texts)
    print("Embeddings generated.")
    return embeddings, chunks

def store_vectors_in_qdrant(embeddings, chunks):
    """Stores vectors and document metadata in Qdrant in batches."""
    print(f"Connecting to Qdrant at {QDRANT_URL}...")
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=60.0  # Set a longer timeout
    )

    # Ensure the collection exists
    try:
        client.recreate_collection(
            collection_name=QDRANT_COLLECTION_NAME,
            vectors_config=models.VectorParams(size=len(embeddings[0]), distance=models.Distance.COSINE),
        )
        print(f"Collection '{QDRANT_COLLECTION_NAME}' recreated.")
    except Exception as e:
        print(f"Could not recreate collection, it might already exist or there's another issue: {e}")
        pass

    batch_size = 100
    num_points = len(embeddings)
    
    print(f"Upserting {num_points} points to Qdrant collection '{QDRANT_COLLECTION_NAME}' in batches of {batch_size}...")

    for i in range(0, num_points, batch_size):
        batch_end = min(i + batch_size, num_points)
        batch_embeddings = embeddings[i:batch_end]
        batch_chunks = chunks[i:batch_end]

        points = []
        # Use a consistent starting ID for each batch to avoid overwriting
        # The id must be unique in the collection
        for j, (embedding, chunk) in enumerate(zip(batch_embeddings, batch_chunks)):
            points.append(
                models.PointStruct(
                    id=i + j,
                    vector=embedding,
                    payload={"text": chunk.page_content, "source": chunk.metadata.get("source")}
                )
            )
        
        client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            points=points,
            wait=True
        )
        print(f"Successfully stored batch {i//batch_size + 1}/{(num_points + batch_size - 1)//batch_size}")

    print(f"Successfully stored all {num_points} vectors in Qdrant.")

if __name__ == "__main__":
    print("Starting indexing script...")
    documents = load_documents(DOCS_PATH)
    chunks = split_documents(documents)
    embeddings, chunks_with_embeddings = generate_embeddings(chunks) # Pass chunks directly
    store_vectors_in_qdrant(embeddings, chunks_with_embeddings)
    print("Indexing script finished.")
