from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


def generate_answer(query, docs):
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = f"Answer the question using the following context:\n\n{context}\n\nQuestion: {query}"

    response = llm.predict(prompt)
    return response
