from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv
from database import SessionLocal
import models


# Setting env variables
load_dotenv()

app = FastAPI()

class Usuario(BaseModel): #serializer  
    id:int
    nombre:str
    email:str
    asociado:bool
    
    class Config:
        orm_mode=True
        
class UsuarioPost(BaseModel): #serializer  
    nombre:str
    email:str
    asociado:bool
    
    class Config:
        orm_mode=True
        
db=SessionLocal()

@app.get('/')
def index():
    return {"message" : "API implementada con FastAPI :D"}

@app.get('/users', response_model=List[Usuario], status_code=200)
def getAllUsers():
    items=db.query(models.Usuario).all()
    return items

@app.get('/users/{id}')
def getUser(id:int):
    user=db.query(models.Usuario).filter(models.Usuario.id==id).first()
    return user

@app.put('/users/{id}', response_model=Usuario, status_code=200)
def updateUser(id:int, user:UsuarioPost):
    user_to_update=db.query(models.Usuario).filter(models.Usuario.id==id).first()
    
    check_mail=db.query(models.Usuario).filter(models.Usuario.email==user.email).first()
    if check_mail is not None:
        raise HTTPException(status_code=400,detail="Ya hay un usuario registrado con ese email :(")
    
    user_to_update.nombre=user.nombre
    user_to_update.email=user.email
    user_to_update.description=user.asociado

    db.commit()

    return user_to_update

@app.post('/users', response_model=Usuario, status_code=201)
def createtUser(user:UsuarioPost):
    new_user=models.Usuario(
        nombre=user.nombre,
        email=user.email,
        asociado=user.asociado
    )
    
    check_mail=db.query(models.Usuario).filter(models.Usuario.email==user.email).first()
    if check_mail is not None:
        raise HTTPException(status_code=400,detail="Ya hay un usuario registrado con ese email :(")

    db.add(new_user)
    db.commit()
    return new_user

@app.delete('/users/{id}', status_code=200)
def deleteUser(id:int):
    user_to_delete=db.query(models.Usuario).filter(models.Usuario.id==id).first()

    if user_to_delete is None:
        raise HTTPException(status_code=404,detail="Usuario no encontrado :/")
    
    db.delete(user_to_delete)
    db.commit()

    return 'Usuario borrado exitosamente :P'