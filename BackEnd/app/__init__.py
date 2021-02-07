from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import os




app=Flask(__name__)

app.config['SECRET_KEY']='somekey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_PATH']='app/static/upload'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



from app import routes
from . import forms
import blog
import admin
from app import models
from admin import routes








# import auth
# import temp



