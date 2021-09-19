import ply.lex as lex
import sys

reserved = {
    'Alphabet': 'ALPHABET',
    'Startvertex': 'STARTVERTEX',
    'Edge': 'EDGE',
    'States': 'STATES',
    'Terminalvertexes': 'TERMINALVERTEXES'
}

tokens = [
             'NUM',
             'UNEXPECTED_ID',
         ] + list(reserved.values())


def t_ID(t):
    r'[A-Z][a-z_0-9]*'
    t.type = reserved.get(t.value, 'UNEXPECTED_ID')
    return t


def t_NUM(t):
    r'([01]{8})+'
    c = ['0b' + t.value[i:i + 8] for i in range(0, len(t.value) - 7, 8)]
    value = ""
    for i in c:
        value += chr(int(i, 2))
    t.value = value
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
with open(sys.argv[1], 'r') as file_in:
    lexer.input(file_in.read())
    file_out = open(sys.argv[1] + '.out', 'w')
    while True:
        token = lexer.token()
        if not token:
            break
        file_out.write(str(token))
        file_out.write('\n')
    file_out.close()
