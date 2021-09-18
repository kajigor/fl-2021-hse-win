import ply.lex as lex
import sys

reserved = {
  'alphabet': 'ALPHABET',
  'states': 'STATES',
  'terminal': 'TERMINAL',
  'state': 'STATE'
}

tokens = [
  'NUM',
  'COMMA',
  'ALPHABET_SYMBOL',
  'ARROW',
  'VARIABLE'
] + list(reserved.values())


def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t


t_ignore = ' \t'
t_COMMA = r'\/\/.*'
t_ALPHABET_SYMBOL = r'"(?:[^\\"]|\\.)*"'
t_VARIABLE = r'[A-Za-z][_0-9A-Za-z]*'
t_ARROW = r'--->'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(sys.argv[1])

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
