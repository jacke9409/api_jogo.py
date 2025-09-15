# # api do zelda
# # =========================
# # Função para buscar dados em JSON da API Zelda
# # =========================
# def buscar_zelda_api(jogo):
#     """
#     Busca dados do jogo/anime Zelda na API Jikan.
#     Retorna um dicionário com título, imagem, sinopse e link.
#     """
#     url = f"https://api.jikan.moe/v4/anime?q={jogo}&limit=1"
#     resposta = requests.get(url)
#     if resposta.status_code == 200:
#         dados = resposta.json()  # JSON retornado pela API
#         if dados["data"]:  # Confere se encontrou algum resultado
#             anime = dados["data"][0]
#             return {
#                 "titulo": anime["title"],
#                 "imagem": anime["images"]["jpg"]["image_url"],
#                 "sinopse": anime["synopsis"],
#                 "link": anime["url"]
#             }
#     return None
