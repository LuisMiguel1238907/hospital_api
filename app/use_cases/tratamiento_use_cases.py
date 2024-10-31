from sqlalchemy.orm import Session
from app.domain.models import Tratamiento
from app.schemas import TratamientoCreate
from typing import List
from sqlalchemy import func

def crear_tratamiento(db: Session, tratamiento: TratamientoCreate) -> Tratamiento:
    db_tratamiento = Tratamiento(**tratamiento.dict())
    db.add(db_tratamiento)
    db.commit()
    db.refresh(db_tratamiento)
    return db_tratamiento

def listar_tratamientos(db: Session) -> List[Tratamiento]:
    return db.query(Tratamiento).all()

def promedio_duracion_tratamientos(db: Session) -> float:
    return db.query(func.avg(Tratamiento.duracion)).scalar()
