#!/usr/bin/env python2

import ply.lex as lex
import sys

tokens = [
  'NUM',
  'WORD',
]

def t_NUM(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_WORD(t):
    r'\".*\"' # as you might guess, this is not what I described, but it did not work to come up with a regexp in 5 minutes.
    t.value = t.value[1:-1]
    return t;

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def main():

    if len(sys.argv) != 2:
        print("Usage: %s <filename>" %sys.argv[0])
        return

    lexer = lex.lex()
    
    try:
        with open(sys.argv[1], 'r') as inp:
            lexer.input(inp.read())
    except:
        print('can\'t open %s file' %sys.argv[1])
        return
    with open(sys.argv[1] + '.out', 'w') as out:
        while True:
          tok = lexer.token()
          if not tok:
            break
          out.write(str(tok) + '\n')

if __name__ == '__main__':
    main()
