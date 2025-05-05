from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


def retrieve_top_documents(query, k=3):
    embedding_model = OpenAIEmbeddings()
    vectorstore = Chroma(persist_directory="./vector_db", embedding_function=embedding_model)

    docs = vectorstore.similarity_search(query, k=k)
    return docs
