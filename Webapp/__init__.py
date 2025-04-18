from flask import Flask

app = Flask(__name__)  # Initialize the Flask app

# Import routes after app initialization to avoid circular imports
from Webapp import main  # Import the main module where the routes are defined
