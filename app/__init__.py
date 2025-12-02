# app/__init__.py
from flask import Flask
from dotenv import load_dotenv

# Load .env file at the very start
load_dotenv() 

def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # --- Register Blueprints ---
    from app.routers.idiom_router import idiom_bp
    app.register_blueprint(idiom_bp)

    return app