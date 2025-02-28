from flask import request, render_template, Blueprint
import requests

FASTAPI_ENVIAR_PALESTRA = "http://127.0.0.1:8000/palestra/"

criar_palestra_bp = Blueprint('criar_palestra', __name__)

@criar_palestra_bp.route('/criar_palestra', methods=['GET', 'POST'])
def criar_palestra():
    if request.method == 'POST':
            data = {
                'nome_palestra': request.form['nome_palestra'],
                'palestrante': request.form['palestrante'],
                'tema': request.form['tema']
            }
            
            response = requests.post(FASTAPI_ENVIAR_PALESTRA, json=data)

            if response.status_code == 200:
                return render_template('criar_palestra.html', status='sucesso')
            else:
                return render_template('criar_palestra.html', status='erro')
        
    return render_template('criar_palestra.html')