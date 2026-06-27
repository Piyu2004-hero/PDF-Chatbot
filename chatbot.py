import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class PDFChatbot:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=os.getenv(
                "GROQ_API_KEY"
            ),
            model="llama-3.3-70b-versatile",
            temperature=0
        )

    def ask(
        self,
        question,
        retriever
    ):

        results = retriever.retrieve(
            question,
            top_k=3
        )

        context = "\n\n".join(
            [
                doc["content"]
                for doc in results
            ]
        )

        prompt = f"""
Use the following context to answer.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.invoke(
            prompt
        )

        return response.content