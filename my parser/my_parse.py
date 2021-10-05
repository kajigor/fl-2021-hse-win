import ply.yacc as yacc
import sys
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

from my_lex import tokens


def states_are_equal(state1, state2):
    if state1.is_terminal != state2.is_terminal:
        return False
    if state1.is_start != state2.is_start:
        return False
    if state1.from_state != state2.from_state:
        return False
    if state1.to_state != state2.to_state:
        return False
    return True


class Edge:
    def __init__(self):
        self.state_from_name = ""
        self.state_to_name = ""
        self.symbols = []

    def add_symbol(self, symbol):
        self.symbols.append(symbol)

    def add_state_from(self, state_from_):
        if self.state_from_name != "":
            raise Exception("Error: the outgoing state already exists")
        self.state_from_name = state_from_

    def add_state_to(self, state_to_):
        if self.state_to_name != "":
            raise Exception("Error: the incoming state already exists")
        self.state_to_name = state_to_


class State:
    def __init__(self, name_):
        self.name = name_
        self.is_terminal = False
        self.is_start = False
        self.out_edges = []
        self.in_edges = []
        self.from_states = []
        self.to_states = []

    def set_is_terminal(self):
        self.is_terminal = True

    def set_is_start(self):
        self.is_start = True


class Automata:
    def __init__(self):
        self.sigma = []
        self.edges = []
        self.states = [State("stock")]

    def add_symbol(self, symbol_):
        self.sigma.append(symbol_)

    def add_edge(self, edge_):
        self.edges.append(edge_)

    def add_state(self, state_):
        self.states.append(state_)

    def add_terminal_state(self, terminal_name):
        flag = False
        for s in self.states:
            if s.name == terminal_name:
                s.set_is_terminal()
                flag = True
        if not flag:
            raise Exception("Error: there is no such a state to mark terminal")

    def add_start_state(self, start_name):
        flag = False
        for s in self.states:
            if s.name == start_name:
                s.set_is_start()
                flag = True
        if not flag:
            raise Exception("Error: there is no such a state to mark start")

    def find_start_state(self):
        for s in self.states:
            if s.is_start:
                return s

    def find_terminal_states(self):
        terminal_states = []
        for s in self.states:
            if s.is_terminal:
                terminal_states.append(s)
        return terminal_states

    def check_uniqueness_states(self):
        for i in range(0, len(self.states)):
            for j in range(0, len(self.states)):
                if i != j and states_are_equal(self.states[i], self.states[j]):
                    raise Exception(
                        "Error: these states are not unique: " + self.states[i].name + " and " + self.states[j].name)

    def check_start_state(self):
        flag = False
        for s in self.states:
            if s.is_start:
                flag = True
        if not flag:
            raise Exception("Error: there is no start state in the automata")

    def print_automata(self):
        dictionary = {x.name: dict() for x in self.states}
        for edge in self.edges:
            for symbol in edge.symbols:
                dictionary[edge.state_from_name][symbol] = edge.state_to_name
        for state in self.states:
            for symbol in self.sigma:
                if not (symbol in dictionary[state.name]):
                    dictionary[state.name][symbol] = "stock"
        dfa = VisualDFA(
            states=set([x.name for x in self.states]),
            input_symbols=set(self.sigma),
            transitions=dictionary,
            initial_state=self.find_start_state().name,
            final_states=set([x.name for x in self.find_terminal_states()]),
        )
        dfa.show_diagram()
        dfa.table
        dfa.show_diagram(filename=(sys.argv[1] + '.out'), path='/Users/emilialekhman/Desktop/fl/fl-2021-hse-win/my parser/')


def p_automata(p):
    '''Automata : Sigma
                 | States
                 | Terminal
                 | Start_state
                 | Edges '''


def p_sigma(p):
    'Sigma : Start_description_sigma list_symb'


def p_states(p):
    'States : Start_description_states list_state'


def p_terminal(p):
    'Terminal : Start_description_terminal list_state'


def p_start_state(p):
    'Start_state : Start_description_start_state list_state'


def p_edges(p):
    'Edges : Start_description_edges list_edges'


def p_sigma_start(p):
    'Start_description_sigma : SIGMA COLON'
    parser.list_read_now = "sigma"


def p_states_start(p):
    'Start_description_states : STATES COLON'
    parser.list_read_now = "states"


def p_terminal_start(p):
    'Start_description_terminal : TERMINAL COLON'
    parser.list_read_now = "terminal"


def p_start_state_start(p):
    'Start_description_start_state : START_STATE COLON'
    parser.list_read_now = "start_state"


def p_edges_start(p):
    'Start_description_edges : DELTA COLON'
    parser.list_read_now = "edge"


def p_list_edges(p):
    '''list_edges : list_edges COMMA edge
                | edge'''


def p_edge(p):
    'edge : OPEN_BR ID DASH ID COMMA NUM CLOSED_BR'
    parser.list_read_now = "edge"
    parser.edge_read_now.add_state_from(p[2])
    parser.edge_read_now.add_state_to(p[4])
    parser.edge_read_now.add_symbol(p[6])
    parser.automata.add_edge(parser.edge_read_now)
    parser.edge_read_now = Edge()


def p_read_list_state(p):
    '''list_state : list_state COMMA ID
                | ID'''
    i = 3
    if len(p) == 2:
        i = 1
    if parser.list_read_now == "states":
        parser.automata.add_state(State(p[i]))
    elif parser.list_read_now == "terminal":
        parser.automata.add_terminal_state(p[i])
    elif parser.list_read_now == "start_state":
        parser.automata.add_start_state(p[i])


def p_read_list_symb(p):
    '''list_symb : list_symb COMMA NUM
                | NUM'''
    i = 3
    if len(p) == 2:
        i = 1
    if parser.list_read_now == "sigma":
        parser.automata.add_symbol(p[i])


def p_error(p):
    raise Exception("Syntax error")


parser = yacc.yacc()

parser.list_read_now = ""
parser.automata = Automata()
parser.edge_read_now = Edge()
parser.is_valid_automata = True

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')


def not_valid_automata(err):
    parser.is_valid_automata = False
    print(err)
    print("The automata will not be created")


while True:
    try:
        s = input()
    except EOFError:
        break
    if not s:
        continue
    try:
        result = parser.parse(s)
    except Exception as e:
        not_valid_automata("Error: " + str(e))
        break

if parser.is_valid_automata:
    try:
        parser.automata.print_automata()
    except Exception as e:
        not_valid_automata("Error: " + str(e))
