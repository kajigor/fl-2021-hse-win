import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}

tokens = [
             'NUM',
             'PLUS',
             'MULT',
             'ID'
         ] + list(reserved.values())


def t_ID(t):
    r'[a-z_][a-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


t_PLUS = r'\+'
t_MULT = r'\*'

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

infile = open(sys.argv[1], "r")
x = infile.readline()
lexer.input(infile.read())

outfile = open(sys.argv[1] + ".out", "w")
# sys.stdout = outfile

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
