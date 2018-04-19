from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder="views")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tranbo9x@172.16.69.251/status_page'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
