from flask import request, jsonify
from app.configs.database import db
from app.models.vaccination_model import Vaccination
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

def get_vaccinations():
  try:
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 5))

    session: Session = db.session
    base_query = session.query(Vaccination)

    vaccinations = base_query.paginate(page, per_page)

    return jsonify({
      "page": page,
      "vaccinations": vaccinations.items
    }), 200
  except NotFound:
    return jsonify({"msg": "Not found"}), 404

def create_vaccination():
  try:
    data = request.json

    vaccination_data = {}
    vaccination_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]
    correct_values = {
      "cpf": "str",
      "name": "str",
      "vaccine_name": "str",
      "health_unit_name": "str"
    }

    missing_values = []
    invalid_values = {}

    for key in vaccination_keys:
      value_type: str = str(type(data.get(key)))[8:-2]

      if not data.get(key):
        missing_values.append(key)

      elif value_type != "str":
        invalid_values[key] = value_type

      vaccination_data[key] = data.get(key)

    if len(missing_values) > 0:
      response = {
        "missing_keys": missing_values,
        "avaliable_keys": vaccination_keys
      }
      raise TypeError(response)

    if len(invalid_values) > 0:
      response = {
        "correct_values": correct_values,
        "invalid_values": invalid_values
      }
      raise TypeError(response)

    if len(data.get("cpf")) != 11:
      raise TypeError({"error": "cpf max length is 11", "cpf": data.get("cpf")})

    vaccination = Vaccination(**vaccination_data)

    db.session.add(vaccination)
    db.session.commit()

    return jsonify(vaccination), 201

  except TypeError as err:
    return jsonify(err.args[0]), 400

  except IntegrityError as err:
    if "already exists" in err.args[0]:
      return jsonify({"error": "cpf already in use"}), 409