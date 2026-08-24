from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Telemetry(Base):

    __tablename__ = "telemetry"

    id = Column(Integer, primary_key=True)

    battery = Column(Float)

    temperature = Column(Float)

    fuel = Column(Float)

    signal = Column(Float)