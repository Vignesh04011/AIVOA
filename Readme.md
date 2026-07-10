# 🏥 AI-Powered HCP CRM Assistant

An AI-powered Healthcare CRM Assistant that enables Medical Representatives to log, edit, analyze, and manage Healthcare Professional (HCP) interactions using Natural Language Processing and Large Language Models.

The application combines a modern React frontend, FastAPI backend, LangGraph multi-agent workflow, Groq LLMs, and PostgreSQL to automate CRM interaction management.

---

# Features

## AI Interaction Extraction

Convert natural language into structured CRM interaction data.

Example:

> I met Dr. Smith yesterday around 8 PM. We discussed diabetes therapy and I shared a brochure.

Automatically extracts:

- HCP Name
- Interaction Type
- Date
- Time
- Attendees
- Topics Discussed
- Materials Shared
- Sentiment
- Outcomes
- Follow-up Actions

---

## AI Editing

Modify existing interactions using natural language.

Examples:

- Change meeting time to 7 PM
- Actually it was Dr. Eva
- Remove brochure
- Attendees were Vignesh
- Sentiment was Neutral

Only requested fields are updated while preserving all others.

---

## AI Summary

Generate concise summaries of interactions.

---

## Medical Insights

Generate AI-powered medical insights from interaction details.

---

## Recommendations

Generate intelligent follow-up recommendations for future HCP engagement.

---

## Interaction Search

Search previously logged CRM interactions using natural language.

Example:

- Show all meetings with Dr. Smith
- Previous interactions with Dr. Eva

---

## CRM Interaction Logging

Save structured interactions into PostgreSQL.

---

# Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios

---

## Backend

- FastAPI
- LangGraph
- Groq API
- SQLAlchemy
- PostgreSQL
- Pydantic

---

## AI

- Llama 3.3 70B Versatile
- LangGraph Multi-Agent Workflow

---

# Multi-Agent Architecture

```
                User
                  │
                  ▼
        Supervisor Agent
                  │
        Determines execution plan
                  │
                  ▼
           Executor Agent
                  │
      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼

 Interaction    Summary     Medical

      │           │            │

      ▼           ▼            ▼

 Recommendation  Search      Save

                  │

                  ▼

          Formatter Agent

                  │

                  ▼

             JSON Response
```

---

# Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── config/
│   ├── database/
│   ├── graph/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── api/
│   └── App.jsx
```

---

# Workflow

1. User enters a natural language request.
2. Supervisor Agent identifies required tool(s).
3. Executor Agent executes AI agents.
4. Formatter Agent formats the final response.
5. React updates:
   - CRM Form
   - AI Chat
6. User can log interaction into PostgreSQL.

---

# Installation

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Runs at

```
http://localhost:5173
```

---

# Environment Variables

Create a `.env` file inside the backend.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

DATABASE_URL=postgresql://username:password@localhost/database_name
```

---

# API Endpoints

## Chat

```
POST /chat
```

Example

```json
{
  "message": "I met Dr. Smith yesterday around 8 PM.",
  "interaction": {}
}
```

---

## Create Interaction

```
POST /interactions
```

Stores interaction into PostgreSQL.

---

# Example AI Commands

Extraction

```
I met Dr. Smith yesterday around 8 PM.
```

Editing

```
Change meeting time to 7 PM.

Actually it was Dr. Eva.

Remove brochure.
```

Summary

```
Summarize this interaction.
```

Medical Insights

```
Generate medical insights.
```

Recommendations

```
Recommend follow-up actions.
```

Search

```
Show previous meetings with Dr. Smith.
```

Save

```
Log this interaction.
```

---

# Future Improvements

- Voice Interaction
- Authentication
- Multi-user support
- File attachments
- Calendar integration
- Email reminders
- Analytics Dashboard
- RAG-based knowledge retrieval
- Session memory
- Role-based access control

---

# Author

**Vignesh Vane**

AI & Machine Learning Engineer

GitHub: https://github.com/Vignesh04011

LinkedIn: https://www.linkedin.com/

---

# License

This project was developed as part of an AI Healthcare CRM assignment and is intended for educational and demonstration purposes.