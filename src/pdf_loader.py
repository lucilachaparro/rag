from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    print(f"Loading pdf: {file_path}...")  # Debug log
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    pdf_path = "data/pdf/AIEngineer.pdf"
    docs = load_pdf(pdf_path)
    for doc in docs:
        print(doc.page_content[:500])  # Print the first 500 characters