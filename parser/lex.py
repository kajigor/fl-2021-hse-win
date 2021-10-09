import ply.lex as lex
import sys

tokens = [
    'COMMA',
    'ALT',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'EQ',
    'RULENAME',
    'PLAINTEXT',
]


def t_PLAINTEXT(t):
    r'\'(\\\'|[^\'])+\''
    t.value = t.value[1:-1]
    return t


t_COMMA = r','
t_ALT = r'\|'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'\='
t_RULENAME = r'([^\[\]\(\)\{\}\=\|\\\']|\\\[|\\\]|\\\(|\\\)|\\\{|\\\}|\\\=|\\\||\\\\|\\\')+'
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
