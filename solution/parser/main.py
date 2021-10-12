import ply.lex as lex

tokens = ['method', 'var_init', 'last_par', 'body_begin', 'body_end',
          'skip', 'return', 'par', 'var', 'if', 'else', 'operator', 'for', 'condition']
file_out = open("output.dot", 'w')
stack = ["v_0"]
index_of_vertex = 1
operators = {"^": [0, True], "*": [1, False], "/": [1, False], "+": [2, False], "-": [2, False], "==": [3, True],
             "/=": [3, True], "<=": [3, True], "<": [3, True], ">=": [3, True], ">": [3, True], "!": [4, True],
             "&&": [5, True], "||": [6, True], "=": [7, True]}  # [prio, is_not_left_associativity]


def error(ch):
    file_out.write("}\n")
    file_out.close()
    print("Illegal character '%s'" % ch)
    exit()


def add_edge(a, b):
    file_out.write(a + " -> " + b + "\n")


def create_name(name):
    global index_of_vertex
    result = "v_" + str(index_of_vertex)
    index_of_vertex += 1
    file_out.write(result + " [label=<" + name + ">]\n")
    return result


def create_type_vertex(type_):
    return create_name("Type=\"" + type_ + "\"")


def create_parameters_list_vertex():
    return create_name("Parameters list")


def create_parameter_vertex():
    return create_name("Parameter")


def create_name_vertex(name):
    return create_name("Name=\"" + name + "\"")


def create_value_vertex():
    return create_name("Value")


def index_checking(s, index, arr):
    if len(s) <= index:
        return False
    for i in arr:
        if s[index] == i:
            return False
    return True


def get_type(s):
    result = ""
    index = 0
    while index_checking(s, index, {' '}):
        result += s[index]
        index += 1
    return result


def char_checking(ch):
    if ch == '>':
        return "&gt;"
    if ch == '<':
        return "&lt;"
    if ch == '&':
        return "&amp;"
    if ch != ' ':
        return ch
    return ''


def get_var_value(s):
    index = 0
    result = ""
    while index_checking(s, index, {'='}):
        index += 1
    index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index_checking(s, index, {';', ']'}):
        result += char_checking(s[index])
        index += 1
    return result


def get_name(s):
    index = 0
    result = ""
    while index_checking(s, index, {' '}):
        index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index_checking(s, index, {' ', '(', ',', ')'}):
        result += char_checking(s[index])
        index += 1
    return result


def get_return_value(s):
    result = ""
    index = 0
    while index_checking(s, index, {' '}):
        index += 1
    while index_checking(s, index, {';'}):
        result += char_checking(s[index])
        index += 1
    return result


def get_if_value(s):
    result = ""
    index = 0
    while index_checking(s, index, {'('}):
        index += 1
    index += 1
    while index_checking(s, index, {')'}):
        result += char_checking(s[index])
        index += 1
    return result


def get_operator_name(s):
    result = ""
    index = 0
    while index_checking(s, index, {' '}):  # type
        index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index_checking(s, index, {' '}):  # operator_x_y
        index += 1
    while index < len(s) and s[index] == ' ':
        index += 1
    while index_checking(s, index, {' ', '('}):
        result += char_checking(s[index])
        index += 1
    return result


def get_prio(s):
    result = ""
    index = 0
    while index_checking(s, index, {'_'}):
        index += 1
    index += 1
    while index_checking(s, index, {'_'}):
        if s[index] != ' ':
            result += s[index]
        index += 1
    return result


def get_assoc(s):
    result = ""
    index = 0
    while index_checking(s, index, {'_'}):
        index += 1
    index += 1
    while index_checking(s, index, {'_'}):
        index += 1
    index += 1
    while index_checking(s, index, {' '}):
        result += s[index]
        index += 1
    return result


def get_condition(s):
    result = ""
    index = 0
    while index < len(s):
        if s[index] != ' ' and s[index] != ']' and s[index] != ';':
            result += s[index]
        index += 1
    return expression_process(result)


