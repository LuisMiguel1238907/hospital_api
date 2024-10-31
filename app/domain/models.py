from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    edad = Column(Integer)
    diagnostico = Column(String)
    requiere_seguimiento = Column(Boolean, default=False)

class Tratamiento(Base):
    __tablename__ = 'tratamientos'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    duracion = Column(Integer)  # Duración en días
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    
    paciente = relationship("Paciente", back_populates="tratamientos")

Paciente.tratamientos = relationship("Tratamiento", order_by=Tratamiento.id, back_populates="paciente")
