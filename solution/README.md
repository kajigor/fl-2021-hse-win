# Задача №0
Подправил.
# Задача №1
# Задача №2-3
Код в файле `main.py`, тесты - ниже.  
Запуск: `python main.py input.txt`  
![](01.jpg)
![](02.jpg)  
Тесты:  
1) `DE011000010110001001100011ECBBA0B00110001BACCA0B00110001BAB011000010110001001100011BA1B00110010BACCA1B00110010BAB011000010110001001100011BA1B00110010BACD`  
2) `DE0011000000110001ECBBA0B00110001BACCA0B00110001BAB00110001BA0B00110010BACCA0B00110001BAB00110000BA1B00110011BACCA0B00110010BAB00110000BA1B00110011BACCA1B00110011BAB00110001BA0B00110010BACCA1B00110011BAB00110000BA1B00110011BACD`  
3) `DE0011000000110001ECBBA0B00110001BACCA0B00110001BAB00110001BA0B00110001BACCA0B00110001BAB00110000BA0B00110010BACCA0B00110010BAB00110000BA0B00110011BACCA0B00110011BAB00110000BA1B00110100BACCA1B00110100BAB00110001BA0B00110001BACCA0B00110011BAB00110001BA0B00110001BACCA0B00110010BAB00110001BA0B00110001BACD`  
4) `DE0011000000110001ECBBA0BBACCA0BBAB00110000BA0B00110000BACCA0B00110000BAB00110000BA0B00110000BACCA0B00110000BAB00110001BA1B00110001BACCA0BBAB00110001BA1B00110001BACCA1B00110001BAB00110000BA0B00110000BACCA1B00110001BAB00110001BA1B00110001BACD`  


Вывод:  
1)
```
I solemnly swear I am up to no good!
Alphabet:
a b c 
Vertexes list:
1. Name: "1" and it is not a terminal
2. Name: "2" and it is a terminal
Edges list:
From None to 1 name: ""
From 1 to 2 name: "abc"
From 2 to 2 name: "abc"
Edges list:
1. Initial state found: 1
2. Vertex names are unique
3. Elements of the alphabet are unique
4. Machine is not deterministic
5. Machine is full
Mischief Managed!
```
2)
```
I solemnly swear I am up to no good!
Alphabet:
0 1 
Vertexes list:
1. Name: "1" and it is not a terminal
2. Name: "2" and it is not a terminal
3. Name: "3" and it is a terminal
Edges list:
From None to 1 name: ""
From 1 to 2 name: "1"
From 1 to 3 name: "0"
From 2 to 3 name: "0"
From 3 to 2 name: "1"
From 3 to 3 name: "0"
Edges list:
1. Initial state found: 1
2. Vertex names are unique
3. Elements of the alphabet are unique
4. Machine is deterministic
5. Machine is not full
Mischief Managed!
```
3)
```
I solemnly swear I am up to no good!
Alphabet:
0 1 
Vertexes list:
1. Name: "1" and it is not a terminal
2. Name: "2" and it is not a terminal
3. Name: "3" and it is not a terminal
4. Name: "4" and it is a terminal
Edges list:
From None to 1 name: ""
From 1 to 1 name: "1"
From 1 to 2 name: "0"
From 2 to 3 name: "0"
From 3 to 4 name: "0"
From 4 to 1 name: "1"
From 3 to 1 name: "1"
From 2 to 1 name: "1"
Edges list:
1. Initial state found: 1
2. Vertex names are unique
3. Elements of the alphabet are unique
4. Machine is not deterministic
5. Machine is not full
Mischief Managed!
```
4)
```
I solemnly swear I am up to no good!
Alphabet:
0 1 
Vertexes list:
1. Name: "" and it is not a terminal
2. Name: "0" and it is not a terminal
3. Name: "1" and it is a terminal
Edges list:
From None to 1 name: ""
From 1 to 2 name: "0"
From 2 to 2 name: "0"
From 2 to 3 name: "1"
From 1 to 3 name: "1"
From 3 to 2 name: "0"
From 3 to 3 name: "1"
Edges list:
1. Initial state found: 1
2. Vertex names are unique
3. Elements of the alphabet are unique
4. Machine is deterministic
5. Machine is full
Mischief Managed!
```

Сайт для перевода чаров [тут](https://www.rapidtables.com/convert/number/ascii-to-binary.html).
