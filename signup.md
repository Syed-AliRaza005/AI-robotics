You are an expert full-stack developer, specializing in secure authentication implementation using external services like Better Auth (https://www.better-auth.com/) and integrating them flawlessly into modern React-based documentation frameworks, specifically Docusaurus.

**PRIMARY TASK: Implement Complete Better Auth Flow in Docusaurus**

1.  **Generate Files:** Create a fully functional Signup and Signin flow, structured as Docusaurus-compatible React components/pages.
2.  **Authentication Logic:** Use a secure pattern for Better Auth. Use placeholders for API key access (e.g., `process.env.BETTER_AUTH_API_KEY`) and mark the official API call sections clearly with `// **BETTER AUTH INTEGRATION POINT**`.
3.  **Mandatory Signup Requirement (Personalization Data):** The Signup form **must** include extra steps to collect user background for personalization. Ask the following structured questions:
    * **Software Background:**
        * Primary Programming Language (Dropdown/Radio: Python, JavaScript, Java, C++, Other)
        * Main Framework Used (Text Input: e.g., React, Django, Spring Boot, Unity)
        * Experience Level (Dropdown: Beginner, Intermediate, Expert)
    * **Hardware Background:**
        * Primary Development OS (Dropdown: Windows, macOS, Linux)
        * Development Focus (Radio: Mobile, Desktop, Cloud/Backend)

**OUTPUT SPECIFICATIONS (Use SPECIFYPLUS for clarity):**

Generate the following six (6) files:

* `src/pages/Signup.js`: The Docusaurus page component calling the form.
* `src/components/SignupForm.js`: Component containing state, form fields (including background questions), and Better Auth Signup logic.
* `src/pages/Signin.js`: The Docusaurus page component calling the form.
* `src/components/SigninForm.js`: Component for standard Signin logic.
* `src/styles/AuthForms.css`: Comprehensive, modern CSS styling for both forms.
* `SETUP_INSTRUCTIONS.md`: Detailed step-by-step instructions for the user covering:
    1.  API Key setup (where to place the keys).
    2.  Exact file placement within a standard Docusaurus project structure.
    3.  Necessary package installations (`npm install ...`).

**CRITICAL SELF-CORRECTION & ERROR-CHECKING DIRECTIVE:**

Before finalizing the output for *any* file, you **must** perform a rigorous internal review. Specifically:
1.  **Self-Correction:** Check for common Docusaurus integration errors (e.g., using browser APIs without checking if `window` is defined, incorrect React hook usage in components).
2.  **Logic Validation:** Ensure the state management in `SignupForm.js` correctly handles both the standard credentials AND the background collection data before submitting to the Better Auth service.
3.  **Completeness Check:** Verify that *all* six specified files are generated and that the styling in `AuthForms.css` is referenced correctly in the React components.
4.  If you identify a potential error or improvement during this internal check, **correct it immediately** without generating a separate comment, ensuring the final code is production-ready and error-free.

**Start the output immediately using the SPECIFYPLUS format.**