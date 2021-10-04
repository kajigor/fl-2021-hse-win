import ply.lex as lex
import sys
import re

reserved = {
    'Alf': 'ALPHABET',
    'Common_Vertex': 'COMMON_VERTEX',
    'Start': 'START_VERTEX',
    'Ends': 'TERMINAL_VERTEX',
    'Edge': 'EDGE'
}

tokens = [
    'STR'
         ] + list(reserved.values())
alphabet = {}
edges = []
ends = []
start_vertex = -1
vertices = []

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Incorrect input format '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ALPHABET(t):
    r"""Alf:\s\{[.*,]*.*\}"""
    tmp = t.value[6:-1]
    flag = True
    j = int(0)
    for i in tmp:
        if i == '\\':
            flag = False
            continue
        if i == ',' or i == '{' or i == '}' or i == '(' or i == ')':
            if not flag:
                alphabet[i] = j
                j += 1
                flag = True
        else:
            alphabet[i] = j
            j += 1
    return t


def t_START_VERTEX(t):
    r"""Start:\s[a-zA-Z]+\(S\)"""
    tmp = t.value[7:-3]
    global start_vertex
    if tmp:
        start_vertex = tmp
    return t


def t_TERMINAL_VERTEX(t):
    r"""[a-zA-Z]+\(T\)"""
    tmp = t.value
    ends.append(tmp[:-3])
    vertices.append(tmp[:-3])
    return t

def t_COMMON_VERTEX(t):
    r"""[a-z]+\(\)"""
    tmp = t.value
    vertices.append(tmp[:-2])
    return t

def t_EDGE(t):
    r"""\([a-zA-Z]+\,[a-zA-Z]+\)\{[\d,]*\d\}"""
    tmp = t.value
    edges.append(tmp)
    return t


t_STR = r'Alf|Vertices|Edges|Start|:|,'
t_ignore = ' \t'

lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
fileout = open(sys.argv[1] + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break

fileout.write("Analyzing:\n\n")
fileout.write("Alphabet:\n")
for i in alphabet.keys():
    fileout.write('"' + i + '"' + ' ')

fileout.write("Edges: \n")
for i in edges:
    fileout.write(i + '\n')

fileout.write("Testing...\n")
fileout.write('\n')
if start_vertex != -1:
    fileout.write("Passed: starting vertex exists\n")



if len(vertices) == len(set(vertices)):
    fileout.write("All states are unique\n")
