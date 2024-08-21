# populate_db.py

import sqlite3

def populate_db():
    conn = sqlite3.connect('database/medical.db')
    cursor = conn.cursor()
    
    # Lista de medicamentos comunes con posibles alergias
    medicines = [
        ('Paracetamol', 'Alivio de fiebre y dolor.', 'Posible reacción alérgica: erupciones cutáneas, urticaria.'),
        # ... (incluye todos los medicamentos listados anteriormente)
        ('Clotrimazole', 'Antifúngico utilizado para tratar infecciones por hongos.', 'Posible reacción alérgica: erupciones cutáneas, picazón.'),
        ('Itraconazole', 'Antifúngico utilizado para tratar infecciones por hongos.', 'Posible reacción alérgica: erupciones cutáneas, dolor abdominal.'),
    ]
    
    cursor.executemany('''
    INSERT INTO medicines (name, uses, possible_allergies) VALUES (?, ?, ?)
    ''', medicines)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_db()
