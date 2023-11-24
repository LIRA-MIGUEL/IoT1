import fastapi
import sqlite3
from pydantic import BaseModel
# Importamos CORS para el acceso
# from fastapi.middleware.cors import CORSMiddleware


# Crea la base de datos
conn = sqlite3.connect("sql/dispositivos.db")

app = fastapi.FastAPI()

""" # Permitimos los origenes para conectarse
origins = [
    "http://0.0.0.0:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://herokufrontendsql-8c522739b4c3.herokuapp.com",
    "https://herokuflaskfront-60829f087760.herokuapp.com"
]

# Agregamos las opciones de origenes, credenciales, métodos y headers
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

 """
class Dispositivo(BaseModel):
    valor : str


@app.get("/")
def inicio():
    return {'Developer by':'Patricio Vargas f:', "IoT Proyect": ":3"}

# Rutas para las operaciones
@app.get("/dispositivos")
async def obtener_dispositivos():
    """Obtiene todos los dispositivos."""
    # TODO Consulta todos los contactos de la base de datos y los envia en un JSON
    c = conn.cursor()
    c.execute('SELECT * FROM dispositivos;')
    response = []
    for row in c:
        dispositivo = {"id":row[0],"dispositivo":row[1], "valor":row[2]}
        response.append(dispositivo)
    return response


@app.get("/dispositivos/{id}")
async def obtener_dispositivo(id: str):
    """Obtiene un contacto por su email."""
    # Consulta el contacto por su email
    c = conn.cursor()
    c.execute('SELECT * FROM dispositivos WHERE id = ?', (id))
    dispositivo = None
    for row in c:
        dispositivo = {"id":row[0],"dispositivo":row[1],"valor":row[2]}
    return dispositivo


@app.put("/disposiivos/{id}")
async def actualizar_dispositivo(id: str, Dispositivo: Dispositivo):
    """Actualiza un contacto."""
    c = conn.cursor()
    c.execute('UPDATE dispositivos SET valor = ? WHERE id = ?',
              (Dispositivo.valor, id))
    conn.commit()
    return Dispositivo
