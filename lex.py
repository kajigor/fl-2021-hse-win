import ply.lex as lex
import sys

reserved = {
    'word:': 'INPUT_WORD',
    'start': 'START',
    'terminal': 'TERMINAL',
    'transition': 'TRANSITION'
}

tokens = [
             'ARROW',
             'NUMBER',
             'UNEXPECTED_ID',
             'OPEN_BRACKET_ROUND',
             'CLOSE_BRACKET_ROUND',
             'OPEN_BRACKET_FIGURE',
             'CLOSE_BRACKET_FIGURE',
             'OPEN_BRACKET_SQUARE',
             'CLOSE_BRACKET_SQUARE',
             'VERTEX_NAME',
             'WORD',
             'COMMA'
         ] + list(reserved.values())


def t_WORD(t):
    r'([0-9][0-9A-F]~)*[0-9][0-9A-F]'
    return t


def t_VERTEX_NAME(t):
    r'[a-z]+[0-9]+'
    return t


def t_ID(t):
    r'[a-z_0-9]+:*'
    t.type = reserved.get(t.value, 'UNEXPECTED_ID')
    return t


t_ARROW = r'->'
t_OPEN_BRACKET_ROUND = r'\('
t_CLOSE_BRACKET_ROUND = r'\)'
t_OPEN_BRACKET_FIGURE = r'\{'
t_CLOSE_BRACKET_FIGURE = r'\}'
t_OPEN_BRACKET_SQUARE = r'\['
t_CLOSE_BRACKET_SQUARE = r'\]'
t_COMMA = r'\,'

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
