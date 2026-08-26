from flask import Flask
from flask_cors import CORS

from database.db import db
from routes.asset_routes import asset_bp


# Create Flask application
app = Flask(__name__)

CORS(app)


# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cloudasset.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize database
db.init_app(app)


# Register API routes
app.register_blueprint(asset_bp)


# Home route
@app.route("/")
def home():
    return {
        "message": "CloudAsset Backend Running 🚀"
    }


# Create database tables
with app.app_context():
    db.create_all()


# Run application
# host="0.0.0.0" makes the server reachable from outside Docker container
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)