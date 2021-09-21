import ply.lex as lex
import sys

reserved = {
  '{': 'OPENBR',
  '}': 'CLOSEBR'
}

tokens = [	
  'NUM',
  'WRONG_ID'
] + list(reserved.values())


def t_ID(t):
  r'[{}]'
  t.type = reserved.get(t.value, 'WRONG_ID')
  return t


def t_NUM(t):
  r'[0-9]{3}'
  return t

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
