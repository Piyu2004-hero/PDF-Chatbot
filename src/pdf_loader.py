from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
import os


def process_uploaded_pdfs(uploaded_files):
    """
    Process PDFs uploaded using Streamlit.
    """

    all_documents = []

    for uploaded_file in uploaded_files:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        loader = PyPDFLoader(temp_path)
        documents = loader.load()

        for doc in documents:
            doc.metadata["source_file"] = uploaded_file.name
            doc.metadata["file_type"] = "pdf"

        all_documents.extend(documents)

        os.remove(temp_path)

    return all_documents


def split_documents(
    documents,
    chunk_size=1000,
    chunk_overlap=200
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    return splitter.split_documents(documents)