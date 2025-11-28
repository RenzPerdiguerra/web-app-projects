# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# SQLALCHEMY


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:mayday09@localhost:5432/ds"

db = SQLAlchemy(app)






# sql alchemy