# ---------------------------------------------------
# Analisador lexico da linguagem D
# Imprime a sequencia de tokens de um arquivo fonte
#
# uso: python3 main.py [arquivo.d]
# ---------------------------------------------------
import os
import sys

from ttoken import TOKEN
from lexico import Lexico


def detectaCodificacao(caminho):
    # o fonte pode estar em utf-8 ou latin-1; latin-1 aceita qualquer byte
    # e serve de ultimo recurso
    with open(caminho, 'rb') as arq:
        dados = arq.read()
    try:
        dados.decode('utf-8')
        return 'utf-8'
    except UnicodeDecodeError:
        return 'latin-1'


def abreFonte(caminho):
    try:
        codificacao = detectaCodificacao(caminho)
        return open(caminho, 'r', encoding=codificacao)
    except OSError as erro:
        print(f'erro: nao foi possivel abrir "{caminho}": {erro.strerror}')
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
    else:
        # sem argumento, usa o fonte de demonstracao, se estiver presente
        caminho = 'testes/exemplo.d'
        if not os.path.exists(caminho):
            print('uso: python3 main.py <arquivo.d>')
            sys.exit(1)

    arqfonte = abreFonte(caminho)
    lexico = Lexico(arqfonte)
    arqfonte.close()

    tokenLido = lexico.getToken()
    while tokenLido[0] != TOKEN.eof:
        lexico.imprimeToken(tokenLido)
        tokenLido = lexico.getToken()
    lexico.imprimeToken(tokenLido)
