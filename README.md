# RAG Chatbot - Promtior

Hi! This is my technical test submission. It consists of a Retrieval-Augmented Generation (RAG) project in which you can ask a chatbot 🤖 questions about **Promtior**.

The project uses Python and LangChain, combining a retrieval mechanism to fetch relevant information from Promtior's website and the provided PDF file, and a generative model to provide meaningful answers. It has a simple front-end application to interact with the bot.

In this case, the model used is a local Llama 3.2 model. This means the app's performance will depend on the characteristics of the system where it runs. 

## How to Run    
To run locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/lucilachaparro/rag.git
2. Set up a virtual environment inside the project's directory
   ```bash
   python -m venv venv
3. Activate the virtual environment
   ```bash
   source venv/bin/activate
4. Install dependencies
    ```bash
   pip install -r requirements.txt
5. Run the app
   ```bash
   python app.py
To use online
1. Go to [lucila.dev](https://lucila.dev) 😊



## Test questions
- Ask the bot questions about Promtior and get detailed, accurate answers.
- The two questions the app should be able to answer to pass this test are:
  1. What services does Promtior offer?
  2. When was the company founded?
 
