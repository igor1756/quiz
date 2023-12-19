import os
import json

class Senador():
    
    subdiretorio = 'dados'
    arquivo = 'senadores_tratado.json'

    # vai funcionar independentemente de onde senador.py for chamado
    arquivo_json = os.path.join(os.path.dirname(__file__), '..', subdiretorio, arquivo)

    def __init__():
        pass

    @staticmethod
    def get_all():
        try:
            with open(Senador.arquivo_json,'r') as file:
                dados = json.load(file)
                return dados
        except FileNotFoundError:
            print(f"Arquivo '{Senador.arquivo_json}' não encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o conteúdo do arquivo '{Senador.arquivo_json}'.")
            return None

    @staticmethod
    def get_qtde_senadores_por_partido():
        # partidos = []
        contagem_por_partido = {}
        for i in Senador.get_all():
            partido = i.get('partido')
            # partidos.append(partido)
            contagem_por_partido[partido] = contagem_por_partido.get(partido, 0) + 1
            # dict.items() obtem uma lista de tuplas
            # sorted eh um metodo builtin parametros os itens do dict, a chave da ordenacao eh a qtde e descrescente
            contagem_ordenada = dict(sorted(contagem_por_partido.items(), key=lambda item: item[1], reverse=True))
        return contagem_ordenada

# teste
# if __name__ == '__main__':
#     # Teste do método get_all() fora do bloco da classe
#     dados_pessoais = Senador.get_qtde_senadores_por_partido()
#     print(dados_pessoais)