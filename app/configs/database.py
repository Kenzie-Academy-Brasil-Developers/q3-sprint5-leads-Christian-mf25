from re import S
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()

def init_app(app: Flask):
	db.init_app(app)
	app.db = db

	from app.models.lead_models import LeadModel