def init_vertex(vertex, s):
    add_edge(stack[-1], vertex)
    add_edge(vertex, create_type_vertex(get_type(s)))
    add_edge(vertex, create_name_vertex(get_name(s)))


def init_value_tree(expression, new_vertex):
    value_vertex = create_value_vertex()
    add_edge(new_vertex, value_vertex)
    stack.append(value_vertex)
    add_edge(stack[-1], expression_process(expression))
    stack.pop()


def is_digit(ch):
    return '0' <= ch <= '9'


def is_letter(ch):
    return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'


def expression_process(s):
    arr = []
    index = 0
    while index < len(s):
        if s[index] == ' ':
            # space
            index += 1
        elif s[index] == '(':
            # brackets
            bal = 1
            index += 1
            while index < len(s) and bal != 0:
                if s[index] == '(':
                    bal += 1
                if s[index] == ')':
                    bal -= 1
                index += 1
        elif is_digit(s[index]) or (s[index] == '-' and len(s) != index - 1 and is_digit(s[index + 1]) and
                                    (index == 0 or s[index - 1] == '(')):
            # number
            index += 1
            while index < len(s) and is_digit(s[index]):
                index += 1
        elif s[index] == "\"":
            # string
            index += 1
            while len(s) < index and s[index] != "\"":
                index += 1
        elif is_letter(s[index]):
            # word
            while index < len(s) and (is_letter(s[index]) or is_digit(s[index]) or s[index] == '_'):
                index += 1
        else:
            # operator
            result = ""
            start = index
            while index < len(s) and (s[index] != ' ' and s[index] != '(' and s[index] != ')'
                                      and not is_letter(s[index]) and not is_digit(s[index])):
                result += s[index]
                index += 1
            if result in operators:
                if len(arr) == 0 or operators[result][0] > arr[0][0] or (
                        operators[result][0] == arr[0][0] and not operators[result][1]):
                    arr = [operators[result], [start, index]]
            else:
                error(s[index])
    if arr:
        # external operator found
        cur_operator = s[arr[1][0]:arr[1][1]]
        for i in range(0, len(cur_operator)):
            if i == len(cur_operator) - 1:
                cur_operator = cur_operator[:i:] + char_checking(cur_operator[i])
            elif i == 0:
                cur_operator = char_checking(cur_operator[i]) + cur_operator[i + 1::]
            else:
                cur_operator = cur_operator[:i:] + char_checking(cur_operator[i]) + cur_operator[i + 1::]
        new_vertex = create_name("Operator=\"" + cur_operator + "\"")
        stack.append(new_vertex)
        add_edge(stack[-1], expression_process(s[0:arr[1][0]:]))
        add_edge(stack[-1], expression_process(s[arr[1][1]::]))
        stack.pop()
        return new_vertex
    else:
        # external operator not found
        index = 0
        if s == "":
            # empty
            return create_name("")
        if is_digit(s[0]) or (s[0] == '-' and len(s) != 1 and is_digit(s[1])):
            # alone number
            if s[0] == '-':
                new_vertex = create_name("Unary minus")
                add_edge(new_vertex, create_name("Number=\"" + s[1::] + "\""))
                return new_vertex
            return create_name("Number=\"" + s + "\"")
        if len(s) >= 2 and s[0] == "\"" and s[len(s) - 1] == "\"":
            return create_name("String=" + s)
        if len(s) >= 2 and s[0] == '(' and s[len(s) - 1] == ')':
            # expression in brackets
            new_vertex = create_name("Brackets")
            stack.append(new_vertex)
            add_edge(stack[-1], expression_process(s[1:len(s) - 1:]))
            stack.pop()
            return new_vertex
        if len(s) > 2 and is_letter(s[index]):
            # alone variable or method
            name = ""
            while index < len(s) and (is_letter(s[index]) or is_digit(s[index]) or s[index] == '_'):
                name += char_checking(s[index])
                index += 1
            if len(s) == index:
                # alone variable
                return create_name("Variable=\"" + name + "\"")
            if s[index] != '(':
                error(s[index])
            # alone method
            new_vertex = create_name("Method assignment")
            stack.append(new_vertex)
            add_edge(stack[-1], create_name_vertex(name))
            stack.append(create_parameters_list_vertex())
            add_edge(stack[-2], stack[-1])
            index += 1
            while index < len(s) and s[index] != ')':
                result = ""
                while index < len(s) and s[index] != ',' and s[index] != ')':
                    result += s[index]
                    index += 1
                index += 1
                parameter_vertex = create_parameter_vertex()
                add_edge(stack[-1], parameter_vertex)
                stack.append(parameter_vertex)
                add_edge(stack[-1], expression_process(result))
                stack.pop()
            stack.pop()
            stack.pop()
            return new_vertex
        return create_name("Variable=\"" + s + "\"")


