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
    r'".*"'
    t.value = t.value[1:-1]
    i = 0
    while i < len(t.value):
        if t.value[i] == '\\':
            if i == len(t.value) - 1:
                raise KeyError(t.value)
            n = t.value[i + 1]
            c = ''
            if n == '\\':
                c = '\\'
            elif n == 'n':
                c = '\n'
            elif n == 't':
                c = '\t'
            else:
                raise KeyError(t.value)
            t.value = t.value[:i] + c + t.value[i + 2:]
        i += 1
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
            try:
                tok = lexer.token()
                if not tok:
                    break
                out.write(str(tok) + '\n')
            except KeyError as e:
                print('syntax error: %s' %e)

if __name__ == '__main__':
    main()
