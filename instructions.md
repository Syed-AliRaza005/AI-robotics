# RAG Chatbot Setup Instructions (Roman Urdu)

Yeh step-by-step hidayat aapko Gemini CLI agent ne di hain taake aap apne Docusaurus project mein RAG chatbot set up kar saken.

## 1. Zaroori Python Dependencies Install Karen

Sab se pehle, Python virtual environment banayen aur activate karen, phir zaroori libraries install karen:

```bash
# Agar aapke paas virtual environment nahi hai
python -m venv venv
# Windows par
.\venv\Scripts\activate
# macOS/Linux par
source venv/bin/activate

pip install -q -U  qdrant-client langchain-community langchain-google-genai fastapi uvicorn python-dotenv
```

## 2. GEMINI_API_KEY Environment Variable Set Karen

Apni Google Gemini API key ko `.env` file mein ya apne system environment mein set karen. `indexing_script.py` aur `main.py` is key ko `.env` file se load karenge.

`.env` file banayen (agar maujood nahi hai) aur usmein apni key likhen:

```
GEMINI_API_KEY="APKI_GEMINI_API_KEY_YANHAAAYEGI"
```

`APKI_GEMINI_API_KEY_YANHAAAYEGI` ki jagah apni asal Gemini API key dalen.

## 3. Indexing Script Chala Kar Data Load Karen

`indexing_script.py` script aapke Docusaurus documentation (Markdown files) ko padhega, unhein chote hisson (chunks) mein todega, aur phir unke embeddings generate kar ke unhein Qdrant database mein store karega.

Yeh script chalane se pehle, confirm karen ke aapka virtual environment active hai aur `GEMINI_API_KEY` set hai.

```bash
python indexing_script.py
```

Console mein aapko data loading, chunking aur Qdrant mein vectors store hone ki progress nazar aayegi. Is process ko mukammal hone dein.

## 4. FastAPI Server Start Karen

`main.py` file mein aapka RAG chatbot ka backend server maujood hai. Yeh server user queries receive karega, Qdrant se relevant information retrieve karega, aur phir Gemini model ka istemal karte hue jawab generate karega.

Server start karne ke liye:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Server `http://localhost:8000` par chalna shuru ho jayega. `--reload` flag istemal karne se code changes par server automatically restart ho jayega.

## 5. ChatWidget.js Ko Docusaurus Mein Embed Karen

`ChatWidget.js` ek React component hai jo frontend par chat UI provide karega. Isko apne Docusaurus project mein shamil karne ke liye neeche diye gaye steps follow karen:

1.  **`ChatWidget.js` aur `ChatWidget.module.css` files ko apne Docusaurus project mein copy karen.**
    Aap in files ko `AI-native-book/src/components/` (agar `components` folder nahi hai to bana len) jaisi jagah par rakh sakte hain.

    ```
    # Example:
    cp ChatWidget.js AI-native-book/src/components/
    cp ChatWidget.module.css AI-native-book/src/components/
    ```

2.  **Docusaurus Layout Mein `ChatWidget` Ko Import Aur Use Karen.**
    Apne `AI-native-book/src/theme/Layout/index.js` (ya `index.tsx` agar TypeScript use kar rahe hain) file ko edit karen. Agar yeh file maujood nahi hai, to aap `docusaurus swizzle @docusaurus/theme-classic Layout --danger` command use kar ke isko create kar sakte hain.

    `index.js` file mein (ya `index.tsx`):

    ```jsx
    import React from 'react';
    import Layout from '@theme-init/Layout';
    // ChatWidget ko import karen
    import ChatWidget from '../../components/ChatWidget'; // Path adjust karen agar zaroorat ho

    export default function LayoutWrapper(props) {
      return (
        <>
          <Layout {...props} />
          {/* ChatWidget ko yahan render karen */}
          <ChatWidget />
        </>
      );
    }
    ```

    Agar aap `Layout` ko swizzle nahi karna chahte, to aap `docusaurus.config.js` mein `custom_css` ya `custom_js` fields ka istemal kar sakte hain, lekin React component ko directly embed karne ka best tareeqa `Layout` ko swizzle karna hi hai.

3.  **Docusaurus Project Start Karen.**
    Jab saare steps mukammal ho jayen, apne Docusaurus project ko start karen:

    ```bash
    cd AI-native-book
    npm install # Agar dependencies install nahi hain
    npm start
    ```

Ab aapko apni Docusaurus website par floating chat widget nazar aayega. Aap us par click kar ke chatbot se sawal puch sakte hain. Yakeen karen ke FastAPI server (step 4) bhi chal raha ho.

---
**Note:** `aihistory.md` file aapke aur Gemini CLI agent ke darmiyan hone wali batcheet ka record rakhega, jo is chatbot ke setup se alag hai.
