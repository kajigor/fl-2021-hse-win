import ply.yacc as yacc
import sys
from lex import tokens

class Edge:
    def __init__(self):
        self.state_from = ""
        self.state_to = ""
        self.symbols = []
        
    def add_symbol(self, symbol):
        self.symbols.append(symbol)
        
    def add_state_from(self, state_from_):
        if self.state_from != "":
            raise Exception("This edge already has an outgoing state")
        self.state_from = state_from_
        
    def add_state_to(self, state_to_):
        if self.state_to != "":
            raise Exception("This edge already has an incoming state")
        self.state_to = state_to_
        
class State:
    def __init__(self, name_):
        self.name = name_
        self.terminality = False
        self.description = ""
        
    def change_terminality(self):
        self.terminality = True
        
    def add_description(self, description_):
        self.description = description_
                       
class Automaton:
    def __init__(self):
        self.alphabet = []
        self.edges = []
        self.states = []
        
    def print_val(self):
        print("Alphabet:")
        print("    ", end = "")
        print(self.alphabet)
        print("States:")
        for i in self.states:
            s = "False"
            if i.terminality:
                s = "True"
            print("    name: " + i.name + ", terminality: " + s + ", description: \"" + i.description + "\"")
        print("Edges:")
        for i in self.edges:
            print("    state from: " + i.state_from + ", state to: " + i.state_to + ", symbols: ", end = "")
            print(i.symbols)
  
    def add_symbol(self, symbol_):
        self.alphabet.append(symbol_)
 
    def add_edge(self, edge_):
        self.edges.append(edge_)
        
    def add_state(self, state_):
        self.states.append(state_)
        
    def add_terminal(self, terminal):
        f = False
        for s in self.states:
            if s.name == terminal:
                s.change_terminality()
                f = True
        if not f:
            raise Exception("No such state was found in the list of states")
     
    def add_description_for_state(self, state, description_):
        for s in self.states:
            if s.name == state:
                s.add_description(description_)
        

def check_err1():
    if parser.list_read_now != "" or parser.is_open_curly_bracket or parser.is_open_square_bracket:
    	return True
    return False
    
def p_automaton(p):
    '''Automaton : Alphabet
                 | States
                 | Terminal
                 | Description_states
                 | Edges '''
    
#def p_empty(p):
#    'Empty :'
#    pass

def p_alphabet(p):
    'Alphabet : Start_description_alphabet list Close_curly_bracket'
    
def p_states(p):
    'States : Start_description_states list Close_curly_bracket'
    
def p_terminal(p):
    'Terminal : Start_description_terminal list Close_curly_bracket'

def p_edges(p):
    '''Edges : Edges Start_description_edge list Close_square_bracket
             | Start_description_edge list Close_square_bracket'''

def p_edge_start(p):
    'Start_description_edge : VARIABLE ARROW VARIABLE SQUARE_BRACKET_OPEN'
    if check_err1() or parser.edge_read_now.state_from != "" or parser.edge_read_now.state_to != "" or parser.edge_read_now.symbols != []:
        raise Exception("Error while reading the edge")
    parser.list_read_now = "edge"
    parser.is_open_square_bracket = True
    parser.edge_read_now.add_state_from(p[1])
    parser.edge_read_now.add_state_to(p[3])
            
def p_alphabet_start(p):
    'Start_description_alphabet : ALPHABET CURLY_BRACKET_OPEN'
    if check_err1():
        raise Exception("Error while reading the alphabet")
    parser.list_read_now = "alphabet"
    parser.is_open_curly_bracket = True
    
def p_states_start(p):
    'Start_description_states : STATES CURLY_BRACKET_OPEN'
    if check_err1():
        raise Exception("Error while reading the states")
    parser.list_read_now = "states"
    parser.is_open_curly_bracket = True
    
def p_description_states(p):
    ''' Description_states : Description_states STATE VARIABLE CURLY_BRACKET_OPEN STR CURLY_BRACKET_CLOSE
                           | STATE VARIABLE CURLY_BRACKET_OPEN STR CURLY_BRACKET_CLOSE '''
    i = 2
    if len(p) == 7:
        i += 1
    if check_err1():
        raise Exception("Error while reading the description_state")
    parser.automaton.add_description_for_state(p[i], p[i + 2])

def p_terminal_start(p):
    'Start_description_terminal : TERMINAL CURLY_BRACKET_OPEN'
    if check_err1():
        raise Exception("Error while reading the terminal states")
    parser.list_read_now = "terminal"
    parser.is_open_curly_bracket = True
    
def p_read_list(p):
    '''list : list COMMA STR
            | list COMMA VARIABLE
            | STR
            | VARIABLE'''
    if parser.list_read_now == "" or (not parser.is_open_curly_bracket and not parser.is_open_square_bracket):
        raise Exception("When reading a list, there are no open brackets or there is no required type for the values ​​being read")
    if parser.list_read_now == "edge" and not parser.is_open_square_bracket:
        raise Exception("Necessary bracket not open")
    if parser.list_read_now != "edge" and parser.list_read_now != "alphabet" and parser.list_read_now != "states" and parser.list_read_now != "terminal":
        raise Exception("Error in the parser")
    if parser.list_read_now != "edge" and not parser.is_open_curly_bracket:
        raise Exception("Necessary bracket not open")
    i = 3
    if len(p) == 2:
       i = 1
    if parser.list_read_now == "alphabet":
        parser.automaton.add_symbol(p[i])
    elif parser.list_read_now == "states":
        parser.automaton.add_state(State(p[i]))
    elif parser.list_read_now == "terminal":
        parser.automaton.add_terminal(p[i])
    elif parser.list_read_now == "edge":
        parser.edge_read_now.add_symbol(p[i])
    	    

def p_close_curly_bracket(p):
    'Close_curly_bracket : CURLY_BRACKET_CLOSE'
    if (parser.list_read_now != "alphabet" and parser.list_read_now != "states" and parser.list_read_now != "terminal") or not parser.is_open_curly_bracket:
        raise Exception("Necessary bracket not open")
    parser.list_read_now = ""
    parser.is_open_curly_bracket = False
    
def p_close_square_bracket(p):
    'Close_square_bracket : SQUARE_BRACKET_CLOSE'
    if parser.list_read_now != "edge" or not parser.is_open_square_bracket:
        raise Exception("Necessary bracket not open")
    parser.list_read_now = ""
    parser.is_open_square_bracket = False
    parser.automaton.add_edge(parser.edge_read_now)
    parser.edge_read_now = Edge()

def p_error(p):
    raise Exception("Syntax error")
    
parser = yacc.yacc()

parser.list_read_now = ""
parser.automaton = Automaton()
parser.edge_read_now = Edge()
parser.is_open_curly_bracket = False
parser.is_open_square_bracket = False
parser.is_valid_automaton = True

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')


def not_valid_automaton(err):
    parser.is_valid_automaton = False
    print(err)
    print("The automaton will not be created")

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
        not_valid_automaton("Error: " + str(e))    
        break

#if parser.is_valid_automaton:
parser.automaton.print_val()
