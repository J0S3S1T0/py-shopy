from .database import Base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship

class categoria(Base):
    __tablename__ = "categoria"

    idCategoria = Column(Integer, primary_key=True)
    estadoCategoria = Column(String(45))
    nombreCategoria = Column(String(60))

    # Relación con modelos
    modelosCategoria = relationship("modelo", back_populates="categoriaModelo")

class modelo(Base):
    __tablename__ = "modelo"

    idModelo = Column(Integer, primary_key=True)
    referenciaModelo = Column(String(60))
    marcaModelo = Column(String(60))
    fechaLanzamientoModelo = Column(Date)

    # Llave foránea con la tabla categoria y el atributo id
    categoriaIdModelo = Column(Integer, ForeignKey("categoria.idCategoria"))

    # Relación con categoria
    categoriaModelo = relationship("categoria", back_populates="modelosCategoria")

class asesoria(Base):
    __tablename__ = "asesoria"

    idAsesoria = Column(Integer, primary_key=True)
    fechaSolicitudAsesoria = Column(Date)
    estadoAsesoria = Column(String(50))  
    necesidadAsesoria = Column(String(500))
    afinacionMayor = Column(String(400))
    mantenimientoCorrectivo = Column(String(400))
    mantenimientoPreventivo = Column(String(400))
    modificaciones = Column(String(400))

    # Llaves foráneas con id usuario, asesor y tipo de asesoría
    usuarioIdAsesoria = Column(Integer, ForeignKey("usuario.idUsuario"))
    asesorIdAsesoria = Column(Integer, ForeignKey("asesor.idAsesor"))
    tipoAsesoriaIdAsesoria = Column(Integer, ForeignKey("tipoAsesoria.idTipoAsesoria"))

    # Relaciones con Usuario, asesor y tipo de asesoría
    usuarioAsesoria = relationship("usuario", back_populates="asesoriasUsuario")
    asesorAsesoria = relationship("asesor", back_populates="asesoriasAsesor")
    tipoAsesoriaAsesoria = relationship("tipoAsesoria", back_populates="asesoriasTipoAsesoria")

    # Relación con servicio
    serviciosAsesoria = relationship("servicio", back_populates="asesoriaServicio")

class servicio(Base):
    __tablename__ = "servicio"

    idServicio = Column(Integer, primary_key=True)
    fechaSolicitudServicio = Column(Date)
    estadoServicio = Column(String(50))  
    necesidadServicio = Column(String(500))
    afinacionMayor = Column(String(400))
    mantenimientoCorrectivo = Column(String(400))
    mantenimientoPreventivo = Column(String(400))
    modificaciones = Column(String(400))

    # Llave foránea con id asesorías
    asesoriaIdServicio = Column(Integer, ForeignKey("asesoria.idAsesoria"))

    # Relación con asesoría
    asesoriaServicio = relationship("asesoria", back_populates="serviciosAsesoria")
    servicioMecanico = relationship("mecanico", back_populates="servicioMecanico")

class asesor(Base):
    __tablename__ = "asesor"

    idAsesor = Column(Integer, primary_key=True)
    nombreAsesor = Column(String(60))
    apellidoAsesor = Column(String(60))
    correoAsesor = Column(String(60))
    telefonoAsesor = Column(Integer)
    documentoAsesor = Column(Integer)

    # Relación con asesorías
    asesoriasAsesor = relationship("asesoria", back_populates="asesorAsesoria")

class historialAsesoria(Base):
    __tablename__ = "historialAsesoria"

    idHistorialAsesoria = Column(Integer, primary_key=True)
    comentariosHistorialAsesoria = Column(String(500))
    fechaRegistroHistorialAsesoria = Column(Date)

    # Llave foránea con asesorías
    asesoriaIdHistorialAsesoria = Column(Integer, ForeignKey("asesoria.idAsesoria"))
    
    # Relación con asesorías
    asesoriaHistorialAsesoria = relationship("asesoria", back_populates="historialAsesoria")

class tipoAsesoria(Base):
    __tablename__ = "tipoAsesoria"

    idTipoAsesoria = Column(Integer, primary_key=True)
    nombreTipoAsesoria = Column(String(50))
    descripcionTipoAsesoria = Column(String(200))

    # Relación con asesorías
    asesoriasTipoAsesoria = relationship("asesoria", back_populates="tipoAsesoriaAsesoria")

