from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'messages.db'

# Crear la tabla si no existe
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            asunto TEXT NOT NULL,
            cuerpo TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        asunto = request.form['asunto']
        cuerpo = request.form['cuerpo']
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mensajes (nombre, asunto, cuerpo, fecha) VALUES (?, ?, ?, ?)',
                       (nombre, asunto, cuerpo, fecha))
        conn.commit()
        conn.close()
        return redirect('/')
    
    return render_template('index.html')

@app.route('/mensajes')
def ver_mensajes():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, asunto, cuerpo, fecha FROM mensajes ORDER BY fecha DESC')
    mensajes = cursor.fetchall()
    conn.close()
    return render_template('mensajes.html', mensajes=mensajes)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
