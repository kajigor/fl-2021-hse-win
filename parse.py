import ply.yacc as yacc
from copy import deepcopy
from lex import tokens
from lex import lexer
import sys


class Vertex:
    def __init__(self, is_start: bool, is_term: bool, name: str, transitions: list):
        self.is_start = is_start
        self.is_term = is_term
        self.name = name
        self.transitions = transitions


class Transition:
    def __init__(self, to: str, word: str):
        self.to = to
        self.word = word


class Alphabet:
    def __init__(self, words: list):
        self.words = words


class DFA:
    def __init__(self, alphabet: Alphabet, vert: list):
        self.alphabet = alphabet
        self.vert = vert


def p_dfa(p):
    'dfa : alphabet_def vertex_list_def'
    p[0] = DFA(p[1], p[2])


def p_transition_def(p):
    'transition_def : VERTEX WITH WORD'
    p[0] = Transition(p[1], p[3])


def p_vertex_list_def(p):
    '''vertex_list_def :
                        | vertex_list_def vertex_def
                        | vertex_def'''
    if len(p) == 3:
        p[0] = deepcopy(p[1])
        p[0].append(p[2])
    else:
        p[0] = [p[1]]


def p_alphabet_def(p):
    'alphabet_def : ALPHABET words_def SEMICOLON'
    # print("alf")
    p[0] = Alphabet(p[2])

def p_words_def(p):
    '''words_def :
                | words_def WORD
                | WORD'''
    if len(p) == 3:
        p[0] = deepcopy(p[1])
        p[0].append(p[2])
    else:
        p[0] = [p[1]]


# TODO
def p_vertex_def(p):
    '''vertex_def :
                | START VERTEX transition_list_def SEMICOLON
                | TERMINAL VERTEX transition_list_def SEMICOLON
                | VERTEX transition_list_def SEMICOLON'''
    # TODO START TERMINAL
    if len(p) == 4:
        p[0] = Vertex(False, False, p[1], p[2])
    else:
        p[0] = Vertex(p[1] == 'start', p[1] == 'terminal', p[2], p[3])


def p_transition_list_def(p):
    '''transition_list_def :
                            | transition_list_def transition_def
                            | transition_def'''
    if len(p) == 3:
        p[0] = deepcopy(p[1])
        p[0].append(p[2])
    else:
        p[0] = [p[1]]


def p_error(p):
    print(p)
    print("Syntax error")

def check_start(dfa: DFA):
    for i in dfa.vert:
        if i.is_start:
            return True
    return False

def check_unique_vertexes(dfa: DFA):
    a = set()
    for i in dfa.vert:
        a.add(i.name)
    return len(a) == len(dfa.vert)

def check_unique_words(dfa: DFA):
    return len(list(set(dfa.alphabet.words))) == len(dfa.vert)

def check_determination(dfa: DFA):
    for i in dfa.vert:
        a = set()
        for j in i.transitions:
            a.add(j.to)
        if len(a) != len(i.transitions):
            return False
    return True

def check_fullness(dfa: DFA):
    a = set(dfa.alphabet.words)
    for i in dfa.vert:
        b = set()
        for j in i.transitions:
            b.add(j.word)
        if a != b:
            return False
    return True

def check_all(dfa: DFA, output):
    if check_unique_vertexes(dfa):
        output.write("Running \"check_unique_vertexes\": ok\n")
    else:
        output.write("Running \"check_unique_vertexes\": fail\n")

    if check_start(dfa):
        output.write("Running \"check_start\": ok\n")
    else:
        output.write("Running \"check_start\": fail\n")

    if check_unique_words(dfa):
        output.write("Running \"check_unique_words\": ok\n")
    else:
        output.write("Running \"check_unique_words\": fail\n")

    if check_determination(dfa):
        output.write("Running \"check_determination\": ok\n")
    else:
        output.write("Running \"check_determination\": fail\n")

    if check_fullness(dfa):
        output.write("Running \"check_fullness\": ok\n")
    else:
        output.write("Running \"check_fullness\": fail\n")

parser = yacc.yacc()

try:
    s = ''.join(open(sys.argv[1]).readlines())
    dfa = parser.parse(s)
except:
    print("Unable to open file")
    exit(1)

output = open(sys.argv[1] + '.out', 'w')

output.write(str(dfa.alphabet.words) + '\n')
for i in dfa.vert:
    output.write("vertex name: " + i.name + '\n')
    output.write("start: " + str(i.is_start) + '\n')
    output.write("terminal: " + str(i.is_term) + '\n')
    for j in i.transitions:
        output.write("{" + j.to + ',' + j.word + "} ")
    output.write("\n-----------------\n")

check_all(dfa, output)

