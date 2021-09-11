def sum_numbers(filename):
    ans = []
    suma = 0
    try:
        with open(filename) as fl:
            for line in fl:
                ans.append(int(line))
        for x in ans:
            suma += x
        return suma
    except:
        return 0


print(sum_numbers("a.txt"))

def log(filename, message):
    f = open(filename, 'a')
    f.write('\n')
    f.write(message)
    f.write('\n')



print(log("a.txt", "new"))


def sum_numbers(filename):
    sum = 0
    try:
        with open(filename) as fl:
            while i in fl:
                for j in i:
                    try:
                        sum += float(j)
                    except:
                        break
# Ой, коммент

'''
 крутой коммент
'''
        return sum
    except:
        return sum


print(sum_numbers("a.txt"))

def solved_tasks(filename):
    # st = set()
    # with open(filename) as file:
    #     for line in file:
    #         stud_id, task = line.split(',')
    #         stud_id = int(stud_id)
    #         if stud_id not in st:
    #             st[stud_id] = 0
    #         st[stud_id] += 1
    # return st
    ans = {}
    help = []
    KEYS = set()
    with open(filename) as file:
        for line in file:
            stud_id, task = line.split(',')
            stud_id = int(stud_id)
            task = int(task)
            KEYS.add(stud_id)
            help.append(tuple((stud_id, task)))

        for pair in help:

            if pair[0] not in ans:
                ans[pair[0]] = set()

            if pair[1] not in ans:
                ans[pair[1]] = set()

            if pair[1] not in ans[pair[0]]:
                ans[pair[0]].add(pair[1])

            if pair[0] not in ans[pair[1]]:
                ans[pair[1]].add(pair[0])

        st = {}
        for key in ans:
            for i in ans[key]:
                if key not in st:
                    st[key] = 0
                st[key] += 1
        hooray = st.copy()
        for key in st:
            if key not in KEYS:
                hooray.pop(key)
    return hooray
def solved_tasks(filename):
    st = {}
    helpp = [[0] * 10 for _ in range(10)]
    with open(filename) as file:
        for line in file:

            stud_id, task = line.split(',')
            stud_id = int(stud_id)
            task = int(task)

            if stud_id not in st:
                st[stud_id] = 0

            if helpp[stud_id][task] == 1:
                st[stud_id] -= 1

            helpp[stud_id][task] = 1

            st[stud_id] += 1



    print(helpp)
    return st


from collections import Counter


def solved_tasks(filename):
    with open(filename) as f:
        for line in f:
            key, value = line.strip().split(',')
    return {key: Counter(str(value))}


st = {}
with open(filename) as file:
    for line in file:
        stud_id, task = line.split(',')
        stud_id = int(stud_id)
        if stud_id not in st:
            st[stud_id] = 0
        st[stud_id] += 1
return st

print(solved_tasks("a.txt"))

def fix_duplicates(ids):
    x = []
    for i in range(len(ids)):
        c = ids[:i + 1]  # пирамидка
        if c.count(ids[i]) == 1:  # как раз вот только что добавили
            x.append(ids[i])
        else:
            x.append(ids[i] + '_' + str(c.count(ids[i]) - 1))
    return x


ids = ["a", "b", "c", "a", "a", "d", "c"]

assert fix_duplicates(ids) == ['a', 'b', 'c', 'a_1', 'a_2', 'd', 'c_1']

def f(x):
    y = 0
    y = float(y)
    if x <= -2:
        y = 1 - (x + 2) ** 2
    elif x > 2:
        y = (x - 2) ** 2 + 1
    elif -2 < x <= 2:
        y = -(x / 2)
    return y


print(f(1))

def modify_list(l):
    for x in range(len(l)):
        if l[x] % 2 != 0:
            l[x] = -1
        else:
            l[x] = l[x] // 2
    cnt = l.count(-1)
    for i in range(cnt):
        l.remove(-1)
    return l


lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)  # None
print(lst)  # [1, 2, 3]

не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if key not in d:
        new_key = 2 * key
        if new_key not in d:
            d.update({new_key: [value]})
        else:
            d[new_key].append(value)
    else:
        d[key].append(value)
    return d


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)  # {2: [-1, -2, -3]}

line = input().split()
lowline = []
for y in line:
    h = y.lower()
    # print(y)
    lowline.append(h)

help = set(lowline)
for x in help:
    print(x, ' ', lowline.count(x))

print(line)
print(help)

r = 'Cc'
print(r.lower())

def f(t):
    return t * t


n = int(input())
dic = {}
answers = []
for i in range(n):
    x = int(input())
    if x not in dic:
        dic.update({x: f(x)})
        # print(f(x))
        answers.append(f(x))
    else:
        # print(dic.get(x))
        answers.append(dic.get(x))

for y in answers:
    print(y)

line = input().split()
co = line.copy()
for i in range(len(co)):
    if i+1 > len(co):
        line[i] = co[i-1] + co[0]
    if i-1 < 0:
        line[i] = co[-1] + co[i+1]
    else:
        line[i] = co[i-1] + co[i+1]

print(line)

x = input().split()
helper = set(x)
for i in sorted(helper):
    if x.count(i) == 1:
        continue
    else:
        print(i, end=' ')

if len(x) == 1:
    print(x[0])
else:
    y = [int(x[i - 1]) + int(x[i + 1]) for i in range(-1, len(x) - 1)]
    for i in range(1, len(y)):
        print(y[i], end=' ')
    print(y[0])

line = str(input())
cnt = 1
x = 1
j = line[x:x + 1] # каретка
for i in line:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = line[x:x + 1]

# for i in range(3):
#     for i in range(4):
#         print(i)

# print({x: x ** 2 for x in range(10)})

for x in [0, 2]:
    print(x)
# head, *tail = [1, 2, 3, 4, 5]
# print(head, tail)
