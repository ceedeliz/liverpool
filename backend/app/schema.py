from pydantic import BaseModel

class Sociedad(BaseModel):
    descripcion: str

    class Config:
        orm_mode = True

class Ubicacion(BaseModel):
    descripcion: str
    

    class Config:
        orm_mode = True

class Empleado(BaseModel):
    nombre: str
    apellido: str
    ubicacion_id: int
    sociedad_id: int

    class Config:
        orm_mode = True

class DataPersonal(BaseModel):
    direccion: str
    cuenta: str
    telefono: str
    num_emp: str
    class Config:
        orm_mode = True
