from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)


# initialize our database to work with our app
db.init_app(app)
migrate = Migrate(app, db)

from . import routes
from . import models