from datetime import datetime
from app.models.lead_models import LeadModel
from app.configs.database import db
from flask import jsonify, request
from re import fullmatch
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


def create_lead():
    data = request.get_json()
    keys = LeadModel.keys
    wrong_keys = list(data.keys() - keys)
    default_keys = LeadModel.default_keys

    try:
        phone = data["phone"]
        valid_phone = fullmatch("(\(?\d{2}\)?)?(\d{4,5}\-\d{4})", phone)
        
        for key in default_keys:
            if key in data:
                raise KeyError
        
        if not valid_phone:
            return {"error": "phone must be (xx)xxxxx-xxxx"}, 400

        lead = LeadModel(**data)
        db.session.add(lead)
        db.session.commit()

        return jsonify({"data": lead}), 201
        

    except (KeyError, TypeError):
        return jsonify({"error": {"expected_keys": keys,"incoming_keys": wrong_keys}}), 400
    
    except IntegrityError as e:
        response = str(e.args)
        duplicated = "email" if "email" in response else "phone"

        return jsonify({"error": f"Key ({duplicated}) = ({data[duplicated]}) already exists"}), 409


def get_lead():
    leads = (
        LeadModel
        .query
        .all()
    )

    return jsonify({"leads":leads}), 200

def update_lead():
    time = datetime.now()
    data = request.get_json()

    if "email" not in data:
        return{"error": "the key needs to be 'email'"}, 400
    
    try:
        email = data["email"]
        lead_to_update = (
            LeadModel
            .query
            .filter_by(email=email)
            .first()
        )
        data["visits"] = lead_to_update.visits + 1
        data["last_visit"] = time
    
    except AttributeError:
        return {"error": "email not found"}, 404
    

    for key, value in data.items():
        setattr(lead_to_update, key, value)

    db.session.add(lead_to_update)
    db.session.commit()

    return "", 200

def delete_lead():
    data = request.get_json()

    if "email" not in data:
        return{"error": "the key needs to be 'email'"}, 400

    try:
        email = data["email"]
        to_delete = (
            LeadModel
            .query
            .filter_by(email=email)
            .first()
        )

        db.session.delete(to_delete)
        db.session.commit()

    except (AttributeError, UnmappedInstanceError):  
            return {"error": "email not found"}, 404

    return "", 200