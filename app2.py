from flask import Flask, redirect, render_template, request, url_for
import csv
import random
import time
from aplic.models.Questao import Questao

app = Flask(__name__, template_folder='aplic/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game',methods=['POST','GET'])
def game():
    try:
        player_name = request.form['player_name']
    except:
        player_name = 'X'
    # return render_template('game.html', question=question, player_name=player_name)
    #return render_template('result.html', player_name=player_name, score=score, high_score=high_score)
    return redirect(url_for('begin',player_name=player_name))

@app.route('/begin',methods=['POST','GET'])
def begin(player_name):
    question = load_question()
    render_template('game.html', question=question, player_name=player_name)

@app.route('/computes',methods=['POST','GET'])
def computes():
    # resposta_jogador =
    pass
    
def load_question():
    # TODO: Carregue as perguntas do arquivo CSV
    # Retorne uma lista de perguntas (cada pergunta é um dicionário)
    #return Questao.PRIMEIRA.value
    texto_pergunta = Questao.SEGUNDA.value.get('texto')
    return texto_pergunta

@app.route('/verify', methods=['POST'])
def verify():
    # Implemente a lógica do jogo aqui
    form = request.form
    jogador = form.get('jogador')
    score=0
    resposta = form.get('alternativaB')
    high_score = update_high_score()
    print(form)
    print(resposta)
    return render_template('result.html', player_name=jogador, high_score=high_score, score=score )

def update_high_score(player_name='Bichão', score=9.9):
    # Atualize a pontuação mais alta se necessário
    # Retorne a nova pontuação mais alta
    return f'{player_name}, {score}'


if __name__ == '__main__':
    app.run(debug=True)
