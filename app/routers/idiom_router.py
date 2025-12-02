# app/routes/idiom_routes.py
import json
from flask import Blueprint, request, jsonify
from app.services import gemini_service # Import your service function

# Create a Blueprint instance
idiom_bp = Blueprint('idiom', __name__)

@idiom_bp.route("/explain_idiom", methods=["POST"])
def explain_idiom_endpoint():
    """
    Handles POST requests from the Swift app to get an idiom explanation.
    """
    if not request.is_json:
        # Flask utility to return an error JSON response
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    idiom_text = data.get('idiom')
    
    if not idiom_text:
        return jsonify({"error": "Missing 'idiom' field in request body"}), 400

    try:
        # 1. Call the service function to get the result (Separation of Concerns!)
        explanation_text = gemini_service.get_idiom_explanation(idiom_text)
        
        # 2. Return the structured JSON response to the Swift app
        return jsonify({"explanation": explanation_text}), 200
        
    except Exception as e:
        # Log the error and return a 500 server error
        print(f"AI service error: {e}")
        return jsonify({"error": "Internal server error while processing the request."}), 500