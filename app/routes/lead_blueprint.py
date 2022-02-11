from flask import Blueprint

from app.controllers.lead_controller import create_lead, delete_lead, get_lead, update_lead

bp_lead = Blueprint("bp_lead", __name__, url_prefix="/leads")
bp_lead.post("")(create_lead)
bp_lead.get("")(get_lead)
bp_lead.patch("")(update_lead)
bp_lead.delete("")(delete_lead)