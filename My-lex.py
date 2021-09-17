import ply.lex as lex
import sys

tokens = [
    'NUM',
    'POINT',
    'SHARP',
    'DOLLAR',
    'ARROW',
    'COMMA',
    'QUOTES'
]


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


t_POINT = r'\.'
t_SHARP = r'\#'
t_DOLLAR = r'\$'
t_ARROW = r'->'
t_QUOTES = r'\"'

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
