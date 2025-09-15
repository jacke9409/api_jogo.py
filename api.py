# # consumindo a api
# # =========================
# # Imports necessários
# # =========================
# import streamlit as st
# import datetime as dt
# import requests
# import plotly.express as px

# # =========================
# # Configuração da página
# # =========================
# st.set_page_config(
#     page_title="Games Hub • Infos & Curiosidades",
#     page_icon="🎮",
#     layout="centered"
# )

# # =========================
# # Estilos CSS
# # =========================
# st.markdown("""
# <style>
# .main {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     text-align: center;
# }
# img {
#     border-radius: 10px;
# }
# .card {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     text-align: center;
#     padding: 20px;
#     border-radius: 15px;
#     margin-bottom: 20px;
#     width: 400px;
#     color: white;
# }
# </style>
# """, unsafe_allow_html=True)

# # =========================
# # Cabeçalho
# # =========================
# st.title("🎮 Games Hub: Infos & Curiosidades")
# st.caption(f"Data: {dt.date.today():%d/%m/%Y}")
# st.write("Selecione um jogo para ver informações, destaques e curiosidades.")

# # =========================
# # Função para buscar dados da API Jikan (Anime/ Zelda)
# # =========================
# def buscar_anime(nome):
#     url = f"https://api.jikan.moe/v4/anime?q={nome}&limit=1"
#     res = requests.get(url)
#     if res.status_code == 200 and res.json()["data"]:
#         anime = res.json()["data"][0]
#         return {
#             "titulo": anime["title"],
#             "imagem": anime["images"]["jpg"]["image_url"],
#             "sinopse": anime["synopsis"],
#             "link": anime["url"]
#         }
#     return None

# # =========================
# # Sidebar
# # =========================
# st.sidebar.header("Escolha um jogo")
# game = st.sidebar.selectbox("🎮 Jogos disponíveis", list(games.keys()))
# info = games[game]

# # =========================
# # Card centralizado do jogo
# # =========================
# if info:  # Confere se a API retornou dados
#     imagem = info.get("imagem", "")
#     cor = info.get("cor", "#333333")
#     link = info.get("link", "#")
#     titulo = info.get("titulo", game)
#     detalhes = info.get("detalhes", info.get("sinopse", "Detalhes não disponíveis."))
#     curiosidades = info.get("curiosidades", [])

#     st.markdown(f"""
#     <div class="card" style="background-color:{cor}">
#         <img src="{imagem}" width="200">
#         <h2>{titulo}</h2>
#         <p><strong>Gênero:</strong> {info.get("genero", "N/A")}</p>
#         <p><strong>Lançamento:</strong> {info.get("lancamento", "N/A")}</p>
#         <a href="{link}" target="_blank" style="color:white; text-decoration:underline;">
#             🔗 Página oficial
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("### 📝 Destaques")
#     st.write(detalhes)

#     st.markdown("### ✨ Curiosidades")
#     for c in curiosidades:
#         st.write(f"- {c}")
