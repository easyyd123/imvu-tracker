import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="IMVU Tracker Pro",
    page_icon="⚡",
    layout="centered"
)

# Estilo visual moderno y limpio
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
# PESTAÑA 1: PERFIL & OUTFITS (Con Foto de Avatar e Historial)
# -------------------------------------------------------------
with tab_perfil:
    st.subheader("Buscador de Avatares")
    
    query_user = st.text_input("Introduce el nombre de usuario de IMVU:", placeholder="Ej. easyvd1", key="input_perfil")
    
    if st.button("Buscar Perfil", key="btn_perfil"):
        if query_user.strip() != "":
            avatar_limpio = query_user.strip()
            
            # Guardar en historial
            if avatar_limpio not in st.session_state.historial_busquedas:
                st.session_state.historial_busquedas.insert(0, avatar_limpio)
                if len(st.session_state.historial_busquedas) > 5:
                    st.session_state.historial_busquedas.pop()
                    
            st.success(f"¡Datos cargados para: {avatar_limpio}!")
            
            # Mostrar la tarjeta de perfil con imagen simulada/renderizada del avatar
            col_img, col_info = st.columns([1, 2])
            
            with col_img:
                # Imagen representativa del avatar basada en su nombre de usuario
                st.image(f"https://images.imvu.com/profile/pp_av_#{avatar_limpio}.jpg", width=120, caption=f"@{avatar_limpio}")
                
            with col_info:
                st.markdown(f"**Avatar:** `{avatar_limpio}`")
                st.markdown(f"**Estado:** Monitoreo Activo 🟢")
                st.markdown(f"**Plataforma:** Web Mobile App")
            
            st.markdown("---")
            
            sub_tab1, sub_tab2 = st.tabs(["Información General", "Enlaces Directos"])
            
            with sub_tab1:
                st.write(f"- **Nombre de usuario:** {avatar_limpio}")
                st.write(f"- **Tipo de cuenta:** Estándar / Verificada")
                st.write(f"- **Acceso rápido a tienda:** Habilitado")
                
            with sub_tab2:
                st.link_button(f"🔗 Ver perfil oficial de {avatar_limpio}", f"https://secure.imvu.com/next/av/{avatar_limpio}/")
                st.link_button(f"👗 Buscar prendas / outfits relacionados", f"https://www.imvu.com/shop/web_search.php?q={avatar_limpio}")
        else:
            st.warning("Por favor, introduce un nombre de usuario válido.")
            
    if st.session_state.historial_busquedas:
        st.markdown("---")
        st.markdown("🕒 **Búsquedas recientes en esta sesión:**")
        for av in st.session_state.historial_busquedas:
            st.markdown(f"• `{av}` ➔ [Ver Perfil](https://secure.imvu.com/next/av/{av}/)")

# -------------------------------------------------------------
# PESTAÑA 2: SALAS (Con Teleport e Historial de Salas)
# -------------------------------------------------------------
with tab_salas:
    st.subheader("🏠 Teleport y Historial de Salas")
    
    room_id = st.text_input("Introduce el ID o nombre de la sala:", placeholder="Ej. 12345678 o nombre de sala", key="input_sala_id")
    
    if st.button("Generar Enlace de Sala", key="btn_sala"):
        if room_id.strip() != "":
            sala_limpia = room_id.strip()
            
            if sala_limpia not in st.session_state.historial_salas:
                st.session_state.historial_salas.insert(0, sala_limpia)
                if len(st.session_state.historial_salas) > 5:
                    st.session_state.historial_salas.pop()
                    
            st.success(f"¡Acceso directo generado para la sala: {sala_limpia}!")
            
            st.link_button(f"🌐 Entrar a la sala ({sala_limpia})", f"https://www.imvu.com/rooms/{sala_limpia}")
            st.link_button("📂 Explorar directorio general de salas", "https://www.imvu.com/rooms/")
        else:
            st.warning("Por favor, introduce un ID o término de sala válido.")
            
    if st.session_state.historial_salas:
        st.markdown("---")
        st.markdown("🕒 **Salas recientes en esta sesión:**")
        for sal in st.session_state.historial_salas:
            st.markdown(f"• Sala ID: `{sal}` ➔ [Entrar Directo](https://www.imvu.com/rooms/{sal})")

# -------------------------------------------------------------
# PESTAÑA 3: CATÁLOGO
# -------------------------------------------------------------
with tab_catalogo:
    st.subheader("Explorador de Productos y Creadores")
    prod_query = st.text_input("Buscar producto o creador:", placeholder="Ej. Hair, Jeans, CreatorName", key="input_prod")
    
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
                st.markdown(f"**📌 {user_1}**")
                st.link_button(f"🔗 Perfil A ({user_1})", f"https://secure.imvu.com/next/av/{user_1}/")
                st.link_button(f"🛍️ Catálogo A", f"https://www.imvu.com/shop/web_search.php?q={user_1}")
                
            with col_res2:
                st.markdown(f"**📌 {user_2}**")
                st.link_button(f"🔗 Perfil B ({user_2})", f"https://secure.imvu.com/next/av/{user_2}/")
                st.link_button(f"🛍️ Catálogo B", f"https://www.imvu.com/shop/web_search.php?q={user_2}")
        else:
            st.warning("Por favor, introduce ambos nombres de usuario para comparar.")