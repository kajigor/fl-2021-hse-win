import random
import datetime
from recursive_parser import solve, arithmetic_operators
import string
from yacc import solve_yacc

file_size_range = (int(1e5), int(1e6))
variable_name_max_len = 10
number_max_len = 10
expr_max_len = 300
spaces_prob = 0.2
spaces_max_cnt = 5
bracket_prob = 0.05


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def generate_random_number(length):
    num_len = random.randrange(1, length)
    return random.randrange(10**(num_len - 1), 10**num_len)


def generate_random_arithmetic_operator():
    return random.choice(arithmetic_operators)


def generate_random_arithmetic_expr(length):
    res: str = str()
    balance = int(0)
    while len(res) < length:
        if random.random() < bracket_prob:
            res += '('
            balance += 1
        if random.random() < bracket_prob:
            res += ' ' * random.randrange(0, spaces_max_cnt)
        if random.random() > 0.5:
            res += str(generate_random_number(number_max_len))
        else:
            res += generate_alphanum_random_string(variable_name_max_len)
        if random.random() < bracket_prob:
            res += ' ' * random.randrange(0, spaces_max_cnt)
        if random.random() < bracket_prob and balance > 0:
            res += ')'
            balance -= 1
        res += ' '
        if random.random() < bracket_prob:
            res += ' ' * random.randrange(0, spaces_max_cnt)
        if len(res) + 2 < length:
            res += generate_random_arithmetic_operator() + ' '
        if random.random() < bracket_prob:
            res += ' ' * random.randrange(0, spaces_max_cnt)
    for i in range(balance):
        res += ')'

    return res


def generate_random_correct_input(file_size: int) -> str:
    res: str = str()
    while len(res) < file_size:
        res += generate_random_arithmetic_expr(expr_max_len) + ';\n'
    return res


def get_recursive_parser_time(s: str, t: int):
    start_time = datetime.datetime.now()
    if t == 1:
        solve(s, True)
    else:
        solve_yacc(s)
    finish_time = datetime.datetime.now()
    return (finish_time - start_time).microseconds


def get_time_data(t: int) -> list:
    data: list = list()
    file_size_ = file_size_range[0]
    tmp = int(8)
    while file_size_ <= file_size_range[1]:
        for j in range(tmp):
            sz = random.randrange(int(file_size_ / 2), file_size_)
            print(int(file_size_ / 2), sz, file_size_, end=' ')
            s: str = 'def main (int argc) {\n'
            s += generate_random_correct_input(sz)
            s += '}\n'
            with open('input1.txt', 'w') as file_in:
                file_in.write(s)
            sum_time = 0
            for k in range(5):
                sum_time += get_recursive_parser_time('input1.txt', t)
            sum_time /= 5
            data.append((sz, sum_time))
            print(j, tmp, sum_time)
        file_size_ *= 2
        tmp = int(1.5 * tmp)

    return data
