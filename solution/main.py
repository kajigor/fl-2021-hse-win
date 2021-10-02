import ply.lex as lex
import sys

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE'
}

tokens = ['alphabet', 'vertex', 'edge_name', 'edge', 'machine'] + list(reserved.values())

is_open_edge = False
is_open_machine = False
is_first_vertex = False


def get_name(s):
    name = ""
    current_code = ""
    for i in range(0, len(s)):
        current_code += s[i]
        if len(current_code) == 8:
            name += chr(int(current_code, 2))
            current_code = ""
    return name


def t_alphabet(t):
    r'E([0-1]{8})*E'
    global alphabet
    t.value = get_name(t.value[1:len(t.value) - 1:1])
    return t


def t_edge_name(t):
    r'B([0-1]{8})*B'
    global is_first_vertex, file_out
    is_first_vertex = False
    t.value = get_name(t.value[1:len(t.value) - 1:1])
    return t


def t_vertex(t):
    r'A(0|1)B([0-1]{8})*BA'
    global is_first_vertex, file_out
    vertex_info = "name: " + get_name(t.value[3:(len(t.value) - 2):1]) + ", terminality: " + str(t.value[1] == '1')
    if is_first_vertex:
        t.value = "type: from, " + vertex_info
    else:
        t.value = "type: to, " + vertex_info
    return t


def t_edge(t):
    r'C'
    global is_open_edge, is_first_vertex, file_out
    if not is_open_edge:
        t.value = "Open"
        is_first_vertex = True
        is_open_edge = True
    else:
        t.value = "Close"
        is_open_edge = False
    return t


def t_machine(t):
    r'D'
    global is_open_machine
    if not is_open_machine:
        t.value = "Open"
        is_open_machine = True
    else:
        t.value = "Close"
        is_open_machine = False
    return t


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
    file_out = open(sys.argv[1] + '.out', 'w')
    lexer.input(file_in.read())
    file_in.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
        file_out.write(str(tok))
        file_out.write('\n')
    file_out.close()


main()
