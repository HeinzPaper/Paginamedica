from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para buscar enfermedades usando la API de Disease.sh
@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('query')
    url = f"https://disease.sh/v3/covid-19/jhucsse/counties/{query}"  # Ejemplo con COVID-19
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        resultados = data if data else []  # Asegura que resultados sea una lista vacía si no hay datos
    else:
        resultados = []

    return render_template('resultados.html', resultados=resultados, tipo='Enfermedad')

# Ruta para buscar medicamentos usando la API de OpenFDA
@app.route('/buscar_medicamento', methods=['GET'])
def buscar_medicamento():
    query = request.args.get('query')
    url = f"https://api.fda.gov/drug/label.json?search={query}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        medicamentos = data['results'] if 'results' in data else []
    else:
        medicamentos = []

    return render_template('resultados.html', resultados=medicamentos, tipo='Medicamento')

if __name__ == '__main__':
    app.run(debug=True
    
    
    @app.route('/enfermedades')
def enfermedades():
    conn = get_db_connection()
    enfermedades = conn.execute('SELECT * FROM enfermedades').fetchall()
    conn.close()
    return render_template('enfermedades.html', enfermedades=enfermedades)

@app.route('/medicamentos')
def medicamentos():
    conn = get_db_connection()
    medicamentos = conn.execute('SELECT * FROM medicamentos').fetchall()
    conn.close()
    return render_template('medicamentos.html', medicamentos=medicamentos)

