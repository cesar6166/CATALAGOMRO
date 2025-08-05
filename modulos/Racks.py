import streamlit as st
import pandas as pd
from db.racks import (
    get_connection,
    crear_tabla_racks,
    crear_rack,
    asignar_item_a_posicion,
    obtener_items_por_rack,
    liberar_posicion,
    liberar_item_en_posicion,
    eliminar_rack
)

def mostrar_racks():
    st.header("📦 Organización de ítems por RACK y posición")
    conn = get_connection()
    crear_tabla_racks(conn)

    # 🔧 Crear nuevo rack
    st.subheader("🆕 Crear nuevo RACK")
    nuevo_rack = st.text_input("Nombre del nuevo RACK")
    racks = pd.read_sql_query("SELECT Nombre FROM racks", conn)["Nombre"].tolist()

    if st.button("Crear RACK"):
        if nuevo_rack.strip() == "":
            st.error("❌ El nombre del RACK no puede estar vacío.")
        elif nuevo_rack in racks:
            st.warning("⚠️ Este RACK ya existe.")
        else:
            crear_rack(conn, nuevo_rack)
            st.success(f"✅ RACK '{nuevo_rack}' creado correctamente.")
            st.rerun()

    # 📁 Seleccionar rack existente
    st.subheader("📁 Selecciona un RACK para gestionar")
    racks = pd.read_sql_query("SELECT Nombre FROM racks", conn)["Nombre"].tolist()
    if racks:
        rack_seleccionado = st.selectbox("RACK disponible", racks)

        # 📌 Asignar ítem a posición
        st.subheader("📌 Asignar ítem a una posición")
        posicion = st.selectbox("Posición en el rack", list("ABCDEFG"))
        item_id = st.text_input("ID del ítem a asignar")

        if st.button("Asignar ítem a posición"):
            if item_id.strip() == "":
                st.error("❌ Debes ingresar un ID de ítem.")
            else:
                asignar_item_a_posicion(conn, rack_seleccionado, posicion, item_id)
                st.success(f"✅ Ítem {item_id} asignado a {rack_seleccionado} - {posicion}")
                st.rerun()

        # 📋 Mostrar ítems en el rack
        st.subheader(f"📋 Ítems en {rack_seleccionado}")
        df = obtener_items_por_rack(conn, rack_seleccionado)
        st.dataframe(df, use_container_width=True)

        # 🗑️ Liberar ítems
        st.subheader("🗑️ Dar de baja ítems")
        with st.expander("Liberar todos los ítems de una posición"):
            pos_liberar = st.selectbox("Selecciona la posición", list("ABCDEFG"), key="liberar_pos")
            if st.button("Liberar posición completa"):
                liberar_posicion(conn, rack_seleccionado, pos_liberar)
                st.warning(f"⚠️ Todos los ítems en {rack_seleccionado} - {pos_liberar} han sido eliminados.")
                st.rerun()

        with st.expander("Liberar un ítem específico de una posición"):
            pos_item = st.selectbox("Posición", list("ABCDEFG"), key="liberar_item_pos")
            item_a_eliminar = st.text_input("ID del ítem a eliminar", key="liberar_item_id")
            if st.button("Eliminar ítem de posición"):
                liberar_item_en_posicion(conn, rack_seleccionado, pos_item, item_a_eliminar)
                st.warning(f"Ítem {item_a_eliminar} eliminado de {rack_seleccionado} - {pos_item}.")
                st.rerun()

        # 🧹 Eliminar rack completo
        st.subheader("🧹 Eliminar un RACK completo")
        rack_a_eliminar = st.selectbox("Selecciona el RACK a eliminar", racks, key="rack_eliminar")
        if st.button("Eliminar RACK"):
            eliminar_rack(conn, rack_a_eliminar)
            st.warning(f"⚠️ RACK '{rack_a_eliminar}' ha sido eliminado junto con sus asignaciones.")
            st.rerun()
    else:
        st.info("ℹ️ No hay racks registrados aún.")

