import ply.lex as lex
import sys

reserved = {
  'vertex': 'VERTEX',
  'edge': 'EDGE',
  'alphabet': 'ALPHABET',
  'T': 'TRUE',
  'F': 'FALSE',
}

tokens = [
  'STR',
  'SEMICOLON',
  'NAME',
  'COMMA',
  'CURLY_BRAKETS_open',
  'CURLY_BRAKETS_close',
  # 'NUM'
] + list(reserved.values())

def t_STR(t):
  r'[A-Za-z_][A-Za-z_0-9]*'
  t.type = reserved.get(t.value, 'STR')
  return t

def t_NAME(t):
  r'\'(?:[^\\\']|\\.)*\''
  t.value = t.value[1 : -1]
  t.type = reserved.get(t.value, 'NAME')
  return t

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_CURLY_BRAKETS_open = r'\{'
t_CURLY_BRAKETS_close = r'\}'

# def t_NUM(t):
#   r'[0-9]+'
#   t.value = int(t.value)
#   return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

# lexer.input(open(sys.argv[1], 'r').read())
# sys.stdout = open(sys.argv[1] + '.out', 'w')
#
# while True:
#   tok = lexer.token()
#   if not tok:
#     break
#   print(tok)