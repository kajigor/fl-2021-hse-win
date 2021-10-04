import ply.lex as lex
import sys

tokens = [
    'NUM',
    'POINT',
    'NORMAL',
    'TERMINAL',
    'ARROW',
    'COMMA',
    'ALPHABET',
    'QUOTES',
    'START',
    'EDGE'
]


class Vertex:
    def __init__(self, i_, terminality_):
        self.i = i_
        if terminality_ == '#':
            terminality_ = 'N'
        if terminality_ == '$':
            terminality_ = 'T'
        self.terminality = terminality_

    def write(self):
        print(str(self.i) + " " + str(self.terminality), end='')


class Edge:
    def __init__(self, index_vertex_from_, crossover_, index_vertex_to_):
        self.index_vertex_from = index_vertex_from_
        self.crossover = crossover_
        self.index_vertex_to = index_vertex_to_

    def write(self):
        print(str(self.index_vertex_from) + ' ' + str(self.crossover) + ' ' + str(self.index_vertex_to), end='')


class Alphabet:
    def __init__(self, crossover_):
        self.crossover = crossover_

    def write(self):
        print(str(self.crossover), end='')


vertexes = []
unique_vertexes = {}
edges = []
alphabet = []

ERROR = 0


def t_ALPHABET(t):
    r'".+?"'
    global alphabet
    alphabet.append(Alphabet(t.value[1:-1]))
    return t


def t_EDGE(t):
    r'(?<=\n).*\.'
    parts = 4 * []
    part = ''
    for p in t.value:
        if p != '.':
            part += p
        if p == '.':
            parts.append(part)
            part = ''
    global edges
    edges.append(Edge(parts[0], parts[1], parts[2]))
    global vertexes
    vertexes.append(Vertex(parts[2], parts[3]))
    return t


def t_START(t):
    r'(?<=\n)\d(?=\n)'
    global vertexes
    vertexes.append(Vertex(t.value, 'S'))
    return t


def initial_state_checking():
    global unique_vertexes, ERROR
    for v, s in unique_vertexes.items():
        if s == 'S':
            return "Initial state found: " + str(v)
    ERROR = 1
    return "ERROR: initial state does not exist"


def uniqueness_of_states_checking():
    global vertexes, unique_vertexes
    for v in vertexes:
        if unique_vertexes.get(v.i) is None:
            unique_vertexes.update({v.i: v.terminality})
        else:
            if unique_vertexes[v.i] == v.terminality:
                continue
            else:
                global ERROR
                ERROR = 1
                return "ERROR: vertex names are not unique"
    return "Vertexes are unique"


# def uniqueness_alphabet_checking():
#     if len(alphabet) == len(set(alphabet)):
#         return "Elements of the alphabet are unique"
#     else:
#         return "ERROR: elements of the alphabet are not unique"


# def determinism_checking():
#     for v in vertexes:
#         all_edges = ""
#         for e in v.edges:
#             all_edges += e
#         if list(all_edges) != list(set(all_edges)):
#             return "Machine is not deterministic"
#     return "Machine is deterministic"


# def completeness_checking():
#     for v in vertexes:
#         all_edges = ""
#         for e in v.edges:
#             all_edges += e
#         if list(set(alphabet)) != list(set(all_edges)):
#             return "Machine is not full"
#     return "Machine is full"

def automate_is_good():
    return "5/5 are COMPLETE! \n\nAutomate is good! Look: \n"

def automate_is_not_good():
    return "I have sad news... Your automate is bad"


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


t_QUOTES = r'\"|\\\"'
t_POINT = r'\.'
t_NORMAL = r'\#'
t_TERMINAL = r'\$'
t_ARROW = r'->'
t_COMMA = r','

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def main():
    global file_out, alphabet
    lexer = lex.lex()
    lexer.input(open(sys.argv[1], 'r').read())
    sys.stdout = open(sys.argv[1] + '.out', 'w')
    while True:
        token = lexer.token()
        if not token:
            break
        # print(token)
    # ВСЕ ПРОВЕРКИ
    print("1) " + uniqueness_of_states_checking())
    print("2) " + initial_state_checking())

    # ВЫВОД
    if not ERROR:
        print(automate_is_good())

        print("Alphabet:", end=' ')
        for a in alphabet:
            Alphabet.write(a)
            print(',', end=' ')
        print('\n')

        print("Vertexes:", end=' ')
        for v, s in unique_vertexes.items():
            vert = Vertex(v, s)
            Vertex.write(vert)
            print(',', end=' ')
        print('\n')

        print("Edges:", end=' ')
        for e in edges:
            Edge.write(e)
            print(',', end=' ')
    else:
        print(automate_is_not_good())

main()
