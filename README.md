# 🧠 RAG Research Assistant

A simple Retrieval-Augmented Generation (RAG) app that allows you to ask questions and get intelligent answers based on your own PDF or text files.

## 🚀 Features

- PDF/Text ingestion and chunking
- Embedding with OpenAI and ChromaDB
- Semantic search using vector similarity
- Answer generation using OpenAI's GPT
- Clean Streamlit-based UI

## 🛠️ Tech Stack

- LangChain
- ChromaDB
- OpenAI (GPT-3.5/GPT-4)
- PyMuPDF
- Streamlit

## ⚙️ Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/AdnaikSushant/rag-research-assistant.git
cd rag-research-assistant


Create virtual environment and activate:
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Install dependencies:
pip install -r requirements.txt


Add your .env file:
OPENAI_API_KEY=your_openai_key_here


Run the app:
streamlit run app.py


📁 Folder Structure
├── app.py
├── README.md
├── requirements.txt
├── .env
├── data/
└── venv/



💡 Future Improvements
Source citation in responses

File upload from UI

RAG with open-source LLMs

Cloud deployment

🤝 Let's Connect
Built with ❤️ by Sushant Adnaik