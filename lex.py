import ply.lex as lex
import sys

reserved = {
  'to' : 'TO',
  'by' : 'BY',
  'terminal' : 'TERMINAL'
}

tokens = [
  'NUM',
  'CHAR'
] + list(reserved.values())

def t_NUM(t):
  r'[0-9]+\s'
  t.value = int(t.value)
  return t

def t_CHAR(t):
  r'[^\s]+'
  t.type = reserved.get(t.value, 'CHAR')
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

input = open(sys.argv[1], "r")
data = input.read()
input.close()

lexer.input(data)

output = open(sys.argv[1] + ".out", "w")

while True:
  tok = lexer.token()
  if not tok:
    break
  output.write(str(tok))
  output.write('\n')

output.close()