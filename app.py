from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='aplic/templates')

# Lista de questões e respostas
questoes_e_respostas = [
    {
        'pergunta': 'Qual é a capital do Brasil?',
        'alternativas': ['Rio de Janeiro', 'Brasília', 'São Paulo', 'Salvador'],
        'resposta_correta': 'Brasília'
    },
    {
        'pergunta': 'Quanto é 2 + 2?',
        'alternativas': ['3', '4', '5', '6'],
        'resposta_correta': '4'
    },
    # Adicione mais questões conforme necessário
]

# Índice da pergunta atual
pergunta_atual = 0

# Rota para a página principal
@app.route('/', methods=['GET', 'POST'])
def pagina_principal():
    global pergunta_atual

    if request.method == 'POST':
        # Processar resposta do jogador
        pergunta = questoes_e_respostas[pergunta_atual]['pergunta']
        resposta_correta = questoes_e_respostas[pergunta_atual]['resposta_correta']
        resposta_jogador = request.form.get('resposta_jogador')

        # Realizar verificações, imprimir mensagens, etc.
        if resposta_jogador == resposta_correta:
            print(f"O jogador acertou a pergunta: {pergunta}")
        else:
            print(f"O jogador errou a pergunta: {pergunta}")

        # Avançar para a próxima pergunta
        pergunta_atual += 1

        # Se ainda houver perguntas, redirecionar para a próxima pergunta
        if pergunta_atual < len(questoes_e_respostas):
            return redirect(url_for('pagina_principal'))
        else:
            # Se todas as perguntas foram respondidas, redirecionar para a página de conclusão
            return redirect(url_for('conclusao'))

    # Se a pergunta_atual for válida, exibir a pergunta
    if 0 <= pergunta_atual < len(questoes_e_respostas):
        return render_template('pagina.html', pergunta_atual=pergunta_atual, questao=questoes_e_respostas[pergunta_atual])

    # Se pergunta_atual for inválido, redirecionar para a página de conclusão
    return redirect(url_for('conclusao'))

# Rota para a página de conclusão
@app.route('/conclusao', methods=['GET', 'POST'])
def conclusao():
    global pergunta_atual

    if request.method == 'POST' and 'reiniciar_jogo' in request.form:
        # Reiniciar o jogo
        pergunta_atual = 0
        return redirect(url_for('pagina_principal'))

    # Aqui você pode exibir uma mensagem de conclusão, pontuação, etc.
    return render_template('conclusao.html')

if __name__ == '__main__':
    app.run(debug=True)
