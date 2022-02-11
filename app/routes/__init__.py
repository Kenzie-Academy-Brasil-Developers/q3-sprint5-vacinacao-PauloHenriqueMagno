from flask import Flask
from app.routes.vaccinations_route import bp_vaccinations

def init_app(app: Flask):
  app.register_blueprint(bp_vaccinations)