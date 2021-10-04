import sys
import ply.yacc as yacc

from lex import tokens

class Automate:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts


def p_automate(p):
    '''automate : states start end alphabet function'''
    p[0] = Automate("AUTOMATE", p[1:])

def p_states_definition(p):
    'states_definition : EQUAL BRACKET state_list BRACKET SEMICOLON '
    p[0] = p[3]

def p_states(p):
    'states : STATES states_definition'
    p[0] = Automate("STATES", p[2])

def p_start(p):
    'start : START states_definition'
    p[0] = Automate("START", p[2])

def p_end(p):
    'end : END states_definition'
    p[0] = Automate("END", p[2])

def p_error(p):
    print("Syntax error")


def p_state_list(p):
    '''state_list : state state_list
                  | state
                  | '''
    p[0] = []
    if (len(p) == 1):
        return
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

def p_state(p):
    'state : STATE'
    p[0] = p[1]


def p_transfer(p):
    'transfer : TRANSFER'
    p[0] = p[1]


def p_transfer_list(p):
    '''transfer_list : transfer transfer_list
                     | transfer'''
    p[0] = []
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

def p_alphabet_definition(p):
    'alphabet_definition : EQUAL BRACKET transfer_list BRACKET SEMICOLON'
    p[0] = p[3]

def p_alphabet(p):
    'alphabet : ALPHABET alphabet_definition'
    p[0] = Automate("ALPHABET", p[2])

def p_function(p):
    'function : FUNCTION function_def'
    p[0] = Automate("FUNCTION", p[2])

def p_function_def(p):
    'function_def : EQUAL BRACKET function_list BRACKET SEMICOLON'
    p[0] = p[3]

def p_where(p):
    'where : state transfer state'
    p[0] = [p[1], p[2], p[3]]

def p_function_list(p):
    '''function_list : where function_list
                     | where'''
    p[0] = []
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

def print_error(error_string):
    print("ERROR: " + error_string)

def test_unique(automate):
    for part in automate.parts[:4]:
        if len(part.parts) > len(set(part.parts)):
            print_error(part.type + " not unique")

def test_deterministic(automate):
    function = automate.parts[4]
    if len(set((start, key) for start, key, _ in function.parts)) != len(function.parts):
        print_error("automate not deterministic")

def test_automate_full(automate):
    function = automate.parts[4]
    states = automate.parts[0]
    alphabet = automate.parts[3]
    if len(function.parts) != len(states.parts) * len(alphabet.parts):
        print_error("automate not full")

def test_correct_transfers(automate):
    function = automate.parts[4]
    alphabet = automate.parts[3]

    for _, transfer, _ in function.parts:
        if transfer not in alphabet.parts:
            print_error("transfer: " + transfer + " is not exist")

def test_correct_states(automate):
    states = automate.parts[0]
    start, end = automate.parts[1:3]

    for state in start.parts + end.parts:
        if state not in states.parts:
            print_error("state: \"" + state + "\" is not exist")

def test_correct_start(automate):
    start = automate.parts[1]
    if (len(start.parts) == 0):
        print_error("start is empty")

sys.stdout = open(sys.argv[1] + '.out', 'w')

parser = yacc.yacc()
s = open(sys.argv[1], 'r').read()

result = parser.parse(s)
print(result)

test_correct_transfers(result)
test_correct_states(result)
test_correct_start(result)
test_unique(result)
test_deterministic(result)
test_automate_full(result)
