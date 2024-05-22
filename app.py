import streamlit as st
import logging

from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader, PyPDFLoader
from ragatouille import RAGPretrainedModel
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from ragatouille import RAGPretrainedModel
from langchain_community.chat_models import ChatOllama

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
except Exception as e:
    logger.error(f"Error loading RAG model: {e}")
    raise

# Load and split the data
try:
    load_hull_data = TextLoader("data.txt")
    hull_data_pages = load_hull_data.load_and_split()
    hull_document = ""
    for hull_page in hull_data_pages:
        hull_document += hull_page.page_content
except Exception as e:
    logger.error(f"Error loading and splitting data: {e}")
    raise

# Specify the index name
index_name = "hull_data"

# Create a retriever
try:
    retriever = RAG.as_langchain_retriever(index_name="hull_data", k=3)
except Exception as e:
    logger.error(f"Error creating retriever: {e}")
    raise

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}"""
)

# Create a language model
# llm = ChatOpenAI(streaming=True, max_tokens=150)
llm = ChatOllama(streaming=True, max_tokens=150)


# Create a document chain and retrieval chain
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

def ask_question(question):
    try:
        response = retrieval_chain.invoke({"input": question})
        return response["answer"]
    except Exception as e:
        logger.error(f"Error asking question: {e}")
        raise

st.title("Question Answering with Langchain and RAGatouille")
st.write("Type your question and press Enter to get an answer based on the loaded data.")

question = st.text_input("Ask a question...")

if question:
    try:
        answer = ask_question(question)
        st.write(answer)
    except Exception as e:
        st.error(f"An error occurred: {e}")


# question = st.text_input("Ask a question...")1