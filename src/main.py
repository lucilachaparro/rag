from retriever import create_vector_index, load_vector_index, query_index
from generator import generate_answer
from web_scraper import scrape_website
from pdf_loader import load_pdf

def clean_text(text):
    return text.replace("\u200b", "").strip()

if __name__ == "__main__":
    # Load or create index
    index_path = "data/vector_index"
    try:
        vector_store = load_vector_index(index_path)
    except:
        print("Creating new vector index...")
        web_docs = scrape_website("https://www.promtior.ai/")
        pdf_docs = load_pdf("data/pdf/AIEngineer.pdf")
        combined_docs = web_docs + pdf_docs
        vector_store = create_vector_index(combined_docs, index_path)

    # Query the pipeline
    query = "What services does Promtior offer?"
    results = query_index(vector_store, query)

    # Generate answer
    context = " ".join([doc.page_content for doc in results])
    context = clean_text(context)
    query = clean_text(query)
    answer = generate_answer(context, query)
    print(f"Q: {query}\nA: {answer}")