# -------------------------------------------------------------
# PESTAÑA: RASTREADOR DE UBICACIÓN DE SALAS (Estilo BotPower Live Track)
# -------------------------------------------------------------
st.markdown("### 📍 Live Room Tracker")
st.markdown("Consulta la actividad en tiempo real y salas recientes de cualquier usuario.")

tracker_user = st.text_input("Nombre del avatar a rastrear:", placeholder="Ej. mavielle", key="input_live_track")

if st.button("Rastrear Ubicación Activa", key="btn_live_track"):
    if tracker_user.strip() != "":
        u_clean = tracker_user.strip().lower()
        
        st.success(f"¡Buscando registros activos para: @{u_clean}!")
        
        # Tarjeta de estado simulando el panel de rastreo en vivo
        st.markdown(f"""
            <div style="background-color: #161618; border: 1px solid #2A2A2E; padding: 15px; border-radius: 12px; margin-bottom: 15px;">
                <h4 style="color: #FF4B4B; margin: 0;">📡 RASTREO EN VIVO: @{u_clean}</h4>
                <p style="color: #00FF7F; font-size: 13px; margin-top: 5px;">🟢 Escaneo de lobbies públicos: Activo</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Botones de acceso directo a las herramientas de rastreo y feeds de salas públicas
        st.link_button(
            f"🔍 Ver actividad de salas de @{u_clean}", 
            f"https://www.imvu.com/rooms/rooms.php?owner={u_clean}",
            use_container_width=True
        )
        st.link_button(
            f"🌐 Buscar menciones en chats y salas abiertas", 
            f"https://www.imvu.com/catalog/web_search.php?q={u_clean}&type=room",
            use_container_width=True
        )
    else:
        st.warning("Por favor, introduce un nombre de usuario para rastrear.")