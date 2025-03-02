from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from api.config import SECRET_KEY  

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize the Limiter with default limits
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
)

# Bind the limiter to the app
limiter.init_app(app)

from api.routes import*

# if __name__ == "__main__":
#     from routes import*
#     app.run()