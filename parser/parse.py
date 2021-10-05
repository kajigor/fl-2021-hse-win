import ply.yacc as yacc
import sys

from lex import tokens


class Edge:
    def __init__(self, from_, to_, moves_):
        self.f = from_
        self.t = to_
        self.moves = moves_

    def __eq__(self, other):
        return self.f == other.f and \
            self.moves == other.moves

    def show(self):
        return '(from: {}, to: {}, moves: {})'.format(self.f, self.t, self.moves)


class State:
    def __init__(self, name_, type_):
        self.name = name_
        self.type = type_
        self.in_edges = []
        self.out_edges = []
        self.from_state = []
        self.to_state = []

    def add_in_edge(self, edge_):
        self.in_edges.append(edge_)

    def add_out_edge(self, edge_):
        self.out_edges.append(edge_)

    def add_from_state(self, state_):
        self.from_state.append(state_)

    def add_to_state(self, state_):
        self.to_state.append(state_)

    def show(self):
        return '(name: {}, type: {})'.format(self.name, self.type)

    def __eq__(self, other):
        return self.type == other.type and \
            sorted(self.from_state) == sorted(other.from_state) and \
            sorted(self.to_state) == sorted(other.to_state) and \
            self.in_edges == other.in_edges and \
            self.out_edges == other.out_edges


class Automat:
    def __init__(self):
        self.alphabet = set()
        self.edges = []
        self.states = []
        self.valid = True
        self.size = 0

    def add_move(self, move_):
        self.alphabet.add(move_)

    def add_edge(self, edge_):
        self.edges.append(edge_)
        for s in self.states:
            if s.name == edge_.t:
                s.in_edges.append(edge_)
                s.from_state.append(edge_.f)
            if s.name == edge_.f:
                s.out_edges.append(edge_)
                s.to_state.append(edge_.t)

    def add_state(self, state_):
        self.states.append(state_)

    def print(self):
        print('Alphabet:')
        print('\t', end='')
        print(self.alphabet)
        print('States:')
        for s in self.states:
            print('\t' + s.show())
        print('Edges:')
        for e in self.edges:
            print('\t' + e.show())

    def check_size(self):
        if self.size != len(self.states):
            raise Exception('Size of automat and number of states differ')

    def check_start_state(self):
        start = False
        cnt = 0
        for s in self.states:
            if s.type == 'start':
                cnt += 1
                start = True
        if cnt > 1 or not start:
            raise Exception('Start state wasn\'t set correctly')

    def check_equality(self):
        for i in range(len(self.states)):
            for j in range(i, len(self.states)):
                if i != j and self.states[i] == self.states[j]:
                    raise Exception(
                        'Equal states found: ' + self.states[i].show() + ' and ' + self.states[j].show())

    def check_completeness_and_determinancy(self):
        for s in self.states:
            if s.type == 'stock':
                continue
            for a in self.alphabet:
                cnt = 0
                for e in s.out_edges:
                    if str(a) in e.moves:
                        cnt += 1
                if cnt == 0:
                    raise Exception('Automat is not complete')
                if cnt > 1:
                    raise Exception('Automat is non-determinate')

    def check(self):
        try:
            self.check_size()
            self.check_start_state()
            self.check_equality()
            self.check_completeness_and_determinancy()
        except Exception as e:
            self.valid = False
            print('Error:')
            print('\t' + str(e))
        return self.valid


automat = Automat()


def p_substance(p):
    '''substance : state BACKSLASH
                 | edge BACKSLASH
                 | size BACKSLASH'''


def p_size(p):
    'size : NUM'
    automat.size = p[1]


def p_state(p):
    'state : NUM DASH type'
    automat.add_state(State(p[1], p[3]))


def p_term(p):
    '''type : NUM'''
    if p[1] == 0:
        p[0] = 'start'
    elif p[1] == 1:
        p[0] = 'normal'
    elif p[1] == 2:
        p[0] = 'stock'
    else:
        p[0] = 'terminal'


def p_edge(p):
    'edge : NUM ARROW NUM COLON moves'
    automat.add_edge(Edge(p[1], p[3], p[5]))


def p_moves(p):
    '''moves : move COMMA moves
             | move'''
    if len(p) == 4:
        p[0] = p[1] + ',' + p[3]
    else:
        p[0] = p[1]


def p_move(p):
    '''move : NUM
            | STR
            | NUM DOTS NUM'''
    automat.add_move(p[1])
    p[0] = str(p[1])
    if len(p) == 4:
        if p[2] == '...':
            for i in range(int(p[1]) + 1, int(p[3]) + 1):
                automat.add_move(i)
                p[0] += ',' + str(i)


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()

sys.stdin = open(sys.argv[1], 'r')
while True:
    try:
        s = input()
    except EOFError:
        break
    try:
        parser.parse(s)
    except Exception as e:
        print(str(e))
        break


sys.stdout = open(sys.argv[1] + '.out', 'w')

if automat.check():
    automat.print()
