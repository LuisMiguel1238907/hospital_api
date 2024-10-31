from pydantic import BaseModel
from typing import List, Optional

class PacienteBase(BaseModel):
    nombre: str
    edad: int
    diagnostico: str
    requiere_seguimiento: Optional[bool] = False

class PacienteCreate(PacienteBase):
    pass

class PacienteResponse(PacienteBase):
    id: int
    tratamientos: List[str] = []

    class Config:
        orm_mode = True

class TratamientoBase(BaseModel):
    nombre: str
    duracion: int
    paciente_id: int

class TratamientoCreate(TratamientoBase):
    pass

class TratamientoResponse(TratamientoBase):
    id: int

    class Config:
        orm_mode = True
