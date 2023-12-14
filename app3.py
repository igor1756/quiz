from flask import Flask, render_template, request

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

# Rota para a página principal
@app.route('/', methods=['GET', 'POST'])
def pagina_principal():
    if request.method == 'POST':
        respostas_jogador = {}
        for questao in questoes_e_respostas:
            respostas_jogador[questao['pergunta']] = request.form.get(questao['pergunta'])

        # Agora você tem as respostas do jogador no dicionário respostas_jogador
        # Você pode comparar com as respostas corretas e tomar as ações necessárias

    return render_template('pagina.html', questoes_e_respostas=questoes_e_respostas)

# Rota para processar as respostas do jogador
@app.route('/responder', methods=['POST'])
def processar_respostas():
    respostas_jogador = {}
    for questao in questoes_e_respostas:
        respostas_jogador[questao['pergunta']] = request.form.get(questao['pergunta'])

    # Agora você pode comparar as respostas do jogador com as respostas corretas e tomar as ações necessárias
    # Exemplo de verificação simples:
    for questao in questoes_e_respostas:
        pergunta = questao['pergunta']
        resposta_correta = questao['resposta_correta']
        resposta_jogador = respostas_jogador.get(pergunta)

        if resposta_jogador == resposta_correta:
            print(f"O jogador acertou a pergunta: {pergunta}")
        else:
            print(f"O jogador errou a pergunta: {pergunta}")

    return "Respostas processadas com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
