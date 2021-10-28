import ply.lex as lex
import sys
from termcolor import colored

spec_symbols = {'=', '\'', '(', ')', '[', ']', '{', '}', '|', 'n', '#', ','}
ERROR = False
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
    'MULTILINE_COMMENT',
    "INDENT"
]


def t_INDENT(t):
    r'(\ \ \ \ )+'
    t.value = len(t.value) // 4
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


def t_MULTILINE_COMMENT(t):
    r'((/\*)[^(/\*)(\*/)]*(\*/)?)|(\*/)?[^(/\*)(\*/)]*(\*/)'
    if (t_MULTILINE_COMMENT.first_token is None):
        t_MULTILINE_COMMENT.first_token = t
    t_MULTILINE_COMMENT.value += t.value
    t.lexer.lineno += len(t.value.split('\n')) - 1
    if (t.value[0] == '/'):
        t_MULTILINE_COMMENT.counter += 1
    if (t.value[-1] == '/'):
        t_MULTILINE_COMMENT.counter -= 1
    if t_MULTILINE_COMMENT.counter < 0:
        global ERROR
        t_MULTILINE_COMMENT.counter = 0
        ERROR = True
        print(colored("missing pairing /* for */ in line {}".format(t.lexer.lineno), "red"))
    if t_MULTILINE_COMMENT.counter == 0:
        t.value = t_MULTILINE_COMMENT.value
        t_MULTILINE_COMMENT.value = ""
        t.lexpos = t_MULTILINE_COMMENT.first_token.lexpos
        t.lineno = t_MULTILINE_COMMENT.first_token.lineno
        t_MULTILINE_COMMENT.first_token = None
        return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_RULENAME(t):
    r'([^,(/\*)(\*/)\[\]\(\)\{\}\=\|\\\'\#]|\\,|\\\#|\\\[|\\\]|\\\(|\\\)|\\\{|\\\}|\\\=|\\\||\\\\|\\\')+'
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


def t_error(t):
    print(colored("Illegal character '%s'" % t.value[0], "red"))
    global ERROR
    ERROR = True
    t.lexer.skip(1)


lexer = None


def build_lex():
    global lexer
    t_MULTILINE_COMMENT.counter = 0
    t_MULTILINE_COMMENT.value = ""
    t_MULTILINE_COMMENT.first_token = None
    lexer = lex.lex()


def do_lex():
    fin = open(sys.argv[1], 'r')
    lexer.input(fin.read())
    fin.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
    if (t_MULTILINE_COMMENT.value != ""):
        print(colored("missing pairing */ for /* in line {}".format(t_MULTILINE_COMMENT.first_token.lineno), "red"))
        global ERROR
        ERROR = True


build_lex()
do_lex()
if (ERROR):
    exit(1)
