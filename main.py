import ply.lex as lex
import sys

reserved = {
  'start': 'START',
  'terminal': 'TERMINAL',
  '->': 'TRANSITION'
}

tokens = [
  'NUM',
  'NAME',
  'TRANSITION_NAME'
] + list(reserved.values())

def t_NAME(t):
  r'[q][0-9]+'
  t.type = reserved.get(t.value, 'NAME')
  return t


def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

def t_TRANSITION_NAME(t):
  r'[a-z_A-Z_0-9_]+'
  t.type = reserved.get(t.value, 'TRANSITION_NAME')
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(''.join(open(sys.argv[1]).readlines()))

output = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  output.write(str(tok) + '\n')