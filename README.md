# Quiz API
This **Flask-based API** serves collections of questions on various topics, such as **Current Affairs**, **Reasoning**, **Aptitude**, and other specific subjects. The API retrieves data from a **MongoDB database** and includes rate-limiting to manage usage. It is built with security in mind, requiring an API key for access.

## Features
- **Retrieve questions by collection name and topic.**
- **Supports multiple collections (e.g., "current_affairs", "reasoning", "aptitude").**
- **Rate-limited to 50 requests per hour per IP address (configurable).**
- **Secure access with API key authentication.**
- **Error handling for invalid requests, missing data, or database issues.**

## Technologies Used
- **Flask**
- **MongoDB**
- **Custom utilities and config**

## Directory Structure
```plaintext
quiz-api/
├── api/
│   ├── app.py              
│   ├── routes.py          
│   ├── database.py        
│   ├── config.py          
│   └── .env              
│   └── .gitignore        
├── sample_ket.txt        
├── vercel.json          
├── README.md           
└── requirements.txt    


Installation
Clone the Repository
bash
git clone <repository-url>
cd <repository-folder>
Set Up a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
bash
pip install -r requirements.txt
Configure Environment Variables
Create a .env file in the root directory with the following:

API_KEY=your_api_key_here
URI=your_mongodb_connection_string
DB=your_database_name
SECRET_KEY=your_flask_secret_key
Usage
Run the Application
bash
python api/app.py
The API will be available at http://127.0.0.1:5000/.

API Endpoints
Home
URL: /

Method: GET

Description: Returns a welcome message.

Response:

json
{
  "message": "This is home page"
}
Get Questions
URL: /get_questions/<collection_name>/<topic>

Method: GET

Parameters:

collection_name: Name of the collection (e.g., "current_affairs", "reasoning", "aptitude").

topic: Specific topic within the collection (e.g., "politics", "logic", "math").

api_key: Query parameter for authentication (required).

Example Request:

bash
curl "http://127.0.0.1:5000/get_questions/current_affairs/politics?api_key=your_api_key_here"
Success Response (200):

json
{
  "_id": "Politics",
  "questions": [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "Who is the current US President?", "a": "Joe Biden"}
  ]
}
Error Responses:

401 Unauthorized (Invalid/Missing API Key):

json
{"error": "Invalid or missing API key"}
404 Not Found (Collection/Topic Not Found):

json
{"error": "Collection 'current_affairs' not found"}
json
{"error": "No questions found for topic 'Politics'"}
500 Internal Server Error (Database/General Error):

json
{"error": "Database connection failed: <error_message>"}
Rate Limiting
Default: 200 requests per day, 50 requests per hour per IP.

Specific Endpoint Limit: /get_questions is capped at 50 requests per hour.

Database Structure
Collections: Separate collections for each category (e.g., "current_affairs", "reasoning", "aptitude").

Document Schema:

json
{
  "_id": "TopicName",
  "questions": [
    {"q": "Question text", "a": "Answer text"},
    ...
  ]
}
Example Usage
To fetch reasoning questions on "logic":

bash
curl "http://127.0.0.1:5000/get_questions/reasoning/logic?api_key=your_api_key_here"
Contributing
Fork the repository.

Create a feature branch:

bash
git checkout -b feature/new-feature
Commit changes:

bash
git commit -m "Add new feature"
Push to the branch:

bash
git push origin feature/new-feature
Create a Pull Request.

Feel free to make any further modifications. If you need additional assistance, let me know!

Acknowledgments
Thanks to the open-source community for providing valuable resources and libraries.