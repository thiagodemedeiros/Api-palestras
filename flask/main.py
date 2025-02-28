from flask import Flask
from routes.criar_palestra import criar_palestra_bp
from routes.home import home_bp

app = Flask(__name__)

app.register_blueprint(criar_palestra_bp)

app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)
