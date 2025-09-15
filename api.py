#  juntamos o codigo mas ainda ficou muito simples. Vamos adicionar mais jogos
# =========================
# Games Hub com Quiz + Resultados Detalhados
# =========================

# Importa as bibliotecas que vamos usar
import streamlit as st        # Biblioteca para criar a interface web
import datetime as dt         # Biblioteca para trabalhar com datas
import plotly.express as px   # Biblioteca para criar gráficos interativos

# =========================
# Configuração da página
# =========================
st.set_page_config(           # Define as configurações da página do Streamlit
    page_title="Games Hub • Infos & Curiosidades",  # Título da aba
    page_icon="🎮",                                # Ícone da aba
    layout="centered"                              # Layout centralizado
)

# Estilos CSS para personalizar a aparência
st.markdown(
    """
    <style>
    .main {                     /* Centraliza todo o conteúdo */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    img {                       /* Deixa imagens com bordas arredondadas */
        border-radius: 10px;
    }
    .card {                     /* Estiliza o "card" dos jogos */
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        width: 400px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True      # Permite usar HTML e CSS personalizados
)

# =========================
# Cabeçalho principal
# =========================
st.title("🎮 Games Hub: Infos & Curiosidades")  # Título da página
st.caption(f"Data: {dt.date.today():%d/%m/%Y}")  # Mostra a data atual
st.write("Selecione um jogo para ver informações, destaques e curiosidades.")

# =========================
# Base de dados dos jogos
# =========================
# Dicionário com informações dos jogos (cada chave é um jogo)
games = {
    "Minecraft": {
        "lancamento": "2009",
        "genero": "Mundo aberto / Criativo",
        "curiosidades": [
            "Criado por Markus 'Notch' Persson.",
            "Mundos praticamente infinitos via geração procedural.",
            "Um dos jogos mais vendidos da história.",
        ],
        "detalhes": "Exploração e construção em mundos gerados por algoritmo.",
        "imagem": "https://i.pinimg.com/736x/5f/f0/e9/5ff0e997a4a8ba449056ed679660f4cc.jpg",
        "cor": "#8CC63F",
        "link": "https://clickjogos.com.br/minecraft/minecraft-oficial"
    },
    "The Legend of Zelda: Breath of the Wild": {
        "lancamento": "2017",
        "genero": "Aventura / Mundo aberto",
        "curiosidades": [
            "Exploração não linear revolucionou a série.",
            "Física e clima afetam a jogabilidade.",
            "Vencedor de múltiplos prêmios de Jogo do Ano.",
        ],
        "detalhes": "Mundo aberto com física integrada e puzzles variados.",
        "imagem": "https://i.pinimg.com/1200x/31/59/2d/31592dd53c1d4976a8d5cadfd3fd07c5.jpg",
        "cor": "#F5C242",
        "link": "https://www.nintendo.com/pt-br/store/products/the-legend-of-zelda-breath-of-the-wild-switch/"
    },
    "Fortnite": {
        "lancamento": "2017",
        "genero": "Battle Royale",
        "curiosidades": [
            "Eventos ao vivo dentro do jogo.",
            "Crossplay entre várias plataformas.",
            "Temporadas mudam mapa e gameplay.",
        ],
        "detalhes": "Batalhas de 100 jogadores, construção e eventos sazonais.",
        "imagem": "https://i.pinimg.com/736x/7e/e8/c4/7ee8c4361736ed806711ae99f7d6762c.jpg",
        "cor": "#4B8BF5",
        "link": "https://www.fortnite.com/"
    },
    "Roblox": {
        "lancamento": "2006",
        "genero": "Plataforma / UGC",
        "curiosidades": [
            "Usuários criam experiências e jogos.",
            "Economia interna com itens da comunidade.",
            "Muito usado para aprender lógica e game design.",
        ],
        "detalhes": "Plataforma UGC com inúmeras modalidades criadas pela comunidade.",
        "imagem": "https://i.pinimg.com/736x/a6/8c/0b/a68c0bc57047b77fa9c25cb0a9a0cebb.jpg",
        "cor": "#FF0000",
        "link": "https://www.roblox.com/"
    }
}

# =========================
# Sidebar (filtro lateral)
# =========================
st.sidebar.header("Escolha um jogo")  # Texto da sidebar
# Selectbox permite escolher um jogo
game = st.sidebar.selectbox("🎮 Jogos disponíveis", list(games.keys()))

# Pegamos as informações do jogo escolhido
info = games[game]

# =========================
# Card centralizado do jogo
# =========================
st.markdown(
    f"""
    <div class="card" style="background-color:{info['cor']}">
        <img src="{info['imagem']}" width="200">   <!-- Mostra a imagem -->
        <h2>{game}</h2>                            <!-- Nome do jogo -->
        <p><strong>Gênero:</strong> {info['genero']}</p>
        <p><strong>Lançamento:</strong> {info['lancamento']}</p>
        <a href="{info['link']}" target="_blank" style="color:white; text-decoration:underline;">
            🔗 Página oficial
        </a>
    </div>
    """,
    unsafe_allow_html=True  # Permite HTML dentro do Streamlit
)

# =========================
# Destaques e Curiosidades
# =========================
st.markdown("### 📝 Destaques")
st.write(info.get("detalhes", "Detalhes não disponíveis."))  # Mostra os detalhes do jogo

st.markdown("### ✨ Curiosidades")
for c in info["curiosidades"]:  # Lista todas as curiosidades
    st.write(f"- {c}")

# =========================
# Quiz de 10 perguntas
# =========================
st.markdown("---")
st.markdown("### ❓ Quiz de Games (10 Perguntas)")

# Perguntas do quiz: cada item tem pergunta, opções e resposta correta
quiz = [
    {"pergunta": "Qual jogo foi lançado primeiro?", "opcoes": ["Minecraft", "Fortnite", "Zelda BOTW", "Roblox"], "correta": "Roblox"},
    {"pergunta": "Qual jogo é exclusivo da Nintendo?", "opcoes": ["Fortnite", "Minecraft", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
    {"pergunta": "Qual desses jogos tem 'mundos infinitos'?", "opcoes": ["Roblox", "Minecraft", "Fortnite"], "correta": "Minecraft"},
    {"pergunta": "Qual é um Battle Royale?", "opcoes": ["Minecraft", "Zelda BOTW", "Fortnite"], "correta": "Fortnite"},
    {"pergunta": "Qual jogo permite criar experiências próprias?", "opcoes": ["Roblox", "Zelda BOTW", "Fortnite"], "correta": "Roblox"},
    {"pergunta": "Quem criou o Minecraft?", "opcoes": ["Markus 'Notch' Persson", "Shigeru Miyamoto", "Epic Games"], "correta": "Markus 'Notch' Persson"},
    {"pergunta": "Qual jogo tem física e clima afetando a jogabilidade?", "opcoes": ["Fortnite", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
    {"pergunta": "Qual desses é considerado um dos jogos mais vendidos da história?", "opcoes": ["Minecraft", "Fortnite", "Roblox"], "correta": "Minecraft"},
    {"pergunta": "Qual desses jogos tem temporadas que mudam o mapa?", "opcoes": ["Fortnite", "Roblox", "Zelda BOTW"], "correta": "Fortnite"},
    {"pergunta": "Qual jogo saiu em 2006?", "opcoes": ["Roblox", "Minecraft", "Zelda BOTW"], "correta": "Roblox"},
]

# Inicializa um dicionário de respostas no estado da sessão
if "respostas" not in st.session_state:
    st.session_state.respostas = {}

# Mostra cada pergunta com opções de resposta
for i, q in enumerate(quiz, 1):
    resposta = st.radio(f"Q{i}. {q['pergunta']}", q["opcoes"], key=f"q{i}")
    st.session_state.respostas[f"q{i}"] = resposta

# =========================
# Finalizar o quiz
# =========================
if st.button("📊 Finalizar Quiz"):
    score = 0  # Contador de acertos
    resultados_detalhados = []  # Lista para guardar feedback de cada questão

    # Verifica cada resposta
    for i, q in enumerate(quiz, 1):
        resposta = st.session_state.respostas[f"q{i}"]  # Resposta escolhida
        correta = q["correta"]  # Resposta certa

        if resposta == correta:
            score += 1
            resultados_detalhados.append(
                f"✅ Q{i}. {q['pergunta']} — Você respondeu **{resposta}** (Correto)"
            )
        else:
            resultados_detalhados.append(
                f"❌ Q{i}. {q['pergunta']} — Você respondeu **{resposta}**, mas o certo é **{correta}**"
            )

    # Mostra pontuação final
    st.success(f"Você acertou {score} de {len(quiz)} perguntas! 🎉")

    # Mostra barra de progresso proporcional aos acertos
    st.progress(score / len(quiz))

    # Gráfico de pizza mostrando acertos e erros
    resultados = {
        "Acertos": score,
        "Erros": len(quiz) - score
    }
    fig = px.pie(
        names=list(resultados.keys()),    # "Acertos" e "Erros"
        values=list(resultados.values()), # Quantidade de cada
        color=list(resultados.keys()),    # Cores baseadas nas categorias
        color_discrete_map={"Acertos": "green", "Erros": "red"},
        title="Resultado do Quiz"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Lista detalhada de respostas (acertos e erros)
    st.markdown("### 📋 Resultado detalhado")
    for r in resultados_detalhados:
        st.write(r)

# =========================
# Rodapé
# =========================
st.markdown("---")
st.caption("Games Hub em Streamlit — Quiz com pontuação, gráfico e feedback detalhado 🎮✨")