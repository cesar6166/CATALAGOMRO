import streamlit as st
import modulos.Importar
import modulos.Racks
import modulos.Bienvenida
import modulos.Buscar

# ✅ Configuración de la página
st.set_page_config(
    page_title="Catálogo By Cesar Nunez",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🧭 Menú lateral
st.sidebar.title("📁 Menú principal")
opcion = st.sidebar.radio("Selecciona una opción", [
    "🏠 Bienvenida",
    "🔍 Buscar ítems",
    "📤 Importar ítems",
    "🏷️ Asignar ítems a racks"
])

# 🔀 Navegación entre módulos

if opcion == "🏠 Bienvenida":
    from modulos.Bienvenida import mostrar_bienvenida
    mostrar_bienvenida()

elif opcion == "🔍 Buscar ítems":
    from modulos.Buscar import mostrar_busqueda
    mostrar_busqueda()

elif opcion == "📤 Importar ítems":
    from modulos.Importar import mostrar_importador
    mostrar_importador()
    
elif opcion == "🏷️ Asignar ítems a racks":
    from modulos.Racks import mostrar_racks
    mostrar_racks()
