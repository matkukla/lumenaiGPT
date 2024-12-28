from flask import Flask, request, jsonify
from core import generate_response
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

app = Flask(__name__)

@app.route("/lumenai", methods=["POST"])
def lumenai():
    """
    Endpoint for handling user queries to LumenAI.
    """
    data = request.json
    user_input = data.get("input", "")

    if not user_input:
        return jsonify({"error": "Input is required"}), 400

    # Generate response
    response = generate_response(SYSTEM_PROMPT, user_input, FEW_SHOT_EXAMPLES)
    return jsonify({"response": response})

@app.route("/examples", methods=["GET"])
def examples():
    """
    Endpoint to fetch few-shot examples for debugging or frontend integration.
    """
    return jsonify({"examples": FEW_SHOT_EXAMPLES.split("\n")})

if __name__ == "__main__":
    app.run(debug=True)
