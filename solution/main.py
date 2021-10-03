import ply.lex as lex
import sys
import re

tokens = [
    'alphabet',
    'Q',
    'start',
    'T',
    'function'
]

global_alphabet = []
vertex_cnt = ""
start_vertex = ""
terminal_vertexes = []
edges = []

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    fout.write("Incorrect input format '%s'" % t.value[0] + "\n")
    t.lexer.skip(1)

def t_alphabet(t):
    r'alphabet:.+ \|\|'
    s = t.value[9:-3]
    for i in s:
        global_alphabet.append(i)
    return t

def t_Q(t):
    r'Q:\(.+ s'
    global vertex_cnt
    vertex_cnt = t.value[3:-3]
    return t

def t_start(t):
    r'tart:.+ T'
    global start_vertex
    start_vertex = t.value[6:-3]
    return t

def t_T(t):
    r':\(.+ f'
    global terminal_vertexes
    str = t.value[1:-2]
    сur = ""
    for i in str:
        if i == ')':
            terminal_vertexes.append(cur)
        elif i == '(':
            cur = ""
        else:
            cur = cur + i
    return t

def t_function(t):
    r'unction:.+'
    global edges
    str = t.value[8:]
    сur = ""
    cnt = 0
    current_edge = ["","",""]
    for i in str:
        if i == ')':
            if cnt != 2:
                current_edge[cnt] = cur
                cnt += 1
            else:
                current_edge[cnt] = current_edge[cnt] + global_alphabet[int(cur) - 1]
        elif i == '(':
            cur = ""
        elif i == '.':
            edges.append(current_edge)
            current_edge = ["", "", ""]
            cnt = 0
        else:
            cur = cur + i
    return t


lexer = lex.lex()

# fin = open(sys.argv[1], 'r').read()
fin = open("input.txt", 'r').read()
lexer.input(fin)
# fout = open(sys.argv[1] + '.out', 'w')
fout = open('input.txt' + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break

fout.write("Alphabet:\n")
for s in global_alphabet:
    fout.write(s + ' ')
fout.write("\nVertex count:\n" + vertex_cnt + "\nStart position: \n" + start_vertex + "\nTerminal positions: \n")
for i in terminal_vertexes:
    fout.write(i + ' ')
fout.write("\nEdges: \n")
for i in edges:
    fout.write("transition from " + i[0] + " to " + i[1] + " by " + i[2] + "\n")
