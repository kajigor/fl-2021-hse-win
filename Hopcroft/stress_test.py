import random

cpp_file = open("cpp_hopcroft.txt", 'w')

N = 1
Q = int(1e5)

cnt_of_tr = N * Q

cpp_file.write(f"stress test\n{N} ")

for i in range(N):
    cpp_file.write(f"{i} ")

cpp_file.write(f"\n{Q} {int(Q/2)} {cnt_of_tr}\n0 ")

for i in range(int(Q/2)):
    cpp_file.write(f"{random.randint(0, Q - 1)} ")
cpp_file.write('\n')
for i in range(Q):
    for j in range(N):
        cpp_file.write(f"{i} {random.randint(0, Q - 1)} {j}\n")