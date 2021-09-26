import ply.lex as lex
import sys

reserved = {
    'Alf': 'ALPHABET',
    'Common_Vertex': 'COMMON_VERTEX',
    'Start': 'START_VERTEX',
    'End': 'TERMINAL_VERTEX',
    'Edge': 'EDGE'
}

tokens = [
    'COMMA',
    'STR',
    'COLON'
] + list(reserved.values())


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_START_VERTEX = r'[a-zA-Z]+\(S\)'
t_TERMINAL_VERTEX = r'[a-zA-Z]+\(T\)'
t_COMMON_VERTEX = r'[a-z]+\(\)'
t_ALPHABET = r'\{[.*,]*.*\}'
t_COMMA = r'\,'
t_EDGE = r'\([a-zA-Z]+\, [a-zA-Z]+\)\{[\d,]*\d\}'
t_COLON = r'\:'
t_STR = r'Alf|Vertices|Edges|Start'
t_ignore = ' \t'

lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
