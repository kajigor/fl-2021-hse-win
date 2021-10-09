import ply.lex as lex

tokens = ['method', 'var', 'last_par', 'body_begin', 'body_end', 'skip', 'return', 'par']
file_out = open("output.dot", 'w')
stack = ["v_0"]
index_of_vertex = 1
to_arrow = " -> "


def create_name(name):
    global index_of_vertex
    result = "v_" + str(index_of_vertex)
    index_of_vertex += 1
    file_out.write(result + " [label=<" + name + ">]\n")
    return result


def create_method_vertex():
    return create_name("Method")


def create_type_vertex(name):
    return create_name("Type=\"" + name + "\"")


def create_parameters_list_vertex():
    return create_name("Parameters list")


def create_body_vertex():
    return create_name("Body")


def create_parameter_vertex():
    return create_name("Parameter")


def create_name_vertex(name):
    return create_name("Name=\"" + name + "\"")


def create_var_vertex():
    return create_name("Variable")


def create_var_value_vertex(value):
    return create_name("Value=\"" + value + "\"")


def create_return_vertex():
    return create_name("Return")


def get_type(s):
    result = ""
    index = 0
    while index < len(s) and s[index] != ' ':
        result += s[index]
        index += 1
    return result


def get_var_value(s):
    index = 0
    result = ""
    while index < len(s) and s[index] != '=':
        index += 1
    index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index < len(s) and s[index] != ';':
        if s[index] != ' ':
            result += s[index]
        index += 1
    return result


def get_name(s):
    index = 0
    result = ""
    while index < len(s) and s[index] != ' ':
        index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index < len(s) and (s[index] != ' ' and s[index] != '(' and s[index] != ',' and s[index] != ')'):
        result += s[index]
        index += 1
    return result


def get_return_value(s):
    result = ""
    index = 0
    while index < len(s) and s[index] != ' ':
        index += 1
    while index < len(s) and s[index] != ';':
        if s[index] != ' ':
            result += s[index]
        index += 1
    return result


def init_vertex(vertex, s):
    file_out.write(stack[-1] + to_arrow + vertex + "\n")
    file_out.write(vertex + to_arrow + create_name_vertex(get_name(s)) + "\n")
    file_out.write(vertex + to_arrow + create_type_vertex(get_type(s)) + "\n")


def t_method(t):
    r"""(int|int2|string)\s+\w*\("""
    new_vertex = create_method_vertex()
    init_vertex(new_vertex, t.value)
    stack.append(new_vertex)
    stack.append(create_parameters_list_vertex())
    file_out.write(stack[-2] + to_arrow + stack[-1] + "\n")
    return t


def t_body_begin(t):
    r"""\{"""
    new_vertex = create_body_vertex()
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    stack.append(new_vertex)
    return t


def t_body_end(t):
    r"""\}"""
    stack.pop()
    stack.pop()
    return t


def t_par(t):
    r"""(int|int2|string)\s+\w+\s*\,"""
    new_vertex = create_parameter_vertex()
    init_vertex(new_vertex, t.value)
    return t


def t_last_par(t):
    r"""((int|int2|string)\s+\w+)?\s*\)"""
    if get_name(t.value) != "":
        new_vertex = create_parameter_vertex()
        init_vertex(new_vertex, t.value)
    stack.pop()
    return t


def t_var(t):
    r"""(int|int2|string)\s+\w+\s*=\s*.*;"""
    new_vertex = create_var_vertex()
    init_vertex(new_vertex, t.value)
    file_out.write(new_vertex + to_arrow + create_var_value_vertex(get_var_value(t.value)) + "\n")
    return t


def t_return(t):
    r"""return.*;"""
    new_vertex = create_return_vertex()
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    file_out.write(new_vertex + to_arrow + create_type_vertex(get_return_value(t.value)) + "\n")
    return t


def t_skip(t):
    r"""(\s+|\n)"""
    return t


def t_error(t):
    file_out.write("}\n")
    file_out.close()
    print("Illegal character '%s'" % t.value[0])
    exit()
    return t


def main():
    file_out.write("digraph {\n")
    file_out.write("v_0 [label=<root (Methods list)>]\n")
    lexer = lex.lex()
    file_in = open("input.txt", 'r')
    lexer.input(file_in.read())
    file_in.close()
    while True:
        tok = lexer.token()
        if not tok:
            break
    file_out.write("}\n")
    file_out.close()


main()
