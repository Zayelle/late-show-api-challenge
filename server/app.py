from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db  # <-- use this db object only
from server.controllers.auth_controller import auth_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.appearance_controller import appearance_bp
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure app
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Initialize extensions using existing db from server.models
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(episode_bp, url_prefix='/episodes')
app.register_blueprint(guest_bp, url_prefix='/guests')
app.register_blueprint(appearance_bp, url_prefix='/appearances')

# Root route
@app.route('/')
def index():
    return {'message': 'Late Show API is running'}





