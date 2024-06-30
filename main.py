from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

config = {
    "host": "127.0.0.1",
    "port": "3306",
    "user": "root",
    "database": "prenotazione"
}

class  prenotazione(BaseModel):
    nome_prenotazione: str
    numero_di_telefono: int
    numero_di_persone: int
    giorno: str
    orario: str
    messaggio: str

@app.post('/book_table')
def prenotazione(user : prenotazione):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO booking (Nome, Numero_di_Telefono, Persone, Giorno, Orario, Messaggio) VALUES ('{user.Nome}', {user.Numero_di_Telefono},{user.Persone},'{user.Giorno}', '{user.Orario}', '{user.Messaggio}')")

    conn.commit()
    conn.close()
    return{
        "msg":"Tavolo prenotato con successo"
    }