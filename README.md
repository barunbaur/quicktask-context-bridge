# ⚡ QuickTask Context Bridge

A lightweight Python and Streamlit web app that converts messy notes, emails, and chat logs into prioritized, interactive action checklists with instant JSON export.

🔗 **Live Demo:** [quicktask-context-bridge.streamlit.app](https://quicktask-context-bridge.streamlit.app/)

---

## 🎯 The Problem
Important action items frequently get buried inside unstructured meeting notes, chat threads, and emails. Manually formatting tasks, assigning urgency, and structuring data for downstream tools adds daily friction.

## ✨ Key Features
* **Instant Text-to-Task Parsing:** Strips bullet clutter and converts raw multi-line notes into clean action items in one click.
* **Automatic Priority Detection:** Flags tasks as **High** (🔴), **Medium** (🟡), or **Low** (🟢) based on urgency and deadline keywords.
* **Interactive Checklist:** Track completion directly inside the browser.
* **Structured JSON Export:** Download a clean, uniquely ID'd JSON payload ready for automation pipelines (e.g., Make.com, webhooks, or local trackers).

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** Streamlit
* **Hosting:** Streamlit Community Cloud & GitHub

## 🚀 Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/barunbaur/quicktask-context-bridge.git
   cd quicktask-context-bridge
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies and launch:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```
