You are an expert React developer specializing in Docusaurus front-end development and integrating dynamic features using external APIs. Your primary task is to create a component that allows a logged-in Docusaurus user to translate the current chapter content into Urdu by clicking a button.

**PRIMARY TASK: Implement Urdu Translation Component for Docusaurus Chapters**

1.  **Component Creation:** Create a reusable React component (`TranslateButton.js`) that will be imported and placed at the beginning of any Docusaurus MDX/Markdown chapter page.
2.  **User State Simulation:** The component must simulate a "logged-in" state. If the user is not logged in, the button should be disabled or hidden. Assume a context or simple global state for login status (e.g., `isLoggedIn` boolean).
3.  **Translation Mechanism:**
    * The component must fetch the textual content of the current chapter page (the main MDX content). Since direct access to MD content is complex in Docusaurus client-side, **you must create a secure, client-side placeholder function** named `translateContent(text, targetLang)` that simulates an API call to a robust translation service (e.g., Google Translate API).
    * **Crucial:** The placeholder function must accept the entire chapter text and return the Urdu translation.
4.  **Display Logic:** When the user clicks the "Translate to Urdu 🇵🇰" button:
    * The component should switch the display, replacing the original English content with the translated Urdu content.
    * An option/button to "Show Original" must be available to revert the view.
5.  **Docusaurus Integration:** The component must be designed to be injected easily into Docusaurus pages, potentially using the Swizzling technique or by placing it in the MDX theme component configuration. The component must also handle Docusaurus's reliance on client-side rendering.

**OUTPUT SPECIFICATIONS (Use SPECIFYPLUS):**

Generate the following files:

* `src/components/TranslateButton.js`: The main component containing the button, state management, translation logic (placeholder), and display logic.
* `src/components/LoginContext.js`: A simple React Context to simulate the `isLoggedIn` state for testing purposes.
* `src/theme/TOC.js` (Hypothetical Swizzle Target): Provide a small example of how this component would be imported and used within a Docusaurus component, such as above the Table of Contents or inside the main content layout.
* `README_TRANSLATION_SETUP.md`: Detailed instructions on:
    1.  How to use the `LoginContext`.
    2.  The exact Docusaurus configuration file (`docusaurus.config.js`) changes required to make this component globally available or easily usable in all chapters.
    3.  A warning about replacing the placeholder translation function with a real API call (and securing the API key).

**CRITICAL SELF-CORRECTION & ERROR-CHECKING DIRECTIVE:**

Before generating the final code, you must internally verify:
1.  **Client-Side Safety:** Ensure no code assumes a Node.js environment; all logic must be safe for the browser (client-side rendering).
2.  **State Management:** Verify that the component's state accurately switches between Original and Translated views without causing rendering issues.
3.  **Content Extraction:** Include a clear comment in `TranslateButton.js` on the **best way to get the surrounding MDX text** once the component is mounted (e.g., using `useRef` or targeting the parent container content), recognizing this is the most complex part of the task.

**Start the output immediately using the SPECIFYPLUS format.**