#  colocamos mais 6 jogos para ficar mais completo
# =========================
# Base de dados dos jogos (atualizada com mais 6 jogos)
# =========================
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
    },
    # Novos jogos adicionados
    "Grand Theft Auto V": {
        "lancamento": "2013",
        "genero": "Ação / Mundo aberto",
        "curiosidades": [
            "Primeiro GTA com três protagonistas jogáveis.",
            "Online com atualizações constantes.",
            "Um dos jogos mais rentáveis da história.",
        ],
        "detalhes": "História cinematográfica em Los Santos, com modo online massivo.",
        "imagem": "https://i.pinimg.com/736x/cb/53/16/cb5316cfc3b5af1347e98a23ef7e2415.jpg",
        "cor": "#2C3E50",
        "link": "https://www.rockstargames.com/gta-v"
    },
    "The Witcher 3: Wild Hunt": {
        "lancamento": "2015",
        "genero": "RPG",
        "curiosidades": [
            "Baseado nos livros de Andrzej Sapkowski.",
            "Mundo aberto enorme e detalhado.",
            "DLCs são consideradas entre as melhores já feitas.",
        ],
        "detalhes": "Aventura de Geralt em busca de Ciri, com escolhas que afetam o mundo.",
        "imagem": "https://i.pinimg.com/736x/9f/9e/6e/9f9e6e46f7b779dd3f28bb0a7d3fbbd0.jpg",
        "cor": "#6C3483",
        "link": "https://thewitcher.com/en/witcher3"
    },
    "League of Legends": {
        "lancamento": "2009",
        "genero": "MOBA",
        "curiosidades": [
            "Um dos maiores eSports do mundo.",
            "Base para séries como Arcane.",
            "Mais de 160 campeões jogáveis.",
        ],
        "detalhes": "MOBA 5v5 com campeões e estratégias infinitas.",
        "imagem": "https://i.pinimg.com/736x/23/15/b9/2315b9aa92a2aa815a7b56a8bfb54644.jpg",
        "cor": "#1F618D",
        "link": "https://www.leagueoflegends.com/"
    },
    "Counter-Strike: Global Offensive": {
        "lancamento": "2012",
        "genero": "FPS",
        "curiosidades": [
            "Popularizou o mercado de skins raras.",
            "Base dos eSports de tiro competitivo.",
            "Tem versão atualizada: CS2.",
        ],
        "detalhes": "FPS tático de times terroristas contra contraterroristas.",
        "imagem": "https://i.pinimg.com/736x/26/32/5f/26325fa157e3407983519f9e30130487.jpg",
        "cor": "#34495E",
        "link": "https://blog.counter-strike.net/"
    },
    "Among Us": {
        "lancamento": "2018",
        "genero": "Dedução Social",
        "curiosidades": [
            "Explodiu em popularidade em 2020.",
            "Jogadores devem descobrir impostores.",
            "Estilo simples, mas viciante.",
        ],
        "detalhes": "Tripulantes vs impostores em partidas de dedução social.",
        "imagem": "https://i.pinimg.com/736x/73/f5/27/73f5274207c4427110402df29d3a563a.jpg",
        "cor": "#E74C3C",
        "link": "https://innersloth.com/gameAmongUs.php"
    },
    "Overwatch": {
        "lancamento": "2016",
        "genero": "Hero Shooter",
        "curiosidades": [
            "Cada herói tem habilidades únicas.",
            "Popularizou o gênero hero shooter.",
            "Recebeu sequência: Overwatch 2.",
        ],
        "detalhes": "FPS baseado em heróis com habilidades especiais.",
        "imagem": "https://i.pinimg.com/736x/67/fc/41/67fc419ac30a9dffef5b1ec160494c6d.jpg",
        "cor": "#F39C12",
        "link": "https://overwatch.blizzard.com/"
    },
    "Elden Ring": {
        "lancamento": "2022",
        "genero": "RPG / Mundo Aberto",
        "curiosidades": [
            "Criado em parceria com George R. R. Martin.",
            "Exploração livre em mundo sombrio.",
            "Vencedor de Jogo do Ano em 2022.",
        ],
        "detalhes": "RPG desafiador em mundo aberto interconectado.",
        "imagem": "https://i.pinimg.com/736x/40/9e/61/409e61ea09798f633ea80466b8bb9f53.jpg",
        "cor": "#145A32",
        "link": "https://en.bandainamcoent.eu/elden-ring/elden-ring"
    },
    "God of War (2018)": {
        "lancamento": "2018",
        "genero": "Ação / Aventura",
        "curiosidades": [
            "Reinvenção da franquia.",
            "Focado na mitologia nórdica.",
            "Recebeu sequência Ragnarok em 2022.",
        ],
        "detalhes": "Kratos e Atreus em jornada pela mitologia nórdica.",
        "imagem": "https://i.pinimg.com/736x/9d/16/8a/9d168a023221c1b78f5d8f41cf0c7f71.jpg",
        "cor": "#5DADE2",
        "link": "https://www.playstation.com/pt-br/games/god-of-war/"
    },
    "Pokémon Scarlet & Violet": {
        "lancamento": "2022",
        "genero": "RPG / Aventura",
        "curiosidades": [
            "Primeiro Pokémon totalmente em mundo aberto.",
            "Apresenta a região de Paldea.",
            "Introduziu os fenômenos Terastal.",
        ],
        "detalhes": "Exploração livre na região de Paldea com novas mecânicas.",
        "imagem": "https://i.pinimg.com/736x/ae/ea/3f/aeea3f0c96d75a6d70889a31f4f2a4f1.jpg",
        "cor": "#AF7AC5",
        "link": "https://scarletviolet.pokemon.com/"
    }
}