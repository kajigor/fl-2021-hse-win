import ply.lex as lex
import sys

reserved = {
    'Terminal': 'TERMINAL',
    'Sigma': 'SIGMA',
    'Start': 'START',
    'Q': 'STATES',
    'Delta': 'DELTA'
}

tokens = [
             'NUM',
             'ARRFUNC',
             'SEP',
             'UNEXPECTED_ID',
             'OPEN_BR',
             'CLOSED_BR'
         ] + list(reserved.values())


def t_ID(t):
    r'[A-Z][a-z_0-9]*'
    t.type = reserved.get(t.value, 'UNEXPECTED_ID')
    return t


def t_NUM(t):
    r'([01]{8})+'
    chars = ['0b' + t.value[i:i + 8] for i in range(0, len(t.value) - 7, 8)]
    value = ""
    for i in chars:
        value += chr(int(i, 2))
    t.value = value
    return t


t_ARRFUNC = r'->'
t_SEP = r','
t_OPEN_BR = r'\('
t_CLOSED_BR = r'\)'
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
fin = open(sys.argv[1], 'r')
lexer.input(fin.read())
fin.close()
fout = open(sys.argv[1] + '.out', 'w')
while True:
    tok = lexer.token()
    if not tok:
        break
    fout.write(str(tok))
    fout.write('\n')
fout.close()
