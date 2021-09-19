import ply.lex as lex
import sys

file_out = open(sys.argv[1] + '.out', 'w')

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}

tokens = [
             'Vertex',
             'Name',
             'Edge',
             'Machine'
         ] + list(reserved.values())

is_open_edge = False
is_first_vertex = False


def get_name(s):
    name = ""
    current_code = ""
    for i in range(0, len(s)):
        current_code += s[i]
        if len(current_code) == 8:
            name += chr(int(current_code, 2))
            current_code = ""
    return "\"" + name + "\""


def t_Name(t):
    r'B([0-1]{8})*B'
    global is_first_vertex, file_out
    is_first_vertex = False
    file_out.write("name is " + get_name(t.value[1:len(t.value) - 1:1]) + " ")


def t_Vertex(t):
    r'A(0|1)B([0-1]{8})*BA'
    global is_first_vertex, file_out
    vertex_info = "(vertex " + get_name(t.value[3:(len(t.value) - 2):1]) + " with terminality: " + str(
        t.value[1] == '1') + ")"
    if is_first_vertex:
        file_out.write("from " + vertex_info + " ")
    else:
        file_out.write("to " + vertex_info + "\n")
    return t


def t_Edge(t):
    r'C'
    global is_open_edge, is_first_vertex, file_out
    if not is_open_edge:
        file_out.write("Found edge ")
        is_first_vertex = True
        is_open_edge = True
    else:
        is_open_edge = False


def t_Machine(t):
    r'D'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    global file_out
    file_out.write("Illegal character '%s'" % t.value[0])
    exit()


def main():
    global file_out
    lexer = lex.lex()
    file_in = open(sys.argv[1], 'r')
    lexer.input(file_in.read())
    file_in.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
    file_out.close()


main()
