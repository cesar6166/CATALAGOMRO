import streamlit as st

def mostrar_bienvenida():
    st.title("👋 Bienvenido al Catálogo MRO")
    st.markdown("""
    Este sistema te permite gestionar el inventario de ítems en el almacén **MROGRAL**, incluyendo:

    - 📤 Importación de ítems desde Excel.
    - 📋 Visualización del catálogo general pendiente.
    - 🏷️ Asignación de ítems a posiciones dentro de racks.


    ---
    **¿Cómo usar el sistema?**
    - Usa el menú lateral para navegar entre módulos.
    - Puedes crear racks, asignar ítems, y consultar el estado de cada posición.
    - Los cambios se actualizan automáticamente.

    ---
    **Desarrollado por:** *Cesar Nuñez*  
    **Versión:** 1.0  
    **Fecha:** Agosto 2025
    """)
