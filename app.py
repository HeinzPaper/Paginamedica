# app.py

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def search_diseases(query):
    conn = sqlite3.connect('database/medical.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM diseases WHERE name LIKE ? OR description LIKE ?
    ''', ('%' + query + '%', '%' + query + '%'))
    results = cursor.fetchall()
    conn.close()
    return results

def search_medicines(query):
    conn = sqlite3.connect('database/medical.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM medicines WHERE name LIKE ? OR uses LIKE ?
    ''', ('%' + query + '%', '%' + query + '%'))
    results = cursor.fetchall()
    conn.close()
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    disease_results = search_diseases(query)
    medicine_results = search_medicines(query)
    return render_template('search_results.html', 
                           disease_results=disease_results, 
                           medicine_results=medicine_results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
