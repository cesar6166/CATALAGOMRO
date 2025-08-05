import streamlit as st
from db.items import get_connection, crear_tablas, importar_items_desde_excel

def mostrar_importador():
    st.header("📤 Importar ítems desde Excel")
    conn = get_connection()
    crear_tablas(conn)

    archivo_excel = st.file_uploader("Selecciona el archivo Excel", type=["xlsx","xlsm"])
    if archivo_excel is not None:
        importar_items_desde_excel(conn, archivo_excel)
        st.success("✅ Ítems importados correctamente.")
