import ply.lex as lex
import sys

reserved = {
  'Q': 'Q',
  'start': 'START',
  'T': 'T',
  'function': 'FUNCTION'
}

tokens = [
  'NUM',
  'PARENTHESIS',
  'POINT',
  'COLON'
] + list(reserved.values())

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[A-Za-z][a-z]*'
  t.type = reserved.get(t.value, 'ID')
  return t

t_PARENTHESIS = r'\(|\)'
t_POINT = r'\.'
t_COLON = r':'
t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

#input from file
fin = open(sys.argv[1], 'r').read()
lexer.input(fin)
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)