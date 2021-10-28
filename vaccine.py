from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, InfoModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@<server>:5432/<db_name>"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
migrate = Migrate(app, db)
 
@app.route('/')
 
def new_func(app):
    app.run(debug=True)

if __name__ == '__main__':
    new_func(app)