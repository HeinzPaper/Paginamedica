# create_db.py

import sqlite3

def create_db():
    conn = sqlite3.connect('database/medical.db')
    cursor = conn.cursor()
    
    # Crear tabla de enfermedades
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # Crear tabla de medicamentos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        uses TEXT,
        possible_allergies TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
