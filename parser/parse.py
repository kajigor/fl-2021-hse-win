import ply.lex as lex
import sys

tokens = ['SYMBOL', 'EDGE', 'VERTEX', 'newline']

fout = open(sys.argv[1] + '.out', 'w')

types = {'S': 'START', 'M': 'MIDDLE', 'T': 'TERMINAL'}

class Vertex:
    def __init__(self, id, type):
        self.id = id
        self.type = type

    def __str__(self):
        return "vertex " + self.id + self.type + " with type " + types[self.type]

    def __eq__(self, other):
        return self.id == other.id and self.type == other.type


class Edge:
    def __init__(self, v_from, v_to):
        self.v_from = v_from
        self.v_to = v_to
        self.symbols = []

    def __str__(self):
        return "from " + str(self.v_from) + " to " + str(self.v_to) + " if symbols are " + ' '.join(self.symbols)

    def __eq__(self, other):
        return self.v_from == other.v_from and sorted(self.symbols) == sorted(other.symbols)

has_start = False
has_one_start = True
has_terminal = False
vertices = []
edges = []
alphabet = []

def bin_to_str(s):
    binary_int = int(s, 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode('ascii')
    return ascii_text

def t_SYMBOL(t):
    r'([0|1]{8})+\s'
    alphabet.append(bin_to_str(t.value))
    return t


def t_VERTEX(t):
    r'([0-9]+(S|M|T))\s'
    global has_start, has_one_start, has_terminal
    v = str(t.value).strip()
    vertices.append(Vertex(v[:-1], v[-1]))
    if vertices[-1].type == 'S':
        if has_start:
            has_one_start = False
        has_start = True
    if vertices[-1].type == 'T':
        has_terminal = True
    return t

def t_EDGE(t):
    r'([0-9]+(S|M|T))-([0-9]+(S|M|T))\s((([0|1]{8})+)\s)+'
    edge = str(t.value).split(' ')
    v1, v2 = edge[0].split('-')
    edges.append(Edge(Vertex(v1[:-1], v1[-1]), Vertex(v2[:-1], v2[-1])))
    edges[-1].symbols = [bin_to_str(i) for i in edge[1:]]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    global fout
    fout.write("Illegal character in " + t.value)
    fout.close()
    exit()

def has_initial():
    if has_start and has_one_start:
        return "Initial state was found"
    elif not has_one_start:
        return "ERROR: There are more than one initial state"
    return "ERROR: Initial state not found"


def vertices_are_unique():
    vertices_list = [(i.id + i.type) for i in vertices]
    if len(vertices_list) == len(set(vertices_list)):
        return "Vertices names are unique"
    else:
        return "ERROR: Vertices names are not unique"


def symbols_are_unique():
    if len(alphabet) == len(set(alphabet)):
        return "Elements of the alphabet are unique"
    else:
        return "ERROR: Elements of the alphabet are not unique"

def comp_check():
    go_to = {}
    for vertex in vertices:
        go_to[(vertex.id + vertex.type)] = []
    for edge in edges:
        for sym in edge.symbols:
            go_to[(edge.v_from.id + edge.v_from.type)].append(sym)

    for val in go_to.values():
        if len(set(val)) != len(alphabet):
            return "ERROR: Non-Complete automaton"
    return "This automaton is complete"

def determ_check():
    go_to = {}
    for vertex in vertices:
        go_to[(vertex.id + vertex.type)] = []
    for edge in edges:
        for sym in edge.symbols:
            go_to[(edge.v_from.id + edge.v_from.type)].append(sym)

    for val in go_to.values():
        if len(set(val)) != len(val):
            return "ERROR: Non-Deterministic automaton"
    return "This automaton is deterministic"


def main():
    global fout, alphabet
    lexer = lex.lex()
    fin = open(sys.argv[1], 'r')
    lexer.input(fin.read())
    fin.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
    fout.write("alphabet:\n")
    for sym in alphabet:
        fout.write(sym + ' ')
    fout.write('\n\n')
    fout.write("vertices list:\n")
    for vertex in vertices:
        fout.write(str(vertex) + '\n')
    fout.write('\n')
    fout.write("edges list:\n")
    for edge in edges:
        fout.write(str(edge) + '\n')
    fout.write('\n')
    fout.write('analysis:\n')
    fout.write(has_initial() + '\n')
    fout.write(vertices_are_unique() + '\n')
    fout.write(symbols_are_unique() + '\n')
    fout.write(determ_check() + '\n')
    fout.write(comp_check() + '\n')
main()
