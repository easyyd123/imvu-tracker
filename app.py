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
# PESTAÑA 1: PERFIL & OUTFITS (Con fotos de avatar estilo BotPower)
# -------------------------------------------------------------
with tab_perfil:
    st.subheader("Buscador de Avatares")
    
    query_user = st.text_input("Introduce el nombre de usuario de IMVU:", placeholder="Ej. mavielle", key="input_perfil")
    
    if st.button("Buscar Perfil", key="btn_perfil"):
        if query_user.strip() != "":
            avatar_limpio = query_user.strip().lower()
            
            # URL oficial directa de renderizado de avatar en IMVU
            avatar_url = f"https://userimages.imvu.com/gallery/avatar_{avatar_limpio}.jpg"
            
            # Guardar en el historial evitando duplicados
            if not any(item['nombre'] == avatar_limpio for item in st.session_state.historial_busquedas):
                st.session_state.historial_busquedas.insert(0, {
                    'nombre': avatar_limpio,
                    'img': avatar_url
                })
                if len(st.session_state.historial_busquedas) > 4:
                    st.session_state.historial_busquedas.pop()
                    
            st.success(f"¡Datos cargados para: {avatar_limpio}!")
            
            # Tarjeta de perfil principal con imagen oficial
            col_img, col_info = st.columns([1, 1])
            with col_img:
                st.image(avatar_url, caption=f"@{avatar_limpio}", use_column_width=True)
            with col_info:
                st.markdown(f"### @{avatar_limpio}")
                st.markdown("🟢 **Estado:** Activo")
                st.link_button(f"🔗 Ver Perfil", f"https://secure.imvu.com/next/av/{avatar_limpio}/")
                st.link_button(f"🛍️ Catálogo", f"https://www.imvu.com/shop/web_search.php?q={avatar_limpio}")
                
            st.markdown("---")
        else:
            st.warning("Por favor, introduce un nombre de usuario válido.")
            
    # Sección de Búsquedas Recientes estilo Cuadrícula (BotPower Style)
    st.markdown("### RECENT LOOKUPS")
    
    historial = st.session_state.historial_busquedas
    slots = historial + [{'nombre': 'No search yet', 'img': None}] * (4 - len(historial))
    
    col_r1, col_r2 = st.columns(2)
    
    with col_r1:
        # Tarjeta 1
        with st.container():
            if slots[0]['img']:
                st.image(slots[0]['img'], use_column_width=True)
                st.markdown(f"**@{slots[0]['nombre']}**")
                st.link_button(f"Ver Perfil", f"https://secure.imvu.com/next/av/{slots[0]['nombre']}/", key="btn_h0")
            else:
                st.info("No search yet")
                
        # Tarjeta 3
        with st.container():
            if slots[2]['img']:
                st.image(slots[2]['img'], use_column_width=True)
                st.markdown(f"**@{slots[2]['nombre']}**")
                st.link_button(f"Ver Perfil", f"https://secure.imvu.com/next/av/{slots[2]['nombre']}/", key="btn_h2")
            else:
                st.info("No search yet")
                
    with col_r2:
        # Tarjeta 2
        with st.container():
            if slots[1]['img']:
                st.image(slots[1]['img'], use_column_width=True)
                st.markdown(f"**@{slots[1]['nombre']}**")
                st.link_button(f"Ver Perfil", f"https://secure.imvu.com/next/av/{slots[1]['nombre']}/", key="btn_h1")
            else:
                st.info("No search yet")
                
        # Tarjeta 4
        with st.container():
            if slots[3]['img']:
                st.image(slots[3]['img'], use_column_width=True)
                st.markdown(f"**@{slots[3]['nombre']}**")
                st.link_button(f"Ver Perfil", f"https://secure.imvu.com/next/av/{slots[3]['nombre']}/", key="btn_h3")
            else:
                st.info("No search yet")

# -------------------------------------------------------------
# PESTAÑA 2: SALAS
# -------------------------------------------------------------
with tab_salas:
    st.subheader("🏠 Teleport y Historial de Salas")
    
    room_id = st.text_input("Introduce el ID o nombre de la sala:", placeholder="Ej. 12345678", key="input_sala_id")
    
    if st.button("Generar Enlace de Sala", key="btn_sala"):
        if room_id.strip() != "":
            sala_limpia = room_id.strip()
            
            if sala_limpia not in st.session_state.historial_salas:
                st.session_state.historial_salas.insert(0, sala_limpia)
                if len(st.session_state.historial_salas) > 5:
                    st.session_state.historial_salas.pop()
                    
            st.success(f"¡Acceso directo generado para la sala: {sala_limpia}!")
            st.link_button(f"🌐 Entrar a la sala ({sala_limpia})", f"https://www.imvu.com/rooms/{sala_limpia}")
        else:
            st.warning("Introduce un ID o término de sala válido.")
            
    if st.session_state.historial_salas:
        st.markdown("---")
        st.markdown("🕒 **Salas recientes:**")
        for sal in st.session_state.historial_salas:
            st.markdown(f"• Sala ID: `{sal}` ➔ [Entrar Directo](https://www.imvu.com/rooms/{sal})")

# -------------------------------------------------------------
# PESTAÑA 3: CATÁLOGO
# -------------------------------------------------------------
with tab_catalogo:
    st.subheader("Explorador de Productos y Creadores")
    prod_query = st.text_input("Buscar producto o creador:", placeholder="Ej. Hair, Jeans", key="input_prod")
    
    if st.button("Buscar en Tienda", key="btn_prod"):
        if prod_query.strip() != "":
            st.success(f"Búsqueda en catálogo para: {prod_query}")
            st.link_button("🛍️ Ver resultados en la tienda de IMVU", f"https://www.imvu.com/shop/web_search.php?q={prod_query}")
        else:
            st.warning("Introduce el nombre de un artículo o creador.")

# -------------------------------------------------------------
# PESTAÑA 4: COMPARADOR DE PERFILES
# -------------------------------------------------------------
with tab_comparar:
    st.subheader("Comparador Rápido de Avatares")
    col_a, col_b = st.columns(2)
    
    with col_a:
        user_1 = st.text_input("Avatar A:", placeholder="Primer usuario", key="cmp_1")
    with col_b:
        user_2 = st.text_input("Avatar B:", placeholder="Segundo usuario", key="cmp_2")
        
    if st.button("Comparar Perfiles", key="btn_cmp"):
        if user_1.strip() and user_2.strip():
            st.success("¡Comparación generada con éxito!")
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                st.image(f"https://userimages.imvu.com/gallery/avatar_{user_1.strip().lower()}.jpg", use_column_width=True)
                st.markdown(f"**📌 @{user_1}**")
                st.link_button(f"🔗 Perfil A", f"https://secure.imvu.com/next/av/{user_1}/")
                
            with col_res2:
                st.image(f"https://userimages.imvu.com/gallery/avatar_{user_2.strip().lower()}.jpg", use_column_width=True)
                st.markdown(f"**📌 @{user_2}**")
                st.link_button(f"🔗 Perfil B", f"https://secure.imvu.com/next/av/{user_2}/")
        else:
            st.warning("Por favor, introduce ambos nombres de usuario para comparar.")