from flask import Flask, request, jsonify
from flask_cors import CORS
from core import generate_response
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

app = Flask(__name__)
#CORS(app, resources={r"/api/*": {"origins": "https://lumen-ai.lovable.app"}})
CORS(app, resources={r"/api/*": {
    "origins": "https://lumen-ai.lovable.app",
    "methods": ["POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})


@app.route("/api/lumenai", methods=["POST"])
def lumenai():
    """
    Endpoint for handling user queries to LumenAI.
    """
    if request.method == "OPTIONS":
        # Respond to preflight request
        response = jsonify({"message": "Preflight request accepted"})
        response.headers.add("Access-Control-Allow-Origin", "https://lumen-ai.lovable.app")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response
    
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
    app.run(host='0.0.0.0', port=5000)
