# run.py
from app import create_app

# Create and run the application
app = create_app()

if __name__ == "__main__":
    # Flask default: runs on http://127.0.0.1:5000/
    app.run(debug=True)