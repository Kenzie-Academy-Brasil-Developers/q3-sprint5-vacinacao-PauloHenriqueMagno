from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import String, DateTime, Column
from datetime import datetime, timedelta

@dataclass
class Vaccination(db.Model):
  __tablename__ = "vaccine_cards"

  first_shot = datetime.now()
  second_shot = first_shot + timedelta(days = 90)

  cpf: str = Column(String(11), primary_key = True)
  name: str = Column(String, nullable = False)
  first_shot_date: str = Column(DateTime, default = first_shot)
  second_shot_date: str = Column(DateTime, default = second_shot)
  vaccine_name: str = Column(String, nullable = False)
  health_unit_name: str = Column(String, nullable = False)