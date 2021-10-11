import ply.lex as lex

tokens = ['method', 'var_init', 'last_par', 'body_begin', 'body_end',
          'skip', 'return', 'par', 'var', 'if', 'else', 'operator', 'for', 'condition']
file_out = open("output.dot", 'w')
stack = ["v_0"]
index_of_vertex = 1
to_arrow = " -> "
operators = {"^": [2, True], "--": [3, True], "*": [4, False],
             "/": [4, False], "+": [5, False], "-": [5, False], "==": [6, True], "/=": [6, True], "<=": [6, True],
             "<": [6, True], ">=": [6, True], ">": [6, True], "!": [7, True], "&&": [8, True],
             "||": [9, True], "=": [10, True]}  # [prio, is_not_left_associativity]


def error(ch):
    file_out.write("}\n")
    file_out.close()
    print("Illegal character '%s'" % ch)
    exit()


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
    file_out.write(stack[-1] + to_arrow + vertex + "\n")
    file_out.write(vertex + to_arrow + create_name_vertex(get_name(s)) + "\n")
    file_out.write(vertex + to_arrow + create_type_vertex(get_type(s)) + "\n")


def init_value_tree(expression, new_vertex):
    value_vertex = create_value_vertex()
    file_out.write(new_vertex + to_arrow + value_vertex + "\n")
    stack.append(value_vertex)
    file_out.write(stack[-1] + to_arrow + expression_process(expression) + "\n")
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
        elif is_digit(s[index]):
            # number
            while index < len(s) and is_digit(s[index]):
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
        file_out.write(stack[-1] + to_arrow + expression_process(s[0:arr[1][0]:]) + "\n")
        file_out.write(stack[-1] + to_arrow + expression_process(s[arr[1][1]::]) + "\n")
        stack.pop()
        return new_vertex
    else:
        # external operator not found
        index = 0
        if s == "":
            # empty
            return create_name("")
        if is_digit(s[0]):
            # alone number
            return create_name("Number=\"" + s + "\"")
        if len(s) >= 2 and s[0] == '(' and s[len(s) - 1] == ')':
            # expression in brackets
            new_vertex = create_name("Brackets")
            stack.append(new_vertex)
            file_out.write(stack[-1] + to_arrow + expression_process(s[1:len(s) - 1:]) + "\n")
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
            file_out.write(stack[-1] + to_arrow + create_name_vertex(name) + "\n")
            stack.append(create_parameters_list_vertex())
            file_out.write(stack[-2] + to_arrow + stack[-1] + "\n")
            index += 1
            while index < len(s) and s[index] != ')':
                result = ""
                while index < len(s) and s[index] != ',' and s[index] != ')':
                    result += s[index]
                    index += 1
                index += 1
                parameter_vertex = create_parameter_vertex()
                file_out.write(stack[-1] + to_arrow + parameter_vertex + "\n")
                stack.append(parameter_vertex)
                file_out.write(stack[-1] + to_arrow + expression_process(result) + "\n")
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
    file_out.write(stack[-2] + to_arrow + stack[-1] + "\n")
    return t


def t_body_begin(t):
    r"""\{"""
    new_vertex = create_name("Body")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
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
    r"""(int|int2|string)\s+\w+\s*=\s*[^;]*;"""
    new_vertex = create_name("Variable init")
    init_vertex(new_vertex, t.value)
    init_value_tree(get_var_value(t.value), new_vertex)
    return t


def t_return(t):
    r"""return.*;"""
    new_vertex = create_name("Return")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    init_value_tree(get_return_value(t.value), new_vertex)
    return t


def t_var(t):
    r"""\w*\s*[^=]=[^=]\s*.*(;|\])"""
    new_vertex = create_name("Variable assignment")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    file_out.write(
        new_vertex + to_arrow + create_name_vertex(get_type(t.value)) + "\n")  # get_type, because of line starting
    init_value_tree(get_var_value(t.value), new_vertex)
    return t


def t_if(t):
    r"""if\s*\("""
    new_vertex = create_name("If statement")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    stack.append(new_vertex)
    return t


def t_else(t):
    r"""\}\s*else"""
    new_vertex = create_name("Else statement")
    stack.pop()
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    stack.append(new_vertex)
    return t


def t_operator(t):
    r"""(int|int2|string)\s+operator\_\d+\_\d\s+.+\s*\("""
    new_vertex = create_name("Operator")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    file_out.write(new_vertex + to_arrow + create_name_vertex(get_operator_name(t.value)) + "\n")
    file_out.write(new_vertex + to_arrow + create_type_vertex(get_type(t.value)) + "\n")
    file_out.write(new_vertex + to_arrow + create_name("Priority=\"" + get_prio(t.value) + "\"") + "\n")
    file_out.write(new_vertex + to_arrow + create_name("Associativity=\"" + get_assoc(t.value) + "\"") + "\n")
    operators[get_operator_name(t.value)] = [int(get_prio(t.value)), get_assoc(t.value) != 1]
    stack.append(new_vertex)
    stack.append(create_parameters_list_vertex())
    file_out.write(stack[-2] + to_arrow + stack[-1] + "\n")
    return t


def t_for(t):
    r"""for\s*\["""
    new_vertex = create_name("For statement")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
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
    r"""[^\;&^\]&^\n]+(\)|\]|\;)"""  # TODO think, how to use ^
    new_vertex = create_name("Condition")
    file_out.write(stack[-1] + to_arrow + new_vertex + "\n")
    stack.append(new_vertex)
    file_out.write(stack[-1] + to_arrow + get_condition(t.value[:len(t.value) - 1:]) + "\n")
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
