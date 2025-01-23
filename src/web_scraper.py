from langchain_community.document_loaders import WebBaseLoader
import os

os.environ["USER_AGENT"] = "MyApp/1.0"

def scrape_website(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    url = "https://www.promtior.ai/"
    docs = scrape_website(url)
    for doc in docs:
        print(doc.page_content[:500])  # Print the first 500 characters