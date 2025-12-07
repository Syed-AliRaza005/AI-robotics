# Constitution: Physical AI & Humanoid Robotics Textbook

## 1. Core Principles

- **Authoritative Source:** The course structure and content defined in `hackathon.md` are the single source of truth.
- **Spec-Driven Development:** All development will follow the Spec-Kit Plus workflow: Constitution -> Spec -> Plan -> Tasks -> Implement.
- **AI-First Workflow:** The entire project will be developed by an AI agent, ensuring consistency and adherence to these rules.

## 2. Technical Standards

- **Framework:** The project must use **Docusaurus 3.x**. All features and configurations must be compatible with the latest stable version.
- **Dependencies:** All dependencies must be kept up-to-date to ensure compatibility with modern, high-performance deployment environments like **Context7 (MCPS)**.
- **Styling:** The visual design should be clean, professional, and enhance readability. Custom styling should be minimal and implemented via Docusaurus's standard mechanisms (e.g., `custom.css`).

## 3. Content and Code

- **Language:** All explanatory text will be in clear, professional English.
- **Code Examples:** All code examples and snippets will be written in **Python**, unless a specific technology (like shell commands or URDF) requires another language.
- **Content Integrity:** The generated content must accurately reflect the topics outlined in `hackathon.md`, including the 13-week structure, modules, and hardware requirements.

## 4. Deployment

- **Target Platform:** The final output will be a static website ready for deployment on **GitHub Pages**.
- **Configuration:** The `docusaurus.config.js` file must be correctly configured for this deployment target, including the `baseUrl` and `organizationName`/`projectName` fields.

## 5. Acceptance Criteria

- The final website must build successfully without errors.
- The sidebar navigation must correctly reflect the 13-week course structure.
- All specified pages (Hardware, Assessments, Learning Outcomes) must be present and populated.
- The site must be viewable and navigable on modern web browsers.
