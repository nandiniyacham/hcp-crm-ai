# 🧠 AI-First CRM – HCP Interaction Module

## 📌 Overview

This project is an AI-first Customer Relationship Management (CRM) system designed for logging and managing Healthcare Professional (HCP) interactions.

It enables field representatives to log interactions using:

* 📋 Structured Form Input
* 💬 Conversational Chat Interface (AI-powered)

The system uses an LLM-powered agent to convert unstructured text into structured CRM data automatically.

---

## 🚀 Features

* 💬 Chat-based interaction logging using AI
* 📋 Auto-filled structured CRM form
* 🧠 LLM-powered data extraction (Groq API)
* 🤖 AI-powered field extraction (HCP name, sentiment, follow-up, etc.)
* 🔁 Edit existing interactions
* 📅 Follow-up scheduling
* 📊 Insights generation
* ✅ Compliance checking
* 🗄️ Database storage (MySQL)

---

## 🏗️ Tech Stack

### Frontend

* React.js
* Redux Toolkit
* CSS (Google Inter Font)

### Backend

* FastAPI (Python)
* SQLAlchemy ORM

### AI & Agent

* LangGraph (conceptual workflow)
* Groq LLM API (`gemma2-9b-it`, fallback: `llama-3.3-70b-versatile`)

### Database

* MySQL

---

## 🧠 LangGraph Agent Design

The LangGraph agent manages CRM workflows by routing user actions to specific tools.

### 🔧 Tools Implemented

1. **Log Interaction** – Converts free text into structured CRM data using LLM
2. **Edit Interaction** – Updates existing records
3. **Schedule Follow-up** – Suggests next action date
4. **Generate Insights** – Provides summaries
5. **Compliance Check** – Flags issues

---

## 🔗 LangGraph Workflow (Conceptual Implementation)

The LangGraph framework is used to manage tool-based execution flow.

### Workflow Steps:

1. User input enters the system
2. LangGraph routes the request to the appropriate tool:

   * Log Interaction
   * Edit Interaction
   * Schedule Follow-up
   * Generate Insights
   * Compliance Check
3. The selected tool processes the request
4. LLM is used where required (e.g., Log Interaction for data extraction)
5. Structured output is returned to frontend

### Note:

Currently, a simplified agent structure is implemented that mimics LangGraph behavior. This can be extended into a full LangGraph state machine using `StateGraph` for production-level orchestration.

---

## 🔄 System Workflow

1. User enters interaction via chat
2. Frontend sends request to backend
3. LangGraph agent processes input
4. LLM extracts structured data
5. Data stored in MySQL
6. UI auto-fills form

---

## 📸 UI Layout

* **Left Panel:** Structured CRM Form
* **Right Panel:** AI Chat Interface

---

## 📁 Project Structure

```
hcp-crm-ai/
│
├── backend/
├── frontend/
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at: http://127.0.0.1:8000

---

### 🔹 Frontend

```bash
cd frontend
npm install
npm start
```

Frontend runs at: http://localhost:3000

---

## 🔐 Environment Variables

Create `.env` file in backend:

```
GROQ_API_KEY=your_api_key_here
```

---

## 📡 API Endpoints

| Endpoint           | Method | Description          |
| ------------------ | ------ | -------------------- |
| /chat              | POST   | Log interaction      |
| /edit/{id}         | PUT    | Edit interaction     |
| /interactions      | GET    | Get all interactions |
| /schedule_followup | POST   | Suggest follow-up    |
| /generate_insights | POST   | Generate insights    |
| /compliance_check  | POST   | Compliance check     |

---

## 🧪 Example Usage

**Input (Chat):**
"Met Dr. Sharma yesterday for a product discussion. Shared brochure and samples. He was interested. Will follow up next week."

**AI Output (Structured):**

* HCP Name: Dr. Sharma
* Interaction Type: Meeting
* Sentiment: Positive
* Materials Shared: Brochure, Samples
* Follow-up: Follow up next week

---

## 📚 What I Learned

* LLM integration in real-world applications
* Converting unstructured text into structured data
* Designing AI-driven CRM workflows
* Understanding LangGraph-based tool orchestration
* Full-stack development (React + FastAPI + MySQL)

---

## 📌 Future Improvements

* Full LangGraph state machine implementation
* Improved NLP accuracy for entity extraction
* Role-based access (Sales Rep, Manager)
* Advanced analytics dashboard
* Real-time notifications and follow-ups

---

## 🙌 Conclusion

This project demonstrates how AI simplifies CRM workflows in life sciences by automating interaction logging, improving data accuracy, and reducing manual effort for field representatives.
