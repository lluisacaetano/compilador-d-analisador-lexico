# Analisador léxico da linguagem D

Primeira fase do compilador: lê um `.d` e devolve a sequência de tokens.

## Arquivos
- `ttoken.py` — enum `TOKEN`, `msg()` (nome do token) e `reservada()` (palavra reservada / função primitiva / ident).
- `lexico.py` — classe `Lexico` com o autômato (`getToken()` devolve `(token, lexema, linha, coluna)`).
- `main.py` — programa de teste; imprime todos os tokens até o `<eof>`.
- `testes/exemplo.d` — programa válido que exercita todos os tokens.
- `testes/erros.d` — erros léxicos propositais.

## Rodar
```
cd compilador-d/analisador-lexico
python3 main.py testes/exemplo.d
python3 main.py testes/erros.d
```
