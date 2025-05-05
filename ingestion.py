from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from dotenv import load_dotenv

load_dotenv()

def load_and_embed_documents():
    loader = PyPDFLoader("/Users/sushantadnaik/Documents/Projects/rag-research-assistant/data/Publishedpaper.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents) 

    embedding_model = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(chunks, embedding_model, persist_directory="./vector_db")  

    print("Documents embedded and saved!")
    return vectorstore

if __name__ == "__main__":
    load_and_embed_documents()
