from flask import Blueprint
from app.controllers import vaccinations_controller

bp_vaccinations = Blueprint("vaccinations", __name__, url_prefix = "/vaccinations")

bp_vaccinations.get("")(vaccinations_controller.get_vaccinations)
bp_vaccinations.post("")(vaccinations_controller.create_vaccination)