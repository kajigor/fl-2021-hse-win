#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import ply.lex as lex
import argparse
import sys


reserved = {
    'vertices': 'VERTICES',
    'edges': 'EDGES',
    'from': 'FROM',
    'to': 'TO',
    'edge': 'EDGE',
    'start': 'START',
    'terminal': 'TERMINAL',
    'sink': 'SINK',
}

tokens = [
    'NUM',
    'ID',
    'EDGE_VALUE'
] + list(reserved.values())


def t_EDGE_VALUE(t):
    r'".*"'
    t.value = t.value[1:len(t.value) - 1]
    t.type = 'EDGE_VALUE'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value not in reserved:
        raise KeyError(t.value)
    t.type = reserved[t.value]
    return t


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', default=None)
    parser.add_argument('-l', '--log-file', default=sys.stderr)
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.input, 'r') as input_data:
        lexer = lex.lex()
        with open(args.output or args.input + '.out', 'w+') as result:
            for line in input_data:
                lexer.input(line)
                while True:
                    try:
                        tok = lexer.token()
                        if not tok:
                            break
                        result.write(str(tok) + '\n')
                    except KeyError as key_error:
                        result.write('Unknown sequence {}\n'.format(key_error))


if __name__ == '__main__':
    main()
