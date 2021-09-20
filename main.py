import ply.lex as lex
import sys

reserved = {
  'alphabet': 'ALPHABET',
  'start': 'START',
  'terminal': 'TERMINAL',
  'with': 'WITH'
}

tokens = [
  'VERTEX',
  'WORD',
  'KEYWORD'
] + list(reserved.values())

def t_KEYWORD(t):
  r'(alphabet|start|terminal|with)'
  t.type = reserved.get(t.value, 'KEYWORD')
  return t

def t_WORD(t):
  r'([0-9][0-9_]*[0-9]|[0-9])'
  t.value = t.value
  return t

def t_VERTEX(t):
  r'q[0-9]+'
  t.value = t.value
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Wrong input")
  exit(1)

lexer = lex.lex()

try:
  lexer.input(''.join(open(sys.argv[1]).readlines()))
except:
  print("Unable to open file")
  exit(1)

output = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  output.write(str(tok) + '\n')

