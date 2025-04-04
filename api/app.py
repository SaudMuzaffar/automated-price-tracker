import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from flask import Flask
from flask_restx import Api
from routes import api as product_namespace
from database.database import create_tables



def create_app():
    app = Flask(__name__)
    api = Api(
        app,
        version="1.0",
        title="Automated Price Tracker API",
        description="Track product prices over time",
        doc="/swagger"  # Swagger UI at /swagger
    )
    
    api.add_namespace(product_namespace, path="/api/products")

    return app

if __name__ == "__main__":
    create_tables()
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
