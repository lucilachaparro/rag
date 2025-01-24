from langchain_community.document_loaders import WebBaseLoader

def scrape_website(url):
    print(f"Scraping website: {url}...")  # Debug log
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    url = "https://www.promtior.ai/"
    docs = scrape_website(url)
    for doc in docs:
        print(doc.page_content[:500])  # Print the first 500 characters