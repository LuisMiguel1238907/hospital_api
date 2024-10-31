from sqlalchemy.orm import Session
from app.domain.models import Paciente, Tratamiento
from app.schemas import PacienteCreate
from typing import List

def crear_paciente(db: Session, paciente: PacienteCreate) -> Paciente:
    db_paciente = Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def listar_pacientes(db: Session) -> List[Paciente]:
    return db.query(Paciente).all()

def obtener_paciente(db: Session, paciente_id: int) -> Paciente:
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def buscar_pacientes_por_diagnostico(db: Session, diagnostico: str) -> List[Paciente]:
    return db.query(Paciente).filter(Paciente.diagnostico == diagnostico).all()

def pacientes_seguimiento(db: Session) -> List[Paciente]:
    return db.query(Paciente).filter(Paciente.requiere_seguimiento == True).all()
