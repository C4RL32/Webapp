import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestor de Tareas", page_icon="✅", layout="centered")

# Header de la aplicación
st.markdown(
    """
    <style>
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #4A90E2;
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    <div class="header">
        Gestor de Tareas ✅
    </div>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("Bienvenido a tu Gestor de Tareas 📝")

# Inicializar la lista de tareas en la sesión de Streamlit
if "tareas" not in st.session_state:
    st.session_state.tareas = []

# Input para agregar una nueva tarea
nueva_tarea = st.text_input("Agrega una nueva tarea:")

# Botón para agregar la tarea
if st.button("Agregar tarea"):
    if nueva_tarea:  # Verificar que el input no esté vacío
        st.session_state.tareas.append({"tarea": nueva_tarea, "completada": False})
        st.success("Tarea agregada correctamente!")  # Mensaje de éxito
    else:
        st.warning("Por favor, ingresa una tarea válida.")  # Mensaje de advertencia

# Sección para mostrar la lista de tareas
st.header("Lista de Tareas")

# Mostrar las tareas en una lista con checkboxes y botones para eliminar
for i, tarea in enumerate(st.session_state.tareas):
    col1, col2, col3 = st.columns([1, 10, 2])
    with col1:
        # Checkbox para marcar la tarea como completada
        completada = st.checkbox(
            "", value=tarea["completada"], key=f"check_{i}", on_change=lambda i=i: marcar_como_completada(i)
        )
    with col2:
        # Mostrar la tarea (tachada si está completada)
        if tarea["completada"]:
            st.markdown(f"~~{tarea['tarea']}~~")  # Tarea tachada
        else:
            st.markdown(tarea["tarea"])  # Tarea normal
    with col3:
        # Botón para eliminar la tarea
        if st.button("❌", key=f"eliminar_{i}"):
            eliminar_tarea(i)
            st.experimental_rerun()  # Recargar la aplicación para actualizar la lista

# Footer de la aplicación
st.markdown(
    """
    <style>
    .footer {
        font-size: 16px;
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    <div class="footer">
        Desarrollado por <strong>Carlos Hernández</strong> 🚀
    </div>
    """,
    unsafe_allow_html=True
)

# Funciones para manejar la lógica de la aplicación
def marcar_como_completada(index):
    """Marca una tarea como completada o pendiente."""
    st.session_state.tareas[index]["completada"] = not st.session_state.tareas[index]["completada"]

def eliminar_tarea(index):
    """Elimina una tarea de la lista."""
    st.session_state.tareas.pop(index)
    st.success("Tarea eliminada correctamente!")