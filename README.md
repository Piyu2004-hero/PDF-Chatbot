# 📚 PDF-Chatbot
![Dashboard](Assets/overview.png)
An AI-powered PDF Chatbot built with **Streamlit**, **LangChain**, **ChromaDB**, **Sentence Transformers**, and **Groq LLM**. It uses **Retrieval-Augmented Generation (RAG)** to answer questions from PDF documents using semantic search and vector embeddings.

---

## 🚀 Features

- 📄 Chat with one or multiple PDF documents
- 🤖 AI-powered question answering using Groq LLM
- 🔍 Semantic search with vector embeddings
- 📚 Retrieval-Augmented Generation (RAG)
- 💾 ChromaDB vector database for efficient retrieval
- ⚡ Fast inference with Groq Llama 3.3
- 💬 Interactive chat interface built with Streamlit
- 📜 Chat history support
- 📊 PDF processing status and statistics dashboard

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Groq API
- PyPDF
- FAISS
- Python Dotenv

---

## 📂 Project Structure

```text
PDF-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── pdf_loader.py
│   └── vector_store.py
│
├── data/
│   └── (Place your PDF files here)
│
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PDF-Chatbot.git
```

### 2. Navigate to the project folder

```bash
cd PDF-Chatbot
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 📖 How to Use

1. Place your PDF files inside the `data/` folder.
2. Run the Streamlit application.
3. Click **Process PDFs** to generate embeddings and store them in ChromaDB.
4. Ask questions related to the uploaded PDF documents.
5. Receive accurate, context-aware answers powered by the RAG pipeline.

---

## 📸 Application Workflow

1. Load PDF documents
2. Split text into chunks
3. Generate embeddings using Sentence Transformers
4. Store embeddings in ChromaDB
5. Retrieve relevant document chunks
6. Generate answers using Groq Llama 3.3

---

## 📦 Dependencies

Some of the main libraries used:

- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- LangChain Community
- LangChain Groq
- PyPDF
- Python Dotenv
- FAISS

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- PDF upload from the web interface
- Source citations for responses
- Conversation memory
- Multi-user support
- Document summarization
- Support for Word, PowerPoint, and Text files
- Cloud deployment
- Authentication and user management

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

Copyright © 2026 Piyush Saxena

All rights reserved.

This project is provided for educational and portfolio purposes only. No part of this project may be copied, modified, distributed, or used commercially without prior written permission from the author.


---

## 👨‍💻 Author

**Piyush Saxena**

B.Tech CSE (AI & ML)

If you found this project helpful, consider giving it a ⭐ on GitHub!
