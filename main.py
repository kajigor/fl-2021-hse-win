import ply.lex as lex
import sys

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

cnt_checks = 0
cnt_passed = 0
alphabet = {}
edges = {}
ends = []
start_vertex = -1
vertices = []
special_symbols = ['{', '}', ',', '(', ')', '\\']


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


def t_error(t):
    fileout.write("Incorrect input format '%s'" % t.value)
    t.lexer.skip(len(t.value))
    sys.exit(0)

def t_ALPHABET(t):
    r"""Alf:\s\{[.*,]*.*\}"""
    tmp = t.value[6:-1]
    it2 = 0
    j = 0
    while True:
        it2 = tmp.find(', ')
        if it2 == -1:
            break
        alphabet[j] = tmp[0: it2]
        j = j + 1
        tmp = tmp[it2 + 2:]
        if not tmp:
            break
    alphabet[j] = tmp[0:]


def t_START_VERTEX(t):
    r"""Start:\s[a-zA-Z]+\(S\)"""
    tmp = t.value[7:-3]
    global start_vertex
    if tmp:
        start_vertex = tmp


def t_TERMINAL_VERTEX(t):
    r"""[a-zA-Z]+\(T\)"""
    tmp = t.value
    ends.append(tmp[:-3])
    vertices.append(tmp[:-3])


def t_COMMON_VERTEX(t):
    r"""[a-z]+\(\)"""
    tmp = t.value
    vertices.append(tmp[:-2])


def t_EDGE(t):
    r"""\([^)]+\)\{[^;]+\};"""
    tmp = t.value
    st1 = tmp[tmp.find('(') + 1: tmp.find(',')]
    st2 = tmp[tmp.find(',') + 1: tmp.find(')')]
    it = tmp.find('{')
    by_symbols = []
    while True:
        ind = tmp[it + 1:].find(', ')
        if ind != -1:
            new_word = tmp[it + 1: ind + it + 1]
            it = it + len(new_word) + 2
        else:
            break
        by_symbols.append(new_word)
    by_symbols.append(tmp[it + 1: -2])
    edges[st1, st2] = by_symbols


def check_transitions():
    for k in edges.keys():
        for j in edges[k]:
            if j not in alphabet.values():
                fileout.write(
                    f"\n\nError: the word \"{str(j)}\" was found in the transition, which is not in the alphabet\n\n")
                return False
    return True


def is_deterministic():
    for s in vertices:
        l = []
        for e in edges.keys():
            if s == e[0]:
                l += edges[e]
        if len(l) != len(set(l)):
            return False
    return True


def is_complete():
    for s in vertices:
        l = []
        for e in edges.keys():
            if s == e[0]:
                l += edges[e]
        if len(set(l)) != len(alphabet):
            return False
    return True


t_STR = r'Alf|Vertices|Edges|Start|:|,'
t_ignore = ' \t'
lexer = lex.lex()
lexer.input(open(sys.argv[1], 'r').read())
fileout = open(sys.argv[1] + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break

fileout.write("PARSING...\n\n")
fileout.write("Alphabet:\n\t")

for i in alphabet.values():
    fileout.write(f"\"{str(i)}\"\n\t")

fileout.write("\nStates:\n\t")
for i in vertices:
    fileout.write(f"{i}")
    if i == start_vertex:
        fileout.write(" -- Start vertex")
    if i in ends:
        fileout.write(" -- Terminal vertex")
    fileout.write(" -- Common vertex")
    fileout.write("\n\t")


fileout.write("\nTransitions: \n\t")

if not check_transitions():
    fileout.write("Further checks suspended due to errors!")
    sys.exit(0)
for i in edges.keys():
    fileout.write(
        f"transition between state \"{str(i[0])}\" and \"{str(i[1])}\"  by symbols: {str(edges[i])}\n\t")

fileout.write('\n==================================\n')
fileout.write("\nTESTING...\n\n")

cnt_checks = cnt_checks + 1
if start_vertex != -1:
    fileout.write("Passed: starting vertex exists\n")
    cnt_passed = cnt_passed + 1
else:
    fileout.write("Error: start vertex missing\n");

cnt_checks = cnt_checks + 1
if len(vertices) == len(set(vertices)):
    fileout.write("Passed: all states are unique\n")
    cnt_passed = cnt_passed + 1
else:
    fileout.write("Error: states are not unique\n")

cnt_checks = cnt_checks + 1
if len(alphabet.values()) == len(set(alphabet.values())):
    fileout.write("Passed: all symbols are unique\n")
    cnt_passed = cnt_passed + 1
else:
    fileout.write("Error: symbols are not unique\n")

cnt_checks = cnt_checks + 1
if is_deterministic():
    fileout.write("Passed: automaton is deterministic\n")
    cnt_passed = cnt_passed + 1
else:
    fileout.write("Error: automaton is not deterministic\n")

cnt_checks = cnt_checks + 1
if is_complete():
    fileout.write("Passed: automaton is complete\n")
    cnt_passed = cnt_passed + 1
else:
    fileout.write("Error: automaton is not complete\n")

if cnt_checks != cnt_passed:
    fileout.write(f"\nPassed only {cnt_passed} checks out of {cnt_checks}")
else:
    fileout.write(f"\nAll checks passed({cnt_checks}/{cnt_passed})!")
