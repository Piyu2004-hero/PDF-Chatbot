import uuid
import chromadb


class VectorStore:

    def __init__(
        self,
        collection_name="pdf_documents"
    ):

        # In-memory ChromaDB
        self.client = chromadb.Client()

        # Get the collection if it exists, otherwise create it
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        documents,
        embeddings
    ):

        ids = []
        docs = []
        metas = []
        embs = []

        for doc, emb in zip(documents, embeddings):

            ids.append(f"doc_{uuid.uuid4().hex}")

            docs.append(doc.page_content)

            metas.append(dict(doc.metadata))

            embs.append(emb.tolist())

        self.collection.add(
            ids=ids,
            documents=docs,
            metadatas=metas,
            embeddings=embs
        )


class RAGRetriever:

    def __init__(
        self,
        vector_store,
        embedding_manager
    ):

        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(
        self,
        query,
        top_k=5
    ):

        query_embedding = (
            self.embedding_manager
            .generate_embeddings([query])[0]
        )

        results = self.vector_store.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=top_k
        )

        docs = []

        if results["documents"]:

            for doc, meta, distance in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            ):

                docs.append(
                    {
                        "content": doc,
                        "metadata": meta,
                        "similarity_score": 1 - distance
                    }
                )

        return docs