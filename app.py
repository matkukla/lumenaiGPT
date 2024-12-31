from flask import Flask, request, jsonify
from flask_cors import CORS
from core import generate_response
from prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES

app = Flask(__name__)
# List of allowed origins
ALLOWED_ORIGINS = [
    "https://lumen-ai.lovable.app",
    "https://8c6b1832-9804-49a9-9a07-fa7a0fb29fa6.lovableproject.com"
]

CORS(app, resources={r"/api/*": {
    "origins": ALLOWED_ORIGINS,
    "methods": ["POST", "OPTIONS"],
    "allow_headers": ["Content-Type"]
}})

@app.after_request
def add_cors_headers(response):
    """
    Dynamically add CORS headers to the response.
    """
    origin = request.headers.get("Origin")
    if origin in ALLOWED_ORIGINS:
        response.headers["Access-Control-Allow-Origin"] = origin
    return response


@app.route("/api/lumenai", methods=["POST", "OPTIONS"])
def lumenai():
    """
    Endpoint for handling user queries to LumenAI.
    """
    if request.method == "OPTIONS":
        # Respond to preflight request
        response = jsonify({"message": "Preflight request accepted"})
        response.headers.add("Access-Control-Allow-Origin", request.headers.get("Origin"))
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response
    
     # Handle actual POST request
    try:
        data = request.json
        user_input = data.get("input", "").strip()

        if not user_input:
            return jsonify({"error": "Input cannot be empty"}), 400

        # Generate response
        bot_response = generate_response(SYSTEM_PROMPT, user_input, FEW_SHOT_EXAMPLES)
        response = jsonify({"response": bot_response})

        # Add CORS header to POST response
        origin = request.headers.get("Origin")
        if origin in ALLOWED_ORIGINS:
            response.headers["Access-Control-Allow-Origin"] = origin
        return response

    except Exception as e:
        print(f"Error handling request: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

@app.route("/examples", methods=["GET"])
def examples():
    """
    Endpoint to fetch few-shot examples for debugging or frontend integration.
    """
    return jsonify({"examples": FEW_SHOT_EXAMPLES.split("\n")})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
