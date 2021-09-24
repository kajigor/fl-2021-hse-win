import ply.lex as lex
import sys

tokens = [
    'SYMBOL',
    'VERTEX',
    'ARROW',
    'BRACKETS'
]

t_VERTEX = r'0S | ([1-9]+(T|M))'
t_ARROW = r'\-'
t_BRACKETS = r'\[ | \]'

def t_SYMBOL(t):
    r'[0-9]+\s'
    t.value = int(t.value)
    return t

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