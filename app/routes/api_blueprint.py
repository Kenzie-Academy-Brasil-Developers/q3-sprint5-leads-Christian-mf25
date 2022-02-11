from flask import Blueprint
from app.routes.lead_blueprint import bp_lead

bp_api = Blueprint("bp_api", __name__, url_prefix="/")

bp_api.register_blueprint(bp_lead)