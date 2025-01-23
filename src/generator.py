import os
import subprocess

def generate_answer(context, query, model="llama3.2"):
    try:
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        print(f"Running command: ollama run {model}")
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        result.check_returncode()  # Raise an error if the subprocess fails
        return result.stdout.strip()
    except Exception as e:
        print(f"Error in generate_answer: {e}")
        raise


if __name__ == "__main__":
    # Example context and query
    context = "Promtior AI provides AI-driven solutions for data analysis and business automation."
    query = "What services does Promtior AI offer?"
    answer = generate_answer(context, query)
    print(answer)