def t_method(t):
    r"""(int|int2|string)\s+\w*\s*\("""
    new_vertex = create_name("Method")
    init_vertex(new_vertex, t.value)
    stack.append(new_vertex)
    stack.append(create_parameters_list_vertex())
    add_edge(stack[-2], stack[-1])
    return t


def t_body_begin(t):
    r"""\{"""
    new_vertex = create_name("Body")
    add_edge(stack[-1], new_vertex)
    stack.append(new_vertex)
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


def t_var_init(t):
    r"""(int|int2|string)\s+\w+\s*[^\/&^<&^>&^=&(\w|\s)]=\s*[^;]*;"""
    new_vertex = create_name("Variable init")
    init_vertex(new_vertex, t.value)
    init_value_tree(get_var_value(t.value), new_vertex)
    return t


def t_return(t):
    r"""return.*;"""
    new_vertex = create_name("Return")
    add_edge(stack[-1], new_vertex)
    init_value_tree(get_return_value(t.value), new_vertex)
    return t


def t_var(t):
    r"""\w*\s*[^\/&^<&^>&^=&(\w|\s)]=.*(;|\])"""
    new_vertex = create_name("Variable assignment")
    add_edge(stack[-1], new_vertex)
    add_edge(new_vertex, create_name_vertex(get_type(t.value)))  # get_type, because of line starting
    init_value_tree(get_var_value(t.value), new_vertex)
    return t


def t_if(t):
    r"""if\s*\("""
    new_vertex = create_name("If statement")
    add_edge(stack[-1], new_vertex)
    stack.append(new_vertex)
    return t


def t_else(t):
    r"""\}\s*else"""
    new_vertex = create_name("Else statement")
    stack.pop()
    add_edge(stack[-1], new_vertex)
    stack.append(new_vertex)
    return t


def t_operator(t):
    r"""(int|int2|string)\s+operator\_\d+\_\d\s+.+\s*\("""
    new_vertex = create_name("Operator")
    add_edge(stack[-1], new_vertex)
    add_edge(new_vertex, create_name_vertex(get_operator_name(t.value)))
    add_edge(new_vertex, create_type_vertex(get_type(t.value)))
    add_edge(new_vertex, create_name("Priority=\"" + get_prio(t.value) + "\""))
    add_edge(new_vertex, create_name("Associativity=\"" + get_assoc(t.value) + "\""))
    operators[get_operator_name(t.value)] = [int(get_prio(t.value)), get_assoc(t.value) != 1]
    stack.append(new_vertex)
    stack.append(create_parameters_list_vertex())
    add_edge(stack[-2], stack[-1])
    return t


def t_for(t):
    r"""for\s*\["""
    new_vertex = create_name("For statement")
    add_edge(stack[-1], new_vertex)
    stack.append(new_vertex)
    return t


def t_body_end(t):
    r"""\}"""
    stack.pop()  # Body exit
    stack.pop()  # Statement exit
    return t


def t_skip(t):
    r"""(\s+|\n|\]|\))"""
    return t


def t_condition(t):
    r"""([^\;&^\]&^\n]|[\^])+(\)|\]|\;)"""
    new_vertex = create_name("Condition")
    add_edge(stack[-1], new_vertex)
    stack.append(new_vertex)
    add_edge(stack[-1], get_condition(t.value[:len(t.value) - 1:]))
    stack.pop()
    return t


def t_error(t):
    error(t.value[0])
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
