import ply.lex as lex
import sys

reserved = {
    'Sigma': 'SIGMA',
    'T': 'TERMINAL',
    'q0': 'START_STATE',
    'Q': 'STATES',
    'delta': 'DELTA'
}

tokens = [
             'NUM',
             'ID',
             'COMMA',
             'COLON',
             'OPEN_BR',
             'CLOSED_BR',
             'DASH'
         ] + list(reserved.values())


def t_ID(t):
    r'[a-z_][a-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t




t_COMMA = r','
t_COLON = r':'
t_OPEN_BR = r'\('
t_CLOSED_BR = r'\)'
t_DASH = r'--'
t_TERMINAL = r'T'
t_SIGMA = r'Sigma'
t_START_STATE = r'q0'
t_STATES = r'Q'
t_DELTA = r'delta'
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
