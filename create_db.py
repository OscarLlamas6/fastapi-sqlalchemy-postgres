from database import Base, engine
from models import Usuario

print("Creating database... ")

Base.metadata.create_all(engine)