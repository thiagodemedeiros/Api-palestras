from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

banco_palestras = 'palestras.json'

class Palestra(BaseModel):
    nome_palestra: str
    palestrante: str
    tema: str

def carregar_palestras():
    if os.path.exists(banco_palestras):
        with open(banco_palestras, 'r') as palestras:
            try:
                return json.load(palestras)
            except json.JSONDecodeError:
                return []
    return []

def salvar_palestras(palestras):
    with open(banco_palestras, 'w') as palestra:
        json.dump(palestras, palestra, indent=4)

@app.post('/palestra')
async def criar_palestra(palestra: Palestra):
    palestras = carregar_palestras()
    novo_id_palestra = len(palestras)
    
    nova_palestra = {
        'id' : novo_id_palestra,
        'nome_palestra' : palestra.nome_palestra,
        "palestrante": palestra.palestrante,
        "tema": palestra.tema
    }
    
    palestras.append(nova_palestra)
    salvar_palestras(palestras)
    return {
        'status' : 'Sucesso',
        'mensagem': 'Palestra criada com sucesso'
    }

@app.get('/listar_palestras')
async def listar_palestras():
    palestras = carregar_palestras()
    return palestras