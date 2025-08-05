import sqlite3
import pandas as pd

def get_connection():
    conn = sqlite3.connect("Items.db", check_same_thread=False)
    return conn

def crear_tabla_racks(conn):
    cursor = conn.cursor()
    
    # Tabla de racks
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS racks (
            Nombre TEXT PRIMARY KEY
        )
    """)
    
    # Tabla de asignación de ítems a posiciones dentro de racks
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rack_items (
            Rack TEXT NOT NULL,
            Posicion TEXT NOT NULL,
            ItemID TEXT NOT NULL,
            FOREIGN KEY (Rack) REFERENCES racks(Nombre),
            FOREIGN KEY (ItemID) REFERENCES item(ID)
        )
    """)
    
    conn.commit()

def crear_rack(conn, nombre_rack):
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO racks (Nombre) VALUES (?)", (nombre_rack,))
    conn.commit()

def asignar_item_a_posicion(conn, rack, posicion, item_id):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO rack_items (Rack, Posicion, ItemID)
        VALUES (?, ?, ?)
    """, (rack, posicion, item_id))
    conn.commit()

def obtener_items_por_rack(conn, rack):
    query = """
        SELECT Posicion, item.ID, item.Descripcion
        FROM rack_items
        JOIN item ON item.ID = rack_items.ItemID
        WHERE rack_items.Rack = ?
        ORDER BY Posicion
    """
    return pd.read_sql_query(query, conn, params=(rack,))

def liberar_posicion(conn, rack, posicion):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rack_items WHERE Rack = ? AND Posicion = ?", (rack, posicion))
    conn.commit()

def liberar_item_en_posicion(conn, rack, posicion, item_id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM rack_items
        WHERE Rack = ? AND Posicion = ? AND ItemID = ?
    """, (rack, posicion, item_id))
    conn.commit()

def eliminar_rack(conn, nombre_rack):
    cursor = conn.cursor()
    # Eliminar ítems asignados al rack
    cursor.execute("DELETE FROM rack_items WHERE Rack = ?", (nombre_rack,))
    # Eliminar el rack
    cursor.execute("DELETE FROM racks WHERE Nombre = ?", (nombre_rack,))
    conn.commit()

