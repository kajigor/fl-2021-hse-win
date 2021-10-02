import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}

tokens = ['alphabet', 'vertex', 'edge_name', 'edge', 'machine'] + list(reserved.values())

file_out = open(sys.argv[1] + '.out', 'w')


class Vertex:
    def __init__(self, index_, name_, terminality_):
        self.index = index_
        self.name = name_
        self.terminality = terminality_
        self.edges = []

    def write(self):
        file_out.write(str(self.index) + ". " + "Name: \"" + self.name + "\" and it is " +
                       "not " * (not self.terminality) + "a terminal\n")


class Edge:
    def __init__(self, index_vertex_from_, name_, index_vertex_to_):
        self.index_vertex_from = index_vertex_from_
        self.name = name_
        self.index_vertex_to = index_vertex_to_

    def write(self):
        file_out.write("From " + str(self.index_vertex_from) + " to " +
                       str(self.index_vertex_to) + " name: \"" + self.name + "\"\n")


is_open_edge = False
is_open_machine = False
is_first_vertex = False
vertexes = []
edges = []
alphabet = []
current_edge = Edge(None, "", None)


def get_name(s):
    name = ""
    current_code = ""
    for i in range(0, len(s)):
        current_code += s[i]
        if len(current_code) == 8:
            name += chr(int(current_code, 2))
            current_code = ""
    return name


def vertexes_update(name, terminality):
    global vertexes
    new_index = 0
    for v in vertexes:
        if v.name == name and v.terminality == terminality:
            return v.index
        new_index = v.index
    new_index += 1
    vertexes.append(Vertex(new_index, name, terminality))
    return new_index


def t_alphabet(t):
    r'E([0-1]{8})*E'
    global alphabet
    alphabet = list(get_name(t.value[1:len(t.value) - 1:1]))
    return t


def t_edge_name(t):
    r'B([0-1]{8})*B'
    global is_first_vertex, file_out
    is_first_vertex = False
    current_edge.name = get_name(t.value[1:len(t.value) - 1:1])
    return t


def t_vertex(t):
    r'A(0|1)B([0-1]{8})*BA'
    global is_first_vertex, file_out, current_edge
    index = vertexes_update(get_name(t.value[3:(len(t.value) - 2):1]), t.value[1] == '1')
    if is_first_vertex:
        current_edge.index_vertex_from = index
    else:
        current_edge.index_vertex_to = index
        if current_edge.index_vertex_from is not None:
            vertexes[current_edge.index_vertex_from - 1].edges.append(current_edge.name)
        edges.append(current_edge)
    return t


def t_edge(t):
    r'C'
    global is_open_edge, is_first_vertex, file_out, current_edge
    if not is_open_edge:
        current_edge = Edge(None, "", None)
        is_first_vertex = True
        is_open_edge = True
    else:
        is_open_edge = False
    return t


def t_machine(t):
    r'D'
    global is_open_machine, file_out
    if not is_open_machine:
        file_out.write("I solemnly swear I am up to no good!\n")
        is_open_machine = True
    else:
        is_open_machine = False
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global file_out
    file_out.write("Illegal character '%s'" % t.value[0])
    file_out.close()
    exit()


def initial_state_checking():
    index = -1
    for e in edges:
        if e.index_vertex_from is None and e.index_vertex_to is not None:
            if index != -1:
                return "ERROR: not the only initial state"
            else:
                index = e.index_vertex_to
    if index == -1:
        return "ERROR: initial state does not exist"
    return "Initial state found: " + str(index)


def uniqueness_machine_checking():
    vertexes_names = []
    for v in vertexes:
        vertexes_names.append(v.name)
    if len(vertexes_names) == len(set(vertexes_names)):
        return "Vertex names are unique"
    else:
        return "ERROR: vertex names are not unique"


def uniqueness_alphabet_checking():
    if len(alphabet) == len(set(alphabet)):
        return "Elements of the alphabet are unique"
    else:
        return "ERROR: elements of the alphabet are not unique"


def determinism_checking():
    for v in vertexes:
        all_edges = ""
        for e in v.edges:
            all_edges += e
        if list(all_edges) != list(set(all_edges)):
            return "Machine is not deterministic"
    return "Machine is deterministic"


def completeness_checking():
    for v in vertexes:
        all_edges = ""
        for e in v.edges:
            all_edges += e
        if list(set(alphabet)) != list(set(all_edges)):
            return "Machine is not full"
    return "Machine is full"


def main():
    global file_out, alphabet
    lexer = lex.lex()
    file_in = open(sys.argv[1], 'r')
    lexer.input(file_in.read())
    file_in.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
    file_out.write("Alphabet:\n")
    for a in alphabet:
        file_out.write(a + ' ')
    file_out.write('\n')
    file_out.write("Vertexes list:\n")
    for v in vertexes:
        v.write()
    file_out.write("Edges list:\n")
    for e in edges:
        e.write()
    file_out.write("Edges list:\n")
    file_out.write("1. " + initial_state_checking() + "\n")
    file_out.write("2. " + uniqueness_machine_checking() + "\n")
    file_out.write("3. " + uniqueness_alphabet_checking() + "\n")
    file_out.write("4. " + determinism_checking() + "\n")
    file_out.write("5. " + completeness_checking() + "\n")
    file_out.write("Mischief Managed!\n")
    file_out.close()


main()
