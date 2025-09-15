# # # Mostra cada pergunta com opções de resposta e os erros e acertos em formas de gráfico, ai usamos o import plotly express as px que gera gáficos
# # Mostra cada pergunta com opções de resposta
# for i, q in enumerate(quiz, 1):
#     resposta = st.radio(f"Q{i}. {q['pergunta']}", q["opcoes"], key=f"q{i}")
#     st.session_state.respostas[f"q{i}"] = resposta

# # =========================
# # Finalizar o quiz
# # =========================
# if st.button("📊 Finalizar Quiz"):
#     score = 0  # Contador de acertos
#     resultados_detalhados = []  # Lista para guardar feedback de cada questão

#     # Verifica cada resposta
#     for i, q in enumerate(quiz, 1):
#         resposta = st.session_state.respostas[f"q{i}"]  # Resposta escolhida
#         correta = q["correta"]  # Resposta certa

#         if resposta == correta:
#             score += 1
#             resultados_detalhados.append(
#                 f"✅ Q{i}. {q['pergunta']} — Você respondeu **{resposta}** (Correto)"
#             )
#         else:
#             resultados_detalhados.append(
#                 f"❌ Q{i}. {q['pergunta']} — Você respondeu **{resposta}**, mas o certo é **{correta}**"
#             )

#     # Mostra pontuação final
#     st.success(f"Você acertou {score} de {len(quiz)} perguntas! 🎉")

#     # Mostra barra de progresso proporcional aos acertos
#     st.progress(score / len(quiz))

#     # Gráfico de pizza mostrando acertos e erros
#     resultados = {
#         "Acertos": score,
#         "Erros": len(quiz) - score
#     }
#     fig = px.pie(
#         names=list(resultados.keys()),    # "Acertos" e "Erros"
#         values=list(resultados.values()), # Quantidade de cada
#         color=list(resultados.keys()),    # Cores baseadas nas categorias
#         color_discrete_map={"Acertos": "green", "Erros": "red"},
#         title="Resultado do Quiz"
#     )
#     st.plotly_chart(fig, use_container_width=True)

#     # Lista detalhada de respostas (acertos e erros)
#     st.markdown("### 📋 Resultado detalhado")
#     for r in resultados_detalhados:
#         st.write(r)

# # =========================
# # Rodapé
# # =========================
# st.markdown("---")
# st.caption("Games Hub em Streamlit — Quiz com pontuação, gráfico e feedback detalhado 🎮✨")