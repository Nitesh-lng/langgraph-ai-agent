# 🤖 LangGraph AI Agent

An advanced AI chatbot interface built with **LangGraph**, supporting **Groq** and **OpenAI** models. Includes optional **web search via Tavily**, a FastAPI backend, and a Streamlit frontend.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-green)
![Streamlit](https://img.shields.io/badge/frontend-Streamlit-orange)
![LangGraph](https://img.shields.io/badge/langgraph-powered-blueviolet)

---

## 📚 Table of Contents

- [✨ Features](#-features)
- [📸 Preview](#-preview)
- [🚀 Getting Started](#-getting-started)
- [📁 Project Structure](#-project-structure)
- [🤖 Supported Models](#-supported-models)
- [📜 License](#-license)
- [🤝 Contributions](#-contributions)

---

## ✨ Features

- 🔗 Powered by [LangGraph](https://www.langchain.dev/langgraph)
- 🧠 Supports multiple LLM providers (Groq, OpenAI)
- 🌐 Optional web search with Tavily
- ⚙️ Backend: FastAPI
- 🎨 Frontend: Streamlit
- 🛠️ Modular and easy to extend

---

## 📸 Preview


---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/langgraph-ai-agent.git
cd langgraph-ai-agent
```

### 2. Install dependencies

It's recommended to use a virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Setup environment variables

Create a `.env` file:

```env
# .env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Or use the provided example:

```bash
cp .env.example .env
```

### 4. Run the backend server

```bash
uvicorn backend:app --reload --port 9998
```

### 5. Run the frontend

```bash
streamlit run frontend.py
```

---

## 📁 Project Structure

| File/Folder        | Purpose                                  |
|--------------------|------------------------------------------|
| `ai_agent.py`      | Core logic for AI agent setup            |
| `backend.py`       | FastAPI server for chat interaction      |
| `frontend.py`      | Streamlit UI for chatting with the agent |
| `requirements.txt` | Python dependencies                      |
| `.env.example`     | Sample env config (API keys)             |
| `assets/`          | Screenshots and media                    |

---

## 🤖 Supported Models

- **Groq:**
  - `gemma2-9b-it`, `gemma2-13b-it`, `llama-3.3-70b-versatile`, etc.
- **OpenAI:**
  - `gpt-4o-mini`

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

---

## 🤝 Contributions

Have an idea? Found a bug? Want to add a feature?

Feel free to open an issue or submit a pull request!  
⭐ Star this repo to support the project!

---
