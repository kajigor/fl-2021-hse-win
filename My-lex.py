import ply.lex as lex
import sys

tokens = [
    'NUM',
    'POINT',
    'NORMAL',
    'TERMINAL',
    'ARROW',
    'COMMA',
    'ALPHABET',
    'QUOTES'
]


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_ALPHABET(t):
    # мы матчим всё, что находится между ковычками,
    # не матчим сами ковычки, и, чтобы понимать,
    # что у нас слеш не является символом,
    # экранируем его при выводе. Запредим использовать
    # слеши в алфавите данного нам автоомата
    r'"(?:[^\\"]|\\.)*"'
    t.value = t.value[1 : -1]
    return t


t_QUOTES = r'\"|\\\"'
t_POINT = r'\.'
t_NORMAL = r'\#'
t_TERMINAL = r'\$'
t_ARROW = r'->'
t_COMMA = r','

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
