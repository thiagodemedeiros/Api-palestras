import requests
from flask import render_template, Blueprint

listar_palestras_bp = Blueprint('listar_palestras', __name__)

URL_LISTA_PALESTRAS = "http://127.0.0.1:8000/listar_palestras"

@listar_palestras_bp.route('/palestras')
def listar_palestras():
    response = requests.get(URL_LISTA_PALESTRAS)

    if response.status_code == 200:
        palestras = response.json()
    else:
        palestras = []
    
    return render_template('listar_palestras.html', palestras=palestras)