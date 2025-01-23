from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_index(documents, index_path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    vector_store.save_local(index_path)
    return vector_store

def load_vector_index(index_path):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def query_index(vector_store, query, k=3):
    results = vector_store.similarity_search(query, k=k) 
    return results

if __name__ == "__main__":
    from web_scraper import scrape_website
    from pdf_loader import load_pdf

    # Load data
    web_docs = scrape_website("https://www.promtior.ai/")
    pdf_docs = load_pdf("data/pdf/AIEngineer.pdf")
    combined_docs = web_docs + pdf_docs

    # Create vector index
    index_path = "data/vector_index"
    create_vector_index(combined_docs, index_path)

    vector_store = load_vector_index(index_path)
    query = "What services does Promtior offer?"
    results = query_index(vector_store, query)
    for result in results:
        print(result.page_content[:500])  # Print retrieved content