class usuario(Base):
    __tablename__ = "usuario"

    idUsuario = Column(Integer, primary_key=True)
    nombreUsuario = Column(String(60))
    contraseñaUsuario = Column(String(60))
    telefonoUsuario = Column(Integer)
    documentoUsuario = Column(Integer)
    edadUsuario = Column(Integer)
    correoUsuario = Column(String(60))

    # Llave foránea con id rol
    rolIdUsuario = Column(Integer, ForeignKey("rol.idRol"))

    # Relaciones con asesorías, blogs y roles
    asesoriasUsuario = relationship("asesoria", back_populates="usuarioAsesoria")
    blogsUsuario = relationship("blogExperiencia", back_populates="usuarioBlog")
    rolUsuario = relationship("rol", back_populates="usuariosRol")

class galeriaVehiculoModificado(Base):
    __tablename__ = "galeriaVehiculoModificado"

    idGaleriaVehiculoModificado = Column(Integer, primary_key=True)
    nombreVehiculoGaleriaVehiculoModificado = Column(String(100))
    descripcionGaleriaVehiculoModificado = Column(String(100))

    # Llaves foráneas con usuario y vehículo
    usuarioIdGaleriaVehiculoModificado = Column(Integer, ForeignKey("usuario.idUsuario"))
    vehiculoIdGaleriaVehiculoModificado = Column(Integer, ForeignKey("vehiculo.idVehiculo"))

    # Relaciones con usuario y vehículo
    usuarioGaleriaVehiculoModificado = relationship("usuario", back_populates="galeriaUsuario")
    vehiculoGaleriaVehiculoModificado = relationship("vehiculo", back_populates="galeriaVehiculo")

class accesorio(Base):
    __tablename__ = "accesorio"

    idAccesorio = Column(Integer, primary_key=True)
    nombreAccesorio = Column(String(100))
    descripcionAccesorio = Column(String(50))
    precioAccesorio = Column(DECIMAL(10,2))

    # Llave foránea con el idVehiculos
    vehiculoIdAccesorio = Column(Integer, ForeignKey("vehiculo.idVehiculo"))

    # Relación con vehículos
    vehiculoAccesorio = relationship("vehiculo", back_populates="accesoriosVehiculo")

class rol(Base):
    __tablename__ = "rol"

    idRol = Column(Integer, primary_key=True)
    nombreRol = Column(String(60))
    estadoRol = Column(String(60))
    descripcionRol = Column(String(60))

    # Relación con usuarios
    usuariosRol = relationship("usuario", back_populates="rolUsuario")

class vehiculo(Base):
    __tablename__ = "vehiculo"

    idVehiculo = Column(Integer, primary_key=True)
    marcaVehiculo = Column(String(50))
    modeloVehiculo = Column(String(50))
    añoVehiculo = Column(Integer)
    tipoVehiculo = Column(String(50))
    descripcionTecnicaVehiculo = Column(String(50))
    motor = Column(String(50))
    potencia = Column(String(50))
    Velocidad = Column(String(50))
    Transmision = Column(String(50))
    numerosCilindros = Column(String(50))
    cilindradas = Column(String(50))
    velocidadMaxima = Column(String(50))
    calibre = Column(String(50))
    potenciaMaxima = Column(String(50))


    # Llaves foráneas con modelos y marcas
    modeloIdVehiculo = Column(Integer, ForeignKey("modelo.idModelo"))

    # Relaciones con modelo, marca y accesorios
    modeloVehiculo = relationship("modelo", back_populates="vehiculosModelo")
    accesoriosVehiculo = relationship("accesorio", back_populates="vehiculoAccesorio")

class mecanico(Base):
    __tablename__ = "mecanico"

    idMecanico = Column(Integer, primary_key=True)
    nombreMecanico = Column(String(60))
    apellidoMecanico = Column(String(60))
    correoMecanico = Column(String(60))
    telefonoMecanico = Column(Integer)
    documentoMecanico = Column(Integer)
    

    # Relación con asesorías
    servicioMecanico = relationship("servicio", back_populates="servicioMecanico")
    diagnosticoMecanico = relationship("diagnosticos", back_populates="diagnosticoMecanico")

class diagnosticos(Base):
    __tablename__ = "diagnosticos"

    idDiagnosticos = Column(Integer, primary_key=True)
    historialDiagnosticos = Column(String(60))

    # Relación con asesorías
    servicioMecanico = relationship("servicio", back_populates="servicioMecanico")

    #Llave foranea
    diagnosticoVehiculo = Column(Integer, ForeignKey("vehiculo.idVehiculo"))
    diagnosticomecanico = Column(Integer, ForeignKey("mecanico.idMecanico"))

