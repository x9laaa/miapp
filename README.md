# 📨 miapp - Aplicación Flask con SQLite

Esta es una aplicación Flask sencilla que permite registrar mensajes (nombre, asunto, cuerpo y fecha) y visualizarlos en una segunda página. Usa SQLite como base de datos local.

---

## 📦 Requisitos

- Python 3.8 o superior
- Git (para clonar el repositorio)

---

## ⚙️ Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/x9laaa/miapp.git
cd miapp


2. **Crea y activa un entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate

1. **Instala las dependencias**
```bash
pip install -r requirements.txt

1. **Ejecutar la aplicación en modo producción local (con Gunicorn)**
```bash
gunicorn -w 4 -b 127.0.0.1:8000 app:app