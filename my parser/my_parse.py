import ply.yacc as yacc
import sys

from lex import tokens


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def equality_state(state1, state2):
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
        self.state_from = ""
        self.state_to = ""
        self.symbols = []

    def add_symbol(self, symbol):
        self.symbols.append(symbol)
        
    def add_state_from(self, state_from_):
        if self.state_from != "":
            raise Exception("Error: the outgoing state already exists")
        self.state_from = state_from_
        
    def add_state_to(self, state_to_):
        if self.state_to != "":
            raise Exception("Error: the incoming state already exists")
        self.state_to = state_to_

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
        
class Automaton:
    def __init__(self):
        self.sigma = []
        self.edges = []
        self.states = []

    def add_symbol(self, symbol_):
        self.sigma.append(symbol_)
 
    def add_edge(self, edge_):
        self.edges.append(edge_)
        
    def add_state(self, state_):
        self.states.append(state_)
        
    def add_terminal(self, terminal):
        flag = False
        for s in self.states:
            if s.name == terminal:
                s.set_is_terminal()
                flag = True
        if not flag:
            raise Exception("Error: there is no such a state")
    
    def add_start(self, start):
        flag = False
        for s in self.states:
            if s.name == start:
                s.set_is_start()
                flag = True
        if not flag:
            raise Exception("Error: there is no such a state")

    def check_uniqueness_states(self):
        for i in range(0, len(self.states)):
            for j in range(0, len(self.states)):
                if i != j and equality_state(self.states[i], self.states[j]):
                    raise Exception("Error: thes states are not unique: " + self.states[i].name + " and " + self.states[j].name)

    def check_start_state(self):
        flag = False
        for s in self.states:
            if s.is_start == True:
                flag = True
        if not flag:
            raise Exception("Error: there is no start state in the automaton")
    

def p_automaton(p):
    '''Automaton : Sigma
                 | States
                 | Terminal
                 | Start_state
                 | Edges '''

def p_sigma(p):
    'Sigma : Start_description_sigma list_symb'
    
def p_states(p):
    'States : Start_description_states list_state'
    
def p_start_state(p):
    'Start_state : Start_description_start_state list_state'

def p_terminal(p):
    'Terminal : Start_description_terminal list_state'

def p_edges(p):
    'Edges : Start_description_edges list_edges'

def p_sigma_start(p):
    'Start_description_sigma : SIGMA COLON'
    parser.list_read_now = "sigma"
    
def p_states_start(p):
    'Start_description_states : STATES COLON'
    parser.list_read_now = "states"

def p_start_state_start(p):
    'Start_description_start_state : START_STATE COLON'
    parser.list_read_now = "start_state"

def p_terminal_start(p):
    'Start_description_terminal : TERMINAL COLON'
    parser.list_read_now = "terminal"

def p_edges_start(p):
    'Start_description_edges : DELTA COLON'
    parser.list_read_now = "edges"

def p_edge(p):
    'Start_description_edge : OPEN_BR ID DASH ID COMMA NUM CLOSED_BR'
    parser.list_read_now = "edge"
    parser.edge_read_now.add_state_from(p[2])
    parser.edge_read_now.add_state_to(p[4])

def p_read_list_state(p):
    '''list_state : list_state COMMA ID
                | ID'''
    i = 3
    if len(p) == 2:
       i = 1
    if parser.list_read_now == "states":
        parser.automaton.add_state(State(p[i]))
    elif parser.list_read_now == "terminal":
        parser.automaton.add_terminal(p[i])
    elif parser.list_read_now == "start_state":
        parser.automaton.add_start_state(p[i])

def p_read_list_symb(p):
    '''list_symb : list_symb COMMA NUM
                | NUM'''
    i = 3
    if len(p) == 2:
       i = 1
    if parser.list_read_now == "sigma":
        parser.automaton.add_symbol(p[i])

def p_error(p):
    raise Exception("Syntax error")

parser = yacc.yacc()

parser.list_read_now = ""
parser.automaton = Automaton()
parser.edge_read_now = Edge()
parser.is_valid_automaton = True

parser.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + '.out', 'w')


while True:
  try:
    s = input()
  except EOFError:
    break
  if not s:
    continue
  result=parser.parse(s)
  print(result)
