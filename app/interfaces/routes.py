from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.infrastructure.database import get_db
from app.schemas import PacienteCreate, PacienteResponse, TratamientoCreate, TratamientoResponse
from app.use_cases.paciente_use_cases import (
    crear_paciente, 
    listar_pacientes, 
    obtener_paciente as obtener_paciente_db,  # Renombrar aquí para evitar confusión
    buscar_pacientes_por_diagnostico, 
    pacientes_seguimiento
)
from app.use_cases.tratamiento_use_cases import (
    crear_tratamiento, 
    listar_tratamientos, 
    promedio_duracion_tratamientos
)

router = APIRouter()

@router.post("/pacientes", response_model=PacienteResponse)
def agregar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    return crear_paciente(db, paciente)

@router.get("/pacientes", response_model=List[PacienteResponse])
def obtener_pacientes(db: Session = Depends(get_db)):
    return listar_pacientes(db)

@router.get("/pacientes/{paciente_id}", response_model=PacienteResponse)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = obtener_paciente_db(db, paciente_id)  # Usar la función renombrada
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.get("/pacientes/buscar", response_model=List[PacienteResponse])
def buscar_pacientes(diagnostico: str, db: Session = Depends(get_db)):
    return buscar_pacientes_por_diagnostico(db, diagnostico)

@router.post("/tratamientos", response_model=TratamientoResponse)
def agregar_tratamiento(tratamiento: TratamientoCreate, db: Session = Depends(get_db)):
    return crear_tratamiento(db, tratamiento)

@router.get("/tratamientos", response_model=List[TratamientoResponse])
def obtener_tratamientos(db: Session = Depends(get_db)):
    return listar_tratamientos(db)

@router.get("/tratamientos/promedio_duracion")
def promedio_duracion(db: Session = Depends(get_db)):
    promedio = promedio_duracion_tratamientos(db)
    return {"promedio_duracion": promedio}

@router.get("/pacientes/seguimiento", response_model=List[PacienteResponse])
def pacientes_seguimiento_api(db: Session = Depends(get_db)):
    return pacientes_seguimiento(db)

