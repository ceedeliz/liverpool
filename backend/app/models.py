from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Sociedad(Base):
    __tablename__ = "sociedad"
    id_sociedad = Column(Integer, primary_key=True)
    descripcion = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Ubicacion(Base):
    __tablename__ = "ubicacion"
    id_ubicacion = Column(Integer, primary_key=True)
    descripcion = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

class Empleado(Base):
    __tablename__ = "empleado"
    num_emp = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    sociedad_id = Column(Integer, ForeignKey("sociedad.id_sociedad"))
    ubicacion_id = Column(Integer, ForeignKey("ubicacion.id_ubicacion"))

    sociedad = relationship("Sociedad")
    ubicacion = relationship("Ubicacion")

class DataPersonal(Base):
    __tablename__ = "data_personal"
    id = Column(Integer, primary_key=True)
    direccion = Column(String)
    cuenta = Column(String)
    telefono = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    num_emp = Column(Integer, ForeignKey("empleado.num_emp"))

    empleado = relationship("Empleado")
