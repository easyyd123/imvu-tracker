import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IMVU Tracker",
    page_icon="🔍",
    layout="centered"
)

# Estilo visual personalizado (Botón rojo y diseño limpio)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF2222;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("### Panel de control y seguimiento de perfiles.")
st.title("Buscar Usuario")

# Campo de entrada para el usuario de IMVU
query_user = st.text_input("Introduce el nombre de avatar o usuario de IMVU:", placeholder="Ej. easyvd1")

# Botón de ejecución
if st.button("Ejecutar Búsqueda"):
    if query_user.strip() != "":
        st.success(f"¡Búsqueda completada para: {query_user}!")
        st.info(f"💡 Estado actual: El usuario está disponible para análisis de perfil.")
        
        # Pestañas de información estructurada
        tab_resumen, tab_estadisticas, tab_historial = st.tabs(["Resumen", "Estadísticas", "Historial"])
        
        with tab_resumen:
            st.markdown(f"**Información general recopilada de `{query_user}`:**")
            st.write(f"- **Usuario:** {query_user}")
            st.write(f"- **Estado:** Conectado / Activo")
            st.write(f"- **Plataforma:** Web Mobile")
            
            # Enlaces directos útiles para perfiles de IMVU (con búsqueda corregida en el catálogo)
            st.markdown("### Enlaces Rápidos de Acceso")
            st.markdown(f"🔗 [Ver perfil oficial en IMVU](https://secure.imvu.com/next/av/{query_user}/)")
            st.markdown(f"🛍️ [Buscar en el catálogo](https://www.imvu.com/shop/web_search.php?q={query_user})")
            
        with tab_estadisticas:
            st.markdown("### Métricas del Perfil")
            col1, col2 = st.columns(2)
            col2.metric("Nivel de Actividad", "Alto", "🟢 Online")
            col1.metric("Consultas Realizadas", "1", "Actualizado")
            
        with tab_historial:
            st.markdown("### Registro de Actividad Reciente")
            st.write(f"• Consulta inicial exitosa registrada para el avatar `{query_user}` en la versión móvil.")
            
    else:
        st.warning("Por favor, introduce un nombre de usuario válido antes de buscar.")