from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#COnection String:
#Representa la base de datos al conectarse depende de la base de datos que se use y el lenguaje de programacion
SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:admin@localhost:3315/py-shopy'

#Crear el objeto de conexion
conn = create_engine(SQLALCHEMY_DATABASE_URL)

#la clase base pra los modelos
Base = declarative_base()