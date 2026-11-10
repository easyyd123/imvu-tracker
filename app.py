import streamlit as st

# Configuración de la página web (nombre en la pestaña del navegador)
st.set_page_config(page_title="IMVU Tracker", page_icon="🔍", layout="centered")

# Título principal limpio
st.title("IMVU Tracker")
st.write("Panel de control y seguimiento de perfiles.")

# Creamos un contenedor o sección de búsqueda
st.subheader("Buscar Usuario")
nombre_usuario = st.text_input("Introduce el nombre de avatar o usuario de IMVU:")

# Botón de búsqueda con lógica estructurada
if st.button("Ejecutar Búsqueda", type="primary"):
    if nombre_usuario.strip() != "":
        # Simulamos un proceso de consulta estructurado
        with st.spinner(f"Consultando registros para '{nombre_usuario}'..."):
            # Aquí irá la lógica de extracción de datos en las próximas fases
            import time
            time.sleep(1) # Pequeña pausa visual de carga
            
        st.success(f"¡Búsqueda completada para: **{nombre_usuario}**!")
        
        # Mostramos una tarjeta o sección con datos simulados pero listos para conectar
        st.info("💡 **Estado actual:** El usuario está disponible para análisis de perfil.")
        
        # Sección de pestañas para organizar la futura información (ideal para móviles)
        tab1, tab2 = st.tabs(["📊 Resumen", "🕒 Historial"])
        
        with tab1:
            st.write(f"Información general recopilada de **{nombre_usuario}**:")
            st.code(f"Usuario: {nombre_usuario}\nEstado: Conectado / Activo\nPlataforma: Web Mobile")
            
        with tab2:
            st.write("Registro de eventos recientes:")
            st.write("• No hay registros previos guardados en el historial todavía.")
            
    else:
        st.warning("⚠️ Por favor, introduce un nombre de usuario válido antes de buscar.")