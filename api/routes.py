from api.app import app, limiter
from api.database import connect_database
from api.config import API_KEY
from flask import jsonify, request

@app.route('/')
def home():
    return jsonify({"message": "This is home page"})

@app.route('/get_questions/<collection_name>/<topic>', methods=["GET"])
@limiter.limit("50 per hour")
def get_questions(collection_name, topic):
    try:
        # Get and validate API key
        api_key = request.args.get("api_key")
        if not api_key or api_key != API_KEY:
            return jsonify({"error": "Invalid or missing API key"}), 401

        # Connect to database
        db = connect_database()
        if isinstance(db, str):  # Check if error message was returned
            return jsonify({"error": f"Database connection failed: {db}"}), 500
        
        # Verify if collection exists
        if collection_name not in db.list_collection_names():
            return jsonify({"error": f"Collection '{collection_name}' not found"}), 404
        
        # Get collection
        collection = db[collection_name]
        
        # Capitalize topic and search
        topic_ = topic.capitalize()
        result = collection.find_one({"_id": topic_})
        
        if result is None:
            return jsonify({"error": f"No questions found for topic '{topic_}'"}), 404
            
            
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500