from sqlalchemy.sql.elements import False_
from sqlalchemy.sql.expression import true
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Sequence

TABLE_ID = Sequence('table_id_seq', start=1)

class Usuario(Base):
    __tablename__='Usuario'
    id=Column(Integer,TABLE_ID, primary_key=True, server_default=TABLE_ID.next_value())
    nombre=Column(String(336), nullable=False)
    email=Column(String(336), nullable=False, unique=True)
    asociado=Column(Boolean, default=False)
    