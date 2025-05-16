from .database import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship


class categoria(Base):
    __tablename__= "categoria"
    id = Column(Integer,
                primary_key=True)
    estado=Column(String(45))
    nombre = Column(String(60))
    #Relacion
    modelos = relationship("Modelos",
                        back_populates="categoria")


class modelos(Base):
    __tablename__="modelos"
    id = Column(Integer,
                        primary_key=True)
    referencia = Column(String(60))
    marca =Column(String(60))
    fechaLanzamiento= Column(Date)
    
    #calve forane

    categoria_id=Column(Integer,
                        ForeignKey("categoria.id"))
    