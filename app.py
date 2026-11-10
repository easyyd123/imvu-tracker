# -------------------------------------------------------------
# PESTAÑA 1: PERFIL & OUTFITS
# -------------------------------------------------------------
with tab_perfil:
    st.subheader("Buscador de Avatares")
    query_user = st.text_input("Introduce el nombre de usuario de IMVU:", placeholder="Ej. easyvd1", key="input_perfil")
    
    if st.button("Buscar Perfil", key="btn_perfil"):
        if query_user.strip() != "":
            st.success(f"¡Datos cargados para: {query_user}!")
            
            sub_tab1, sub_tab2 = st.tabs(["Información General", "Enlaces Directos"])
            
            with sub_tab1:
                st.write(f"- **Avatar:** {query_user}")
                st.write(f"- **Estado de Conexión:** Monitoreo Activo 🟢")
                st.write(f"- **Plataforma:** Web Mobile App")
                
            with sub_tab2:
                # Usamos botones de enlace nativos para una experiencia móvil más limpia
                st.link_button(f"🔗 Ver perfil oficial de {query_user}", f"https://secure.imvu.com/next/av/{query_user}/")
                st.link_button(f"👗 Buscar prendas / outfits relacionados", f"https://www.imvu.com/shop/web_search.php?q={query_user}")
        else:
            st.warning("Por favor, introduce un nombre de usuario válido.")