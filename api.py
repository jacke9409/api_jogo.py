# #  quiz, infelizmente precisamos usar markdown para o nosso quiz
# # =========================
# # Quiz de 10 perguntas
# # =========================
# st.markdown("---")
# st.markdown("### ❓ Quiz de Games (10 Perguntas)")

# # Perguntas do quiz: cada item tem pergunta, opções e resposta correta
# quiz = [
#     {"pergunta": "Qual jogo foi lançado primeiro?", "opcoes": ["Minecraft", "Fortnite", "Zelda BOTW", "Roblox"], "correta": "Roblox"},
#     {"pergunta": "Qual jogo é exclusivo da Nintendo?", "opcoes": ["Fortnite", "Minecraft", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
#     {"pergunta": "Qual desses jogos tem 'mundos infinitos'?", "opcoes": ["Roblox", "Minecraft", "Fortnite"], "correta": "Minecraft"},
#     {"pergunta": "Qual é um Battle Royale?", "opcoes": ["Minecraft", "Zelda BOTW", "Fortnite"], "correta": "Fortnite"},
#     {"pergunta": "Qual jogo permite criar experiências próprias?", "opcoes": ["Roblox", "Zelda BOTW", "Fortnite"], "correta": "Roblox"},
#     {"pergunta": "Quem criou o Minecraft?", "opcoes": ["Markus 'Notch' Persson", "Shigeru Miyamoto", "Epic Games"], "correta": "Markus 'Notch' Persson"},
#     {"pergunta": "Qual jogo tem física e clima afetando a jogabilidade?", "opcoes": ["Fortnite", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
#     {"pergunta": "Qual desses é considerado um dos jogos mais vendidos da história?", "opcoes": ["Minecraft", "Fortnite", "Roblox"], "correta": "Minecraft"},
#     {"pergunta": "Qual desses jogos tem temporadas que mudam o mapa?", "opcoes": ["Fortnite", "Roblox", "Zelda BOTW"], "correta": "Fortnite"},
#     {"pergunta": "Qual jogo saiu em 2006?", "opcoes": ["Roblox", "Minecraft", "Zelda BOTW"], "correta": "Roblox"},
# ]

# # Inicializa um dicionário de respostas no estado da sessão
# if "respostas" not in st.session_state:
#     st.session_state.respostas = {}
#  essas são só as perguntas