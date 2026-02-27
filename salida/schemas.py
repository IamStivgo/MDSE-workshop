# ==========================================================
# SCHEMAS PYDANTIC — GENERADOS AUTOMÁTICAMENTE
# Fuente: psm_fastapi.api  |  NO EDITAR
# ==========================================================

from pydantic import BaseModel
from datetime import datetime


class Producto(BaseModel):
    id            : float
    nombre        : str
    precio        : float
    stock         : float
    disponible    : bool

    class Config:
        json_schema_extra = {
            "example": {
                "id": 0.0,
                "nombre": "Laptop Pro",
                "precio": 999.99,
                "stock": 42,
                "disponible": True,
            }
        }


class Direccion(BaseModel):
    id            : float
    ciudad        : str
    departamento  : str
    nombre        : str
    descripcion   : str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 0.0,
                "ciudad": "ciudad ejemplo",
                "departamento": "departamento ejemplo",
                "nombre": "Laptop Pro",
                "descripcion": "descripcion ejemplo",
            }
        }


class Cliente(BaseModel):
    id            : float
    nombre        : str
    email         : str
    edad          : float
    id_direccion  : float

    class Config:
        json_schema_extra = {
            "example": {
                "id": 0.0,
                "nombre": "Laptop Pro",
                "email": "usuario@ejemplo.com",
                "edad": 30,
                "id_direccion": 0.0,
            }
        }


class Pedido(BaseModel):
    id            : float
    numero        : float
    total         : float
    estado        : str
    fecha         : datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": 0.0,
                "numero": 1001,
                "total": 150.00,
                "estado": "pendiente",
                "fecha": "2024-01-15",
            }
        }


class Factura(BaseModel):
    id_cliente    : float
    id_producto   : float
    id_pedido     : float

    class Config:
        json_schema_extra = {
            "example": {
                "id_cliente": 0.0,
                "id_producto": 0.0,
                "id_pedido": 0.0,
            }
        }

