import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Sociedad
from models import Sociedad as ModelSociedad
from models import Ubicacion
from models import Ubicacion as ModelUbicacion
from models import Empleado
from models import Empleado as ModelEmpleado
from models import DataPersonal
from models import DataPersonal as ModelDataPersonal

from schema import Sociedad as SchemaSociedad
from schema import Empleado as SchemaEmpleado
from schema import Ubicacion as SchemaUbicacion
from schema import DataPersonal as SchemaDataPersonal

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/add-empleado/", response_model=SchemaEmpleado)
def add_empleado(empleado: SchemaEmpleado):
    db_empleado = ModelEmpleado(nombre=empleado.nombre, apellido=empleado.apellido, sociedad_id=empleado.sociedad_id, ubicacion_id=empleado.ubicacion_id)
    db.session.add(db_empleado)
    db.session.commit()
    return db_empleado

@app.delete("/delete-empleado/{id}")
def delete_empleado(id : int):
    empleado = db.session.query(Empleado).get(id)
    db.session.delete(empleado)
    db.session.commit()
    return "Empleado borrado"

@app.patch("/update-empleado/{id}")
def update_empleado(id : int, empleado_data: SchemaEmpleado):
    db_empleado = db.session.query(Empleado).get(id)
    data  = empleado_data.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_empleado, key, value)
    db.session.add(db_empleado)
    db.session.commit()
    
    return "Empleado actualizado"

@app.post("/add-sociedad/", response_model=SchemaSociedad)
def add_sociedad(sociedad: SchemaSociedad):
    db_sociedad = ModelSociedad(descripcion=sociedad.descripcion)
    db.session.add(db_sociedad)
    db.session.commit()
    return db_sociedad

@app.delete("/delete-Sociedad/{id}")
def delete_Sociedad(id : int):
    Sociedad = db.session.query(Sociedad).get(id)
    db.session.delete(Sociedad)
    db.session.commit()
    return "Sociedad borrada"

@app.patch("/update-sociedad/{id}")
def update_sociedad(id : int, sociedad_data: SchemaSociedad):
    db_sociedad = db.session.query(Sociedad).get(id)
    data  = sociedad_data.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_sociedad, key, value)
    db.session.add(db_sociedad)
    db.session.commit()
    
    return "Sociedad actualizada"

@app.post("/add-ubicacion/", response_model=SchemaUbicacion)
def add_ubicacion(ubicacion: SchemaUbicacion):
    db_ubicacion = ModelUbicacion(descripcion=ubicacion.descripcion)
    db.session.add(db_ubicacion)
    db.session.commit()
    return db_ubicacion

@app.patch("/update-ubicacion/{id}")
def update_ubicacion(id : int, ubicacion_data: SchemaUbicacion):
    db_ubicacion = db.session.query(Ubicacion).get(id)
    data  = ubicacion_data.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_ubicacion, key, value)
    db.session.add(db_ubicacion)
    db.session.commit()
    
    return "Ubicacion actualizada"

@app.delete("/delete-Ubicacion/{id}")
def delete_ubicacion(id : int):
    Ubicacion = db.session.query(Ubicacion).get(id)
    db.session.delete(Ubicacion)
    db.session.commit()
    return "Ubicacion borrada"

@app.patch("/update-sociedad/{id}")
def update_sociedad(id : int, sociedad_data: SchemaSociedad):
    db_sociedad = db.session.query(Sociedad).get(id)
    data  = sociedad_data.dict(exclude_unset=True)
    for key, value in data.items():
        setattr(db_sociedad, key, value)
    db.session.add(db_sociedad)
    db.session.commit()
    
    return "Sociedad actualizada"


@app.post("/add-personal-data/", response_model=SchemaDataPersonal)
def add_ubicacion(data: SchemaDataPersonal):
    db_personal_data = ModelDataPersonal(direccion=data.direccion, cuenta=data.cuenta, telefono=data.telefono, num_emp=data.num_emp)
    db.session.add(db_personal_data)
    db.session.commit()
    return db_personal_data


@app.get("/empleados/")
def get_empleados():
    empleados = db.session.query(Empleado).all()

    return empleados

@app.get("/empleado/{id}")
def get_empleados(id : int):
    empleados = db.session.query(Empleado).get(id)

    return empleados

@app.get("/sociedades/")
def get_sociedades():
    sociedades = db.session.query(Sociedad).all()

    return sociedades

@app.get("/sociedad/{id}")
def get_sociedad(id : int):
    sociedad = db.session.query(Sociedad).get(id)

    return sociedad

@app.get("/ubicaciones/")
def get_ubicaciones():
    ubicaciones = db.session.query(Ubicacion).all()

    return ubicaciones

@app.get("/ubicacion/{id}")
def get_ubicacion(id : int):
    ubicacion = db.session.query(Ubicacion).get(id)

    return ubicacion


# @app.post("/user/", response_model=SchemaUser)
# def create_user(user: SchemaUser):
#     db_user = ModelUser(
#         first_name=user.first_name, last_name=user.last_name, age=user.age
#     )
#     db.session.add(db_user)
#     db.session.commit()
#     return db_user


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
