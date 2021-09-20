import ply.lex as lex
import sys

tokens = [
    'NUM',
    'LETTER',
    'ARROW',
    'BRACKETS'
]


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

t_LETTER = r'[a-z, A-Z]+'
t_ARROW = r'\-'
t_BRACKETS = r'\[ | \]'

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