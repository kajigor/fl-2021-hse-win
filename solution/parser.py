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


class Automate:
    class Vertex:
        def __init__(self, i_, terminality_):
            self.i = i_
            if terminality_ == '#':
                terminality_ = 'Normal'
            if terminality_ == '$':
                terminality_ = 'Terminal'
            self.terminality = terminality_
            self.edges = []

        def write(self):
            print('\t\t' + str(self.i) + ': ' + str(self.terminality), end='\n')

    class Edge:
        def __init__(self, index_vertex_from_, crossover_, index_vertex_to_):
            self.index_vertex_from = index_vertex_from_
            self.crossover = crossover_
            self.index_vertex_to = index_vertex_to_

        def write(self):
            print('\t\t' + "From: " + str(self.index_vertex_from) + "\t\tCrossover: " + str(
                self.crossover) + "\t\tTo: " + str(self.index_vertex_to), end='\n')

    class Alphabet:
        def __init__(self, crossover_):
            self.crossover = crossover_

        def write(self, i):
            print('\t\t' + str(self.crossover) + ": " + str(i))

    vertexes = []
    unique_vertexes = {}
    edges = []
    alphabet = []


ERROR = 0


def t_ALPHABET(t):
    r'".+?"'
    Automate.alphabet.append(Automate.Alphabet(t.value[1:-1]))
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
    Automate.edges.append(Automate.Edge(parts[0], parts[1], parts[2]))
    Automate.vertexes.append(Automate.Vertex(parts[2], parts[3]))
    return t


def t_START(t):
    r'(?<=\n)\d(?=\n)'
    Automate.vertexes.append(Automate.Vertex(t.value, 'Start'))
    return t


def initial_state_checking():
    global ERROR
    for v, s in Automate.unique_vertexes.items():
        if s == 'Start':
            return "Initial state found: " + str(v)
    ERROR += 1
    return "ERROR: initial state does not exist"


def uniqueness_of_states_checking():
    global ERROR
    for v in Automate.vertexes:
        if Automate.unique_vertexes.get(v.i) is None:
            if v.terminality != 'Start':
                Automate.unique_vertexes.update({v.i: v.terminality})
        else:
            if Automate.unique_vertexes[v.i] == v.terminality:
                continue
            else:
                ERROR += 1
                return "ERROR: vertex names are not unique"
    return "Vertexes are unique"


def uniqueness_alphabet_checking():
    if len(Automate.alphabet) == len(set(Automate.alphabet)):
        return "Elements of the alphabet are unique"
    else:
        return "ERROR: elements of the alphabet are not unique"


def make_adjacency():
    for e in Automate.edges:
        for v in Automate.vertexes:
            if e.index_vertex_from == v.i:
                v.edges.append(e.crossover)


def determinism_checking():
    global ERROR
    make_adjacency()
    for v in Automate.vertexes:
        all_vertex_edges = []
        for e in v.edges:
            all_vertex_edges.append(e)
        if len(all_vertex_edges) != len(set(all_vertex_edges)):
            ERROR += 1
            return "Automate is not deterministic"
    return "Automate is deterministic"


def completeness_checking():
    global ERROR
    for v in Automate.vertexes:
        all_vertex_edges = []
        for e in v.edges:
            all_vertex_edges.append(e)
        if len(all_vertex_edges) != len(set(all_vertex_edges)) or len(all_vertex_edges) != len(Automate.alphabet):
            ERROR += 1
            return "Automate is not full"
    return "Automate is full"


def automate_is_good():
    return "========= " + str(5 - ERROR) + "/5 are COMPLETE! ========= \n\nAutomate is good!\tLOOK: \n"


def automate_is_not_good():
    return "========= " + str(5 - ERROR) + "/5 are complete! ========= \n\nI have sad news... Your automate is bad"


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
    print("3) " + uniqueness_alphabet_checking())
    print("4) " + determinism_checking())
    print("5) " + completeness_checking())

    # ВЫВОД
    if not ERROR:
        print(automate_is_good())

        print("Alphabet:", end='\n')
        i = 0
        for a in Automate.alphabet:
            i += 1
            Automate.Alphabet.write(a, i)
        print('\n')

        print("Vertexes:", end='\n')
        for v, s in Automate.unique_vertexes.items():
            vert = Automate.Vertex(v, s)
            Automate.Vertex.write(vert)
        print('\n')

        print("Edges:", end='\n')
        for e in Automate.edges:
            Automate.Edge.write(e)
    else:
        print(automate_is_not_good())


main()
