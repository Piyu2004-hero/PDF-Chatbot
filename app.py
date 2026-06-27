import streamlit as st

from src.pdf_loader import process_uploaded_pdfs, split_documents
from src.embeddings import EmbeddingManager
from src.vector_store import VectorStore, RAGRetriever
from src.chatbot import PDFChatbot

# Create a new vector database

vectorstore = VectorStore()

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stChatMessage {
    border-radius: 12px;
}

.history-box {
    padding: 8px;
    border-radius: 8px;
    background-color: #f5f5f5;
    margin-bottom: 5px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.title("📚 PDF Chatbot")

    st.markdown("---")

    st.markdown("### 🚀 Features")

    st.markdown("""
    ✅ Multi PDF Support

    ✅ Semantic Search

    ✅ RAG Pipeline

    ✅ ChromaDB

    ✅ Groq LLM

    ✅ Chat History
    """)

    st.markdown("---")

    st.subheader("📝 Chat History")

    user_questions = [
        msg["content"]
        for msg in st.session_state.messages
        if msg["role"] == "user"
    ]

    if len(user_questions) == 0:

        st.caption("No chat history yet")

    else:

        for idx, question in enumerate(user_questions):

            with st.expander(
                f"Q{idx+1}: {question[:40]}..."
            ):
                st.write(question)

    st.markdown("---")

    st.subheader("📊 Statistics")

    st.metric(
        "Questions",
        len(user_questions)
    )

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    st.metric(
        "PDF Status",
        "Processed" if st.session_state.pdf_processed else "Not Ready"
    )

    st.markdown("---")

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.rerun()

# ----------------------------------
# HEADER
# ----------------------------------

st.title("📄 Intelligent PDF Chatbot")

st.caption(
    "Ask questions from your PDFs using RAG + ChromaDB + Groq"
)

# ----------------------------------
# TOP METRICS
# ----------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model",
        "Llama 3.3 70B"
    )

with col2:
    st.metric(
        "Vector DB",
        "ChromaDB"
    )

with col3:
    st.metric(
        "Embeddings",
        "MiniLM"
    )

st.markdown("---")

# ----------------------------------
# PDF PROCESSING
# ----------------------------------

with st.expander(
    "📂 Upload PDF",
    expanded=True
):

    uploaded_files = st.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} PDF(s) selected."
        )

    if st.button("🚀 Process Uploaded PDFs"):

        if not uploaded_files:

            st.warning(
                "Please upload at least one PDF."
            )

        else:

            with st.spinner(
                "Processing PDFs..."
            ):

                docs = process_uploaded_pdfs(
                    uploaded_files
                )

                chunks = split_documents(docs)

                embedding_manager = EmbeddingManager()

                texts = [
                    chunk.page_content
                    for chunk in chunks
                ]

                embeddings = (
                    embedding_manager.generate_embeddings(
                        texts
                    )
                )

                vectorstore = VectorStore()

                vectorstore.add_documents(
                    chunks,
                    embeddings
                )

                st.session_state.retriever = RAGRetriever(
                    vectorstore,
                    embedding_manager
                )

                st.session_state.pdf_processed = True

            st.success(
                f"✅ Processed {len(uploaded_files)} PDF(s) into {len(chunks)} chunks."
            )

# ----------------------------------
# CHAT SECTION
# ----------------------------------

st.subheader("💬 Chat with PDFs")

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )

# ----------------------------------
# USER INPUT
# ----------------------------------

question = st.chat_input(
    "Ask anything from your PDFs..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    if not st.session_state.pdf_processed:

        warning_msg = (
            "⚠️ Please process PDFs first."
        )

        with st.chat_message("assistant"):
            st.warning(warning_msg)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": warning_msg
            }
        )

    else:

        chatbot = PDFChatbot()

        with st.chat_message("assistant"):

            with st.spinner(
                "Thinking..."
            ):

                answer = chatbot.ask(
                    question,
                    st.session_state.retriever
                )

                st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

st.caption(
    "🚀 Built with LangChain • ChromaDB • Sentence Transformers • Groq"
)

