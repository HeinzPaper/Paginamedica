import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS enfermedades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL
)
''')

# Insertar datos de ejemplo
cursor.execute('INSERT INTO enfermedades (nombre, descripcion) VALUES (?, ?)',
               ('Gripe', 'Infección viral común que causa fiebre, tos y dolor de garganta.'))
cursor.execute('INSERT INTO medicamentos (nombre, descripcion) VALUES (?, ?)',
               ('Ibuprofeno', 'Medicamento antiinflamatorio utilizado para reducir el dolor y la fiebre.'))

connection.commit()
connection.close()
