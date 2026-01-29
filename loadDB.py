from langchain_community.document_loaders import PyPDFDirectoryLoader
data = "D:/RAG/with_Local_llm/ollma_RAG/data"

def load_documents():
    document_loader = PyPDFDirectoryLoader(data)
    return document_loader.load()

documents = load_documents()
print(documents[0])

