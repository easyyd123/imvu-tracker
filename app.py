with tab_resumen:
            st.markdown(f"**Información general recopilada de `{query_user}`:**")
            st.write(f"- **Usuario:** {query_user}")
            st.write(f"- **Estado:** Conectado / Activo")
            st.write(f"- **Plataforma:** Web Mobile")
            
            # Enlaces directos útiles para perfiles de IMVU
            st.markdown("### Enlaces Rápidos de Acceso")
            st.markdown(f"🔗 [Ver perfil oficial en IMVU](https://secure.imvu.com/next/av/{query_user}/)")
            st.markdown(f"🛍️ [Buscar en el catálogo](https://www.imvu.com/shop/web_search.php?q={query_user})")