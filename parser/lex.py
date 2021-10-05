import sys
import ply.lex as lex

reserved = {
    'States': 'STATES',
    'Start': 'START',
    'End': 'END',
    'Alphabet': 'ALPHABET',
    'Function': 'FUNCTION'
}

tokens = [
             # 'COMMENT',
             'TRANSFER',
             'STATE',
             'EQUAL',
             'BRACKET',
             'SEMICOLON',
         ] + list(reserved.values())

t_SEMICOLON = r';'
t_BRACKET = r'({|})'
t_EQUAL = r'='
t_ignore = ' '


# def t_COMMENT(t):
#     r'//.*\n'
#     t.value = t.value[2:]
#     return t


def t_STATE(t):
    r'[^\s={};"/]+(,)?(\s)?'
    t.value = t.value[:-1]
    if (t.value[-1] == ','):
        t.value = t.value[:-1]
    t.type = reserved.get(t.value, 'STATE')
    return t


def t_TRANSFER(t):
    r'"([^"\\]|\\(")?)+"(,)?\s'
    t.value = t.value[:-1]
    if (t.value[-1] == ','):
        t.value = t.value[:-1]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
