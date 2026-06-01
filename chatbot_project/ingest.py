from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma


loader = PyPDFLoader(
    "docs/Employee-Handbook.pdf"
)

documents = loader.load()

print(
    f"Loaded {len(documents)} pages"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(
    documents
)

print(
    f"Created {len(chunks)} chunks"
)

Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)

print(
    "Employee handbook loaded successfully."
)