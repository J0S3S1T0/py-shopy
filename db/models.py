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
    

class asesoria(Base):
    __tablename__="asesoria"
    id = Column(Integer,
                        primary_key=True)
    fechaAsesoria = Column(Date)
    horaAsesoria =Column(Date)
    estadoAsesoria =Column(String(60))


class asesor(Base):
    __tablename__="asesor"
    id = Column(Integer,
                        primary_key=True)
    nombreAsesor = Column(String(60))
    apellidoAsesor =Column(String(60))
    correoAsesor =Column(String(60))
    telefonoAsesor =Column(Integer)
    documentoAsesor =Column(Integer)


class usuario(Base):
    __tablename__="usuario"
    id = Column(Integer,
                        primary_key=True)
    nombre = Column(String(60))
    contraseña =Column(String(60))
    telefono =Column(Integer)
    documento =Column(Integer)
    edad =Column(Integer)
    correo =Column(String(60))


class servicio(Base):
    __tablename__="servicio"
    id = Column(Integer,
                        primary_key=True)
    descripcion = Column(String(60))
    estadoServicio =Column(String(60))


class rol(Base):
    __tablename__="rol"
    id = Column(Integer,
                        primary_key=True)
    nombreRol = Column(String(60))
    estadoRol =Column(String(60))
    descripcion =Column(String(60))
    correo =Column(String(60))


