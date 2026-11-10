import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IMVU Tracker Pro",
    page_icon="⚡",
    layout="centered"
)

# Estilo visual moderno y oscuro tipo BotPower
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #FF2222;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar estados en la sesión si no existen
if 'historial_busquedas' not in st.session_state:
    st.session_state.historial_busquedas = []

if 'historial_salas' not in st.session_state:
    st.session_state.historial_salas = []

# Encabezado principal
st.markdown("### ⚡ IMVU Tracker & Toolkit")
st.title("Panel de Control")

# Pestañas principales de navegación
tab_perfil, tab_salas, tab_catalogo, tab_comparar = st.tabs([
    "👤 Perfil & Outfits", 
    "🏠 Salas", 
    "🛍️ Catálogo", 
    "⚖️ Comparador"
])

# -------------------------------------------------------------
# PESTAÑA 1: PERFIL & OUTFITS
# -------------------------------------------------------------
with tab_perfil:
    st.subheader("Buscador de Avatares")
    
    query_user = st.text_input("Introduce el nombre de usuario de IMVU:", placeholder="Ej. mavielle", key="input_perfil_main")
    
    if st.button("Buscar Perfil", key="btn_perfil_main_action"):
        if query_user.strip() != "":
            avatar_limpio = query_user.strip().lower()
            
            if avatar_limpio not in st.session_state.historial_busquedas:
                st.session_state.historial_busquedas.insert(0, avatar_limpio)
                if len(st.session_state.historial_busquedas) > 4:
                    st.session_state.historial_busquedas.pop()
                    
            st.success(f"¡Datos cargados para: @{avatar_limpio}!")
            
            st.markdown(f"""
                <div style="background-color: #161618; border: 1px solid #2A2A2E; padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                    <h3 style="color: #FF4B4B; margin: 0;">📌 @{avatar_limpio}</h3>
                    <p style="color: #00FF7F; font-size: 13px; margin-top: 5px;">🟢 Monitoreo Activo</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.link_button(f"🔗 Ver perfil oficial de @{avatar_limpio}", f"https://secure.imvu.com/next/av/{avatar_limpio}/", use_container_width=True)
            st.link_button(f"🛍️ Buscar prendas / outfits relacionados", f"https://www.imvu.com/shop/web_search.php?q={avatar_limpio}", use_container_width=True)
        else:
            st.warning("Por favor, introduce un nombre de usuario válido.")
            
    if st.session_state.historial_busquedas:
        st.markdown("---")
        st.markdown("🕒 **Búsquedas recientes:**")
        for av in st.session_state.historial_busquedas:
            st.markdown(f"• `@{av}` ➔ [Ver Perfil](https://secure.imvu.com/next/av/{av}/)")

# -------------------------------------------------------------
# PESTAÑA 2: SALAS (Con Rastreador de Ubicación)
# -------------------------------------------------------------
with tab_salas:
    st.subheader("🏠 Rastreador y Teleport de Salas")
    
    # Sub-sección 1: Teleport por ID de Sala
    room_id = st.text_input("Introduce el ID de la sala:", placeholder="Ej. 12345678", key="input_sala_id_unique")
    
    if st.button("Generar Enlace de Sala", key="btn_sala_id_action"):
        if room_id.strip() != "":
            sala_limpia = room_id.strip()
            
            if sala_limpia not in st.session_state.historial_salas:
                st.session_state.historial_salas.insert(0, sala_limpia)
                if len(st.session_state.historial_salas) > 5:
                    st.session_state.historial_salas.pop()
                    
            st.success(f"¡Acceso directo generado para la sala: {sala_limpia}!")
            st.link_button(f"🌐 Entrar a la sala ({sala_limpia})", f"https://www.imvu.com/rooms/{sala_limpia}", use_container_width=True)
        else:
            st.warning("Introduce un ID de sala válido.")
            
    st.markdown("---")
    
    # Sub-sección 2: Rastreador de Salas por Usuario (Estilo BotPower Live Track)
    st.markdown("### 📡 Rastreo de Salas por Usuario")
    tracker_user = st.text_input("Nombre del avatar a rastrear en salas:", placeholder="Ej. mavielle", key="input_tracker_user_unique")
    
    if st.button("Rastrear Actividad de Salas", key="btn_tracker_user_action"):
        if tracker_user.strip() != "":
            u_clean = tracker_user.strip().lower()
            
            st.success(f"¡Buscando registros de espacios para: @{u_clean}!")
            
            st.markdown(f"""
                <div style="background-color: #161618; border: 1px solid #2A2A2E; padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                    <h4 style="color: #FF4B4B; margin: 0;">📡 LOBBIES Y SALAS: @{u_clean}</h4>
                    <p style="color: #00FF7F; font-size: 13px; margin-top: 5px;">🟢 Estado: Análisis de espacios públicos activo</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.link_button(
                f"🏠 Ver salas creadas/públicas de @{u_clean}", 
                f"https://www.imvu.com/rooms/rooms.php?owner={u_clean}",
                use_container_width=True
            )
            st.link_button(
                f"🌐 Buscar menciones en chats y salas", 
                f"https://www.imvu.com/catalog/web_search.php?q={u_clean}&type=room",
                use_container_width=True
            )
        else:
            st.warning("Por favor, introduce un nombre de usuario válido para rastrear.")

# -------------------------------------------------------------
# PESTAÑA 3: CATÁLOGO
# -------------------------------------------------------------
with tab_catalogo:
    st.subheader("Explorador de Productos y Creadores")
    prod_query = st.text_input("Buscar producto o creador:", placeholder="Ej. Hair, Jeans", key="input_prod_unique")
    
    if st.button("Buscar en Tienda", key="btn_prod_action"):
        if prod_query.strip() != "":
            st.success(f"Búsqueda en catálogo para: {prod_query}")
            st.link_button("🛍️ Ver resultados en la tienda de IMVU", f"https://www.imvu.com/shop/web_search.php?q={prod_query}", use_container_width=True)
        else:
            st.warning("Introduce el nombre de un artículo o creador.")

# -------------------------------------------------------------
# PESTAÑA 4: COMPARADOR DE PERFILES
# -------------------------------------------------------------
with tab_comparar:
    st.subheader("Comparador Rápido de Avatares")
    col_a, col_b = st.columns(2)
    
    with col_a:
        user_1 = st.text_input("Avatar A:", placeholder="Primer usuario", key="cmp_1_unique")
    with col_b:
        user_2 = st.text_input("Avatar B:", placeholder="Segundo usuario", key="cmp_2_unique")
        
    if st.button("Comparar Perfiles", key="btn_cmp_action"):
        if user_1.strip() and user_2.strip():
            st.success("¡Comparación generada con éxito!")
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.markdown(f"**📌 @{user_1.strip()}**")
                st.link_button(f"🔗 Perfil A", f"https://secure.imvu.com/next/av/{user_1.strip()}/", use_container_width=True)
                
            with col_res2:
                st.markdown(f"**📌 @{user_2.strip()}**")
                st.link_button(f"🔗 Perfil B", f"https://secure.imvu.com/next/av/{user_2.strip()}/", use_container_width=True)
        else:
            st.warning("Por favor, introduce ambos nombres de usuario para comparar.")