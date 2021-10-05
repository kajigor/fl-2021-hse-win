import ply.yacc as yacc
from lex import tokens
import sys

# автомат -- граф, характеризуется состояними (вершины State) и ребрами перехода (ребра Edges)

class State:
  def __init__(self, number_):
    self.number = number_
    self.symbols = []
    self.type = 'average'
    self.in_edges = []
    self.out_edges = []

  def __eq__(self, other):
    if (self.number == other.number or \
        self.symbols == other.symbols and \
        self.type == other.type and \
        self.in_edges == other.in_edges and \
        self.out_edges == other.out_edges):
        return True
    return False      

  def add_symbol(self, symbol):
    self.symbols.append(symbol)

  def make_terminal(self):
    self.type = 'terminal'

  def add_in_edge(self, edge):
    self.in_edges.append(edge)

  def add_out_edge(self, edge):
    self.out_edges.append(edge)

  def print_to(self):
    print('(', end = '')
    print("number: ", end = "")
    print(self.number, end = ", ")
    print("type: ", end = "")
    print(self.type, end = "")
    print(")")         

class Edge:
  def __init__(self):
    self.from_state = 0
    self.to_state = 0
    self.symbols = []

  def __eq__(self, other):
    if (self.from_state == other.from_state and \
        self.to_state == other.to_state and \
        self.symbols == other.symbols):
        return True
    return False      

  def init_from_state(self, state_number):
    self.from_state = state_number

  def init_to_state(self, state_number):
    self.to_state = state_number    

  def add_symbol(self, symbol):
    self.symbols.append(symbol)  

  def print_to(self):
    print(self.from_state, end = "")
    print(" --> ", end = "")  
    print(self.to_state, end = ", ")
    print("symbols: ", end = "")
    self.symbols.sort()
    print("(", end = "")
    print(', '.join(self.symbols), end = "")
    print(")")    

class Automat:
  def __init__(self):
    self.alphabet_size = 0
    self.alphabet = []
    self.count_states = 0
    self.start_state = -1
    self.count_terminal = 0
    self.terminal_states = []
    self.edges = []
    self.states = []

  def init_alphabet_size(self, size):
    self.alphabet_size = size

  def add_alphabet_symbol(self, symbol):
    self.alphabet.append(symbol)

  def init_count_states(self, count):
    self.count_states = count

  def init_start_state(self, state):
    self.start_state = state

  def init_count_terminal(self, count):
    self.count_terminal = count

  def add_terminal_state(self, state_number):
    self.terminal_states.append(state_number)

  def add_edge(self, edge):
    self.edges.append(edge)  

  def print_automat(self):
    self.alphabet.sort()
    print("Alphabet -- " + str(self.alphabet_size) + " symbol(s):", end="\n")
    print("             (", end = "")
    print(', '.join(self.alphabet), end = "")
    print(")")

    print("Start state:")
    print("             " + str(self.start_state))

    self.terminal_states.sort()
    sarr = [str(a) for a in self.terminal_states]
    print("Terminals -- " + str(len(self.terminal_states)) + " state(s):", end="\n")
    print("             ", end = "")
    print(', '.join(sarr))

    print("All states:")
    for state in self.states:
      print("           ", end = "")
      state.print_to()

    print("Edges:")
    for edge in self.edges:
      print("             ", end = "")
      edge.print_to()

  def check_start_state(self):
    if (self.start_state == -1):
      raise Exception("Start state of the automat has not been detected")

  def check_states_uniqueness(self):
    for i in range(len(self.states)):
      for j in range(i, self.states):
        if (self.states[i] == self.states[j]):
          raise Exception("Automat has identical states")

  def check_alphabet_uniqueness(self):
    for i in range(len(self.alphabet)):
      for j in range(i, self.alphabet):
        if (self.alphabet[i] == self.alphabet[j]):
          raise Exception("Symbols of the alphabet are not unique")

  def check_determinancy(self):
    if (False):
      raise Exception("Automat is not deterministic")  

  def checker(self):
    try:
      heck_start_state()
      check_states_uniqueness()
      check_alphabet_uniqueness()
      check_determinancy()
    except Exception as err:
      print("Error:\n    " + str(err))  


automat = Automat()
current_edge = Edge()      

def p_automaton(p):
  '''Automat : Alphabet
               | States_count
               | Start_state
               | Terminals
               | Edges '''

def p_alphabet(p):
  'Alphabet : ALPHABET COLON NUM DASH OPARENTHESES str_alphabet_symbols CPARENTHESES'
  automat .init_alphabet_size(p[3])

def p_states_count(p):
  'States_count : Q COLON NUM'
  automat.init_count_states(p[3])
  for i in range(p[3]):
      automat.states.append(State(i))

def p_start_state(p):
  'Start_state : START COLON NUM'
  automat.init_start_state(p[3])

def p_terminals(p):
  'Terminals : T COLON NUM DASH str_terminal_nums'

def p_edges(p):
  'Edges : EDGES COLON str_edges'

def p_str_alphabet_symbols(p):
  '''str_alphabet_symbols : SYMBOL COMMA str_alphabet_symbols
                          | SYMBOL'''
  automat.add_alphabet_symbol(p[1])    

def p_str_terminal_nums(p):
  '''str_terminal_nums : NUM COMMA str_terminal_nums
                       | NUM''' 
  automat.add_terminal_state(p[1])
  automat.states[p[1]].make_terminal()                               

def p_str_edges(p):
  '''str_edges : str_edge COMMA str_edges
               | str_edge'''

def p_str_edge(p):
  '''str_edge : OPARENTHESES NUM SEMICOLON NUM SEMICOLON str_edge_symbols end_edge''' 
  current_edge.init_from_state(p[2])   
  current_edge.init_to_state(p[4])

def p_str_edge_symbols(p):
  '''str_edge_symbols : SYMBOL COMMA str_edge_symbols
                      | SYMBOL'''   
  current_edge.add_symbol(p[1]) 

def p_end_edge(p):
  '''end_edge : CPARENTHESES'''
  automat.add_edge(current_edge)  
  automat.states[current_edge.from_state].add_out_edge(current_edge) 
  automat.states[current_edge.to_state].add_in_edge(current_edge)                                                          

def p_error(p):
  raise Exception("Syntax error")

parser = yacc.yacc()

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')

# обработка входных данных файла
while True:
  try:
    s = input()
  except EOFError:
    break
  if not s:
    continue
  try:
    result = parser.parse(s)
  except Exception as err:
    print("Error: " + str(err))

automat.print_automat()    