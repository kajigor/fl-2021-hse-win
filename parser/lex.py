# import ply.lex as lex
# import sys

# reserved = {
#   'if': 'IF',
#   'then': 'THEN',
#   'else': 'ELSE'
# }
#
# tokens = [
#   'NUM',
#   'PLUS',
#   'MULT',
#   'ID',
#   'LBR',
#   'RBR'
# ] + list(reserved.values())
#
# def t_ID(t):
#   r'[a-z_][a-z_0-9]*'
#   t.type = reserved.get(t.value, 'ID')
#   return t
#
# def t_NUM(t):
#   r'[0-9]+'
#   t.value = int(t.value)
#   return t
#
# t_PLUS = r'\+'
# t_MULT = r'\*'
# t_LBR = r'\('
# t_RBR = r'\)'
#
# t_ignore = ' \t'
#
# def t_newline(t):
#   r'\n+'
#   t.lexer.lineno += len(t.value)
#
# def t_error(t):
#   print("Illegal character '%s'" % t.value[0])
#   t.lexer.skip(1)
#
# lexer = lex.lex()

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
# lexer.input(open(sys.argv[1], 'r').read())

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

# lexer.input(sys.argv[1])

#while True: 
#  r'\+' 
#  13
#  tok = lexer.token() 
#  if not tok: 
#    break
#  print(tok)
