import streamlit as st
import pandas as pd
from db.items import get_connection

def mostrar_busqueda():
    st.header("🔍 Buscar ítems en el sistema")
    conn = get_connection()

    criterio = st.radio("Buscar por:", ["ID", "Descripción"])
    texto = st.text_input("🔎 Escribe tu búsqueda")

    if texto:
        if criterio == "ID":
            query = """
                SELECT item.ID, item.Descripcion, rack_items.Rack, rack_items.Posicion
                FROM item
                LEFT JOIN rack_items ON item.ID = rack_items.ItemID
                WHERE item.ID LIKE ?
            """
        else:
            query = """
                SELECT item.ID, item.Descripcion, rack_items.Rack, rack_items.Posicion
                FROM item
                LEFT JOIN rack_items ON item.ID = rack_items.ItemID
                WHERE item.Descripcion LIKE ?
            """

        df = pd.read_sql_query(query, conn, params=(f"%{texto}%",))
        st.dataframe(df, use_container_width=True)

        if df.empty:
            st.info("No se encontraron ítems con ese criterio.")
