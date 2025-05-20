# local_webapp.py
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder="webapp")

@app.route('/')
def index():
    return send_from_directory('webapp', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('webapp', filename)

def run_flask_app():
    print("Локальный сервер игры запущен на http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
