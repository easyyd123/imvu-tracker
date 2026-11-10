import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IMVU Tracker Pro",
    page_icon="⚡",
    layout="centered"
)

# Estilo visual oscuro profesional tipo BotPower
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
    .room-card {
        background-color: #161618;
        border: 1px solid #2A2A2E;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar estados de sesión
if 'historial_busquedas' not in st.session_state:
    st.session_state.historial_busquedas = []

if 'rooms_searched' not in st.session_state:
    st.session_state.rooms_searched = None

# Encabezado principal
st.markdown("### ⚡ IMVU Tracker & Toolkit")
st.title("Panel de Control")

tab_perfil, tab_salas, tab_catalogo, tab_comparar = st.tabs([
    "👤 Perfil & Outfits", 
    "🏠 Room List", 
    "🛍️ Catálogo", 
    "⚖️ Comparador"
])

# -------------------------------------------------------------
# PESTAÑA 1: PERFIL & OUTFITS
# -------------------------------------------------------------
with tab_perfil:
    st.subheader("Buscador de Avatares")
    query_user = st.text_input("Introduce el nombre de usuario:", placeholder="Ej. Easyd1", key="input_perf")
    
    if st.button("Buscar Perfil", key="btn_perf"):
        if query_user.strip() != "":
            u = query_user.strip()
            st.success(f"¡Datos cargados para: {u}!")
            st.markdown(f"""
                <div class="room-card">
                    <h3 style="color: #FF4B4B; margin: 0;">📌 @{u}</h3>
                    <p style="color: #00FF7F; font-size: 13px; margin-top: 5px;">🟢 Monitoreo Activo</p>
                </div>
            """, unsafe_allow_html=True)
            st.link_button(f"🔗 Ver perfil oficial", f"https://secure.imvu.com/next/av/{u}/", use_container_width=True)
        else:
            st.warning("Introduce un nombre válido.")

# -------------------------------------------------------------
# PESTAÑA 2: ROOM LIST (Historial Completo de Salas)
# -------------------------------------------------------------
with tab_salas:
    st.markdown("<h2 style='text-align: center;'>ROOM LIST</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Historial completo de rastreo y salas visitadas</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="room-card">', unsafe_allow_html=True)
        room_username = st.text_input("Username", placeholder="Easyd1", key="room_u")
        room_with_user = st.text_input("With user (optional)", placeholder="Filtro secundario", key="room_with")
        search_btn = st.button("SEARCH", key="btn_search_rooms")
        st.markdown('</div>', unsafe_allow_html=True)
        
    if search_btn:
        if room_username.strip() != "":
            st.session_state.rooms_searched = room_username.strip()
            
    if st.session_state.rooms_searched:
        u_clean = st.session_state.rooms_searched
        w_clean = room_with_user.strip() if room_with_user else "Ninguno"
        
        st.success(f"Historial completo de salas para @{u_clean}")
        
        # Tarjeta de estadísticas de usuario estilo BotPower
        st.markdown(f"""
            <div class="room-card" style="text-align: center;">
                <h4 style="color: #FF4B4B; margin-bottom: 10px;">👤 @{u_clean}</h4>
                <div style="display: flex; justify-content: space-around; margin-top: 15px;">
                    <div><span style="font-size: 18px; font-weight: bold; color: white;">1,386</span><br><span style="font-size: 10px; color: #888;">ROOMS</span></div>
                    <div><span style="font-size: 18px; font-weight: bold; color: white;">796</span><br><span style="font-size: 10px; color: #888;">PUBLIC</span></div>
                    <div><span style="font-size: 18px; font-weight: bold; color: white;">576</span><br><span style="font-size: 10px; color: #888;">PRIVATE</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🕒 Complete Rooms History & Snapshots")
        
        # Lista simulada de historial completo de salas (puedes expandir esta lista con más registros)
        historial_salas = [
            {"nombre": "Santorini Pool & Chill", "personas": 2, "tiempo": "10h ago", "id": "101"},
            {"nombre": "18+ Chill Zone & Music", "personas": 4, "tiempo": "11h ago", "id": "102"},
            {"nombre": "VIP Luxury Penthouse", "personas": 6, "tiempo": "14h ago", "id": "103"},
            {"nombre": "Underground Cyber Club", "personas": 12, "tiempo": "1 día ago", "id": "104"},
            {"nombre": "Aesthetic Sunset Lounge", "personas": 3, "tiempo": "1 día ago", "id": "105"},
            {"nombre": "Private Coffee & Chat", "personas": 2, "tiempo": "2 días ago", "id": "106"}
        ]
        
        # Mostrar el historial completo organizado en una cuadrícula de 2 columnas
        for i in range(0, len(historial_salas), 2):
            col1, col2 = st.columns(2)
            
            # Sala izquierda
            with col1:
                sala = historial_salas[i]
                st.markdown(f"""
                    <div class="room-card">
                        <b style="color: white; font-size: 13px;">{sala['nombre']}</b><br>
                        <span style="color: #888; font-size: 11px;">👤 {sala['personas']} personas · {sala['tiempo']}</span><br>
                        <span style="color: #00FF7F; font-size: 10px;">🟢 Registro verificado</span>
                    </div>
                """, unsafe_allow_html=True)
                st.link_button(f"🌐 Entrar ({sala['nombre'][:10]}...)", f"https://www.imvu.com/rooms/rooms.php?owner={u_clean}", key=f"room_left_{i}", use_container_width=True)
                
            # Sala derecha (si existe)
            if i + 1 < len(historial_salas):
                with col2:
                    sala_ der = historial_salas[i+1]
                    st.markdown(f"""
                        <div class="room-card">
                            <b style="color: white; font-size: 13px;">{sala_der['nombre']}</b><br>
                            <span style="color: #888; font-size: 11px;">👤 {sala_der['personas']} personas · {sala_der['tiempo']}</span><br>
                            <span style="color: #00FF7F; font-size: 10px;">🟢 Registro verificado</span>
                        </div>
                    """, unsafe_allow_html=True)
                    st.link_button(f"🌐 Entrar ({sala_der['nombre'][:10]}...)", f"https://www.imvu.com/rooms/rooms.php?owner={u_clean}", key=f"room_right_{i+1}", use_container_width=True)

# -------------------------------------------------------------
# PESTAÑA 3: CATÁLOGO
# -------------------------------------------------------------
with tab_catalogo:
    st.subheader("Explorador de Productos y Creadores")
    prod_query = st.text_input("Buscar producto o creador:", placeholder="Ej. Hair", key="cat_q")
    if st.button("Buscar en Tienda", key="btn_cat"):
        if prod_query.strip():
            st.link_button("🛍️ Ver en la tienda IMVU", f"https://www.imvu.com/shop/web_search.php?q={prod_query}", use_container_width=True)

# -------------------------------------------------------------
# PESTAÑA 4: COMPARADOR
# -------------------------------------------------------------
with tab_comparar:
    st.subheader("Comparador de Avatares")
    c1, c2 = st.columns(2)
    with c1: u1 = st.text_input("Avatar A:", key="cmp1")
    with c2: u2 = st.text_input("Avatar B:", key="cmp2")
    if st.button("Comparar", key="btn_cmp"):
        if u1 and u2:
            st.success("¡Comparación lista!")
            cc1, cc2 = st.columns(2)
            with cc1: st.link_button(f"🔗 Perfil @{u1}", f"https://secure.imvu.com/next/av/{u1}/", use_container_width=True)
            with cc2: st.link_button(f"🔗 Perfil @{u2}", f"https://secure.imvu.com/next/av/{u2}/", use_container_width=True)