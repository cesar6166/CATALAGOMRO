import sqlite3
import pandas as pd

# Obtener conexión a la base de datos
def get_connection():
    conn = sqlite3.connect("Items.db", check_same_thread=False)
    return conn

# Crear tabla si no existe
def crear_tablas(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS item (
        ID TEXT PRIMARY KEY,
        Descripcion TEXT NOT NULL
    )
""")


    conn.commit()
    
def importar_items_desde_excel(conn, ruta_excel):
    df = pd.read_excel(ruta_excel)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        id_item = str(row.get("ID")).strip()
        descripcion = str(row.get("Descripcion")).strip()
        if id_item and descripcion:
            cursor.execute("INSERT OR IGNORE INTO item (ID, Descripcion) VALUES (?, ?)", (id_item, descripcion))

    conn.commit()


