import ply.yacc as yacc
import sys
from lex import tokens


class Result:
    def __init__(self):
        self.alphabet = []
        self.edges = []
        self.start_vertex = []
        self.terminal_vertex = []
        self.another_vertex = []
        self.all_vertex = []
        # self.alphabet_from_vertex = {}
        # self.vertexes_from_vertex = []
    def get_answer(self):
        print("alphabet:")
        print(self.alphabet)
        print("Init vertex:")
        print(self.start_vertex)
        print("Terminal vertex:")
        print(self.terminal_vertex)
        print("Not Init or Terminal vertex:")
        print(self.another_vertex)
        for i in self.edges:
            print("From: " + i[0] + ' To: ' + i[1] + " By this alphabet: ", end = ' ')
            print(i[2])

    def check_logic_mistakes(self):
        for v in self.all_vertex:
            if self.all_vertex.count(v) > 1:
                raise Exception("The same Name from different vertex, is " + v)
        for v in self.alphabet:
            if self.alphabet.count(v) > 1:
                raise Exception("The same symbol in alphabet - " + v)
        if len(self.start_vertex) > 1:
            raise Exception("More than one start vertex")
        if len(self.start_vertex) == 0:
            raise Exception("No start vertex")
        for edge in self.edges:
            for el in edge[2]:
                if not el in self.alphabet:
                    raise Exception("The symbol is not from the alphabet - " + el)
    def check_full(self):
        for v in self.all_vertex:
            a = []
            for edge in self.edges:
                if (edge[0] == v):
                    a += edge[2]
            for v in self.alphabet:
                if a.count(v) != 1:
                    return False
        return True
    def check_deter(self):
        for v in self.all_vertex:
            a = []
            for edge in self.edges:
                if (edge[0] == v):
                    a += edge[2]
            for v in a:
                if a.count(v) != 1:
                    return False
        return True

    def get_place(self, v):
        if (v in self.terminal_vertex):
            return "Terminal"
        if (v in self.start_vertex):
            return "Start"
        if (v in self.another_vertex):
            return "Another"

    def vertex_from(self, v):
        a = []
        for edge in self.edges:
            if (edge[1] == v):
                a += edge[2]
        return a

    def vertex_to(self, v):
        a = []
        for edge in self.edges:
            if (edge[0] == v):
                a += edge[2]
        return a

    def check_uniq(self):
        for v1 in self.all_vertex:
            for v2 in self.all_vertex:
                self.check_two(v1, v2)

    def check_two(self, v1, v2):
        if (v1 != v2) and (self.get_place(v1) == self.get_place(v2)):
            for v in self.vertex_to(v1):
                if not v in self.vertex_to(v2):
                    return
            for v in self.vertex_from(v1):
                if not v in self.vertex_from(v2):
                    return
            print(v1 + " and " + v2 + " are same")

def p_auto(p):
    '''Auto : alphabet
            | vertex
            | edge '''

def p_vertex(p):
    '''vertex : VERTEX NAME SEMICOLON TRUE SEMICOLON TRUE
              | VERTEX NAME SEMICOLON FALSE SEMICOLON TRUE
              | VERTEX NAME SEMICOLON TRUE SEMICOLON FALSE
              | VERTEX NAME SEMICOLON FALSE SEMICOLON FALSE'''
    used = False
    parser.my_result.all_vertex.append(p[2])
    if p[4] == 'T':
        used = True
        parser.my_result.start_vertex.append(p[2])
    if p[6] == 'T':
        used = True
        parser.my_result.terminal_vertex.append(p[2])
    if not used:
        parser.my_result.another_vertex.append(p[2])

def p_alphabet(p):
    '''alphabet : ALPHABET CURLY_BRAKETS_open list CURLY_BRAKETS_close'''
    parser.my_result.alphabet += parser.current_list
    parser.current_list = []

def p_edge(p):
    '''edge : EDGE NAME SEMICOLON NAME SEMICOLON CURLY_BRAKETS_open list CURLY_BRAKETS_close'''
    parser.my_result.edges.append(list([p[2], p[4], parser.current_list]))
    # parser.my_result.alphabet_from_vertex[p[2]] += parser.current_list
    # parser.my_result.vertexes_from_vertex[p[2]].append(p[4])
    parser.current_list = []

def p_list(p):
    ''' list :
             | NAME COMMA list
             | NAME '''
    parser.current_list.append(p[1])


def p_error(p):
    raise Exception("Syntax error")

parser = yacc.yacc()

parser.my_result = Result()
parser.current_list = []
parser.is_ok = True

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')


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
        print("Error: " + str(e))
        parser.is_ok = False
        break

if parser.is_ok:
    try:
        parser.my_result.check_logic_mistakes()
        parser.my_result.get_answer()
        print("Is auto full - " + str(parser.my_result.check_full()))
        print("Is auto deter - " + str(parser.my_result.check_deter()))
        parser.my_result.check_uniq()
        print("Valid")
    except Exception as e:
        print(str(e))