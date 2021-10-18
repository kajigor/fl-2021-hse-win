import ply.lex as lex
import sys

spec_symbols = {'=', '\'', '(', ')', '[', ']', '{', '}', '|', 'n', '#', ','}
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
    'COMMENT'
]


def t_PLAINTEXT(t):
    r'\'(\\\'|[^\'])+\''
    t.value = t.value[1:-1]
    s = ""
    for i in range(len(t.value)):
        if i > 0 and t.value[i - 1] == '\\' and t.value[i] in spec_symbols:
            if t.value[i - 1] == '\\' and t.value[i] == 'n':
                s += '\n'
            else:
                s += t.value[i]
        elif t.value[i] != '\\':
            s += t.value[i]
    t.value = s
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
t_RULENAME = r'([^,\[\]\(\)\{\}\=\|\\\'\#]|\\,|\\\#|\\\[|\\\]|\\\(|\\\)|\\\{|\\\}|\\\=|\\\||\\\\|\\\')+'
t_COMMENT = r'\#.*$'
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
# fout = open(sys.argv[1] + '.out', 'w')
while True:
    tok = lexer.token()
    if not tok:
        break
    print(str(tok))
#     fout.write(str(tok))
#     fout.write('\n')
# fout.close()
