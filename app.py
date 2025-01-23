from flask import Flask, request, jsonify, render_template
from src.retriever import load_vector_index, query_index
from src.generator import generate_answer
app = Flask(__name__)

# Load the FAISS vector index
index_path = "data/vector_index"
vector_store = load_vector_index(index_path)

@app.route("/")
def home():
    return render_template("chat.html")  # Chat UI

@app.route("/ask", methods=["POST"])
def ask_question():
    """
    API endpoint to handle user queries.
    """
    from traceback import format_exc  # For debugging
    
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Retrieve relevant documents
        results = query_index(vector_store, query, k=3)
        context = " ".join([doc.page_content for doc in results])

        # Generate answer using the model
        answer = generate_answer(context, query, model="llama3.2")

        return jsonify({"query": query, "answer": answer})

    except Exception as e:
        # Log detailed error information for debugging
        print("Error occurred while processing the query:")
        print(format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
