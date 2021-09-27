## Задача №1
Разобъем множество всех строк над алфавитом `{a, b}` на несколько групп, которые полностью покрывают все возможные слова:
1) `.*ba...a` - на конце нечетное количество `a`
2) `.*ba...a` - на конце четное количество `a`
3) `a...a` - нечетное количество `a`
4) `a...a` - четное количество `a`  
Заметим, что это действительно покрытие: если в строке есть `b`, то сработают первые три пункта, иначе - три последних.

Дальше несложно заметить, что группы `1`, `3` покрываются регулярными выражениями из условия, а `2`, `4` - нет.  
Докажем это:  
для начала полезно заметить, что пустые строки не подходят никуда, ведь в обоих данных в условии регулярных выражениях есть ьуквы не под `*`.  
PS: скобку в последующем решении в выражении `b*a((a|b)b*a)*` я называю скобку `((a|b)b*a)`.  
1) `b*a((a|b)b*a)*` покрывает `1` и не покрывает `2`:  
Нужно просто заметить, что если в выражеини встречается буква `b`, то тогда после последнего буддет обязательно нечетное количество букв `a`. Это можно понять следующим образом: пусть мы не взяли последнюю скобку ни разу, тогда у нас у `b*` в самом начале должна быть хотя бы `1` буква `b` по предположению, а также ровна одна буква `a` - та, что не в скобке. Если взяли скобку, то тогда если мы никогда в этой скобке не берем букву `b`, то тогда там будет точно четное количество букв `a`, что в сумме с одной `a` вне скобки даст нечетное число. А если мы берем букву `b` в скобках, то тогда после нее будет одна буква `a`, что четное число.  
То есть после добавления скобки или без скобки у нас всегда после последней `b` нечетное число, следователно при любом количестве взятий последней скобки будет нечетное число букв `a`.  
2) `b*a((a|b)b*a)*` покрывает `3` и не покрывает `4`:  
Нужно доказать, что если у нас нет букв `b`, то тогда у нас количество `a` - нечетное. Это легко понять, ведь у нас вне скобки будет одна буква `a`, а внутри скобки - всегда две. Следовательно при любом количестве взятия скобок у нас будет нечетное число букв `a`.  
PS: первую скобку в последующем решении в выражении `((a|b)*ba|a)(aa)*` я называю скобку `((a|b)*ba|a)`, а втоую - `(aa)*`.  
3) `((a|b)*ba|a)(aa)*` покрывает `1` и не покрывает `2`:  
Если в строке есть буква `b`, то точно есть левая часть первой скобки, следовательно на конце точно есть хотя бы одна `a`, еще дополнительные `a` могут добавится только от второй скобки, то добится может только четное число, следоавтельно количество `a` останется нечетным.  
4) `((a|b)*ba|a)(aa)*` покрывает `3` и не покрывает `4`:  
Если у нас нет буквы `b`, тогда у первой скобки точно сработает правая часть, следовательно есть одна буква `a`, аналогичная ситуация относительно прошлого пункта: вторая скобка после этого не поменяет четность.  
Доказали для каждой строки, что ее либо обе регулярки из улсовия покрывают, либо обе не покрывают, следовательно они равны.
## Задача №2
Решение будет отличаться от решения в предыдущим дз, только разница в том, что мы будем кодировать `ASCII` описания ребер и вершин в бинарную строку.
Пусть `S` - алфавит для описания языка, на котором задается названия ребер и вершин в автомате (пояснения к автомату, может быть его номер). Назовем его `L`. Возьмем 4 символа: `A`, `B`, `C`, `D`. Дальше нужно научиться записывать слова: "вершинa", "ребро" и "автомат". Параметра у вершины: является ли она терминальной и ее описание. Будем делать так: для начала оборачивать слово в буквы `A` (то есть для каджого слова будет верно, что он начинается и заканчивается на букву `A`), внутри первым символом будет `0` или `1` - в зависимости от терминальности, и дальше бинарный код описания на языке `L` (переведенное в бинарную строку длины `8`, так как `char` - это один байт), обернутое в `B`. Для слова ребро будем оборачивать его в `C`, внутри записать исходящую вершину, затем описание ребра, обернутое в `B`, а потом входящую. И теперь осталось описать слово автомат: обернем в символы `D`, а внутри - отсортированный список ребер. Таким образом, у нас каждый автомат описывается единственным образом, а слово не может относится к более чем одному автомату.
![](01.jpg)
Коды будут:
1) `DCBBA0B00110001BACCA0B00110001BAB011000010110001001100011BA1B00110010BACCA1B00110010BAB011000010110001001100011BA1B00110010BACD`
2) `DCBBA0B00110001BACCA0B00110001BAB00110001BA0B00110010BACCA0B00110001BAB00110000BA1B00110011BACCA0B00110010BAB00110000BA1B00110011BACCA1B00110011BAB00110001BA0B00110010BACCA1B00110011BAB00110000BA1B00110011BACD`
3) `DCBBA0B00110001BACCA0B00110001BAB00110001BA0B00110001BACCA0B00110001BAB00110000BA0B00110010BACCA0B00110010BAB00110000BA0B00110011BACCA0B00110011BAB00110000BA1B00110100BACCA1B00110100BAB00110001BA0B00110001BACCA0B00110011BAB00110001BA0B00110001BACCA0B00110010BAB00110001BA0B00110001BACD`


Сайт для перевода чаров [тут](https://www.rapidtables.com/convert/number/ascii-to-binary.html).
## Задача №3
Код в файле `main.py`, тесты - коды из предыдущего задания.

Запуск: `python main.py input.txt`

Выводы для тестов:

1)
```
LexToken(Machine,'Open',1,0)
LexToken(Edge,'Open',1,1)
LexToken(EdgeName,'',1,2)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,4)
LexToken(Edge,'Close',1,17)
LexToken(Edge,'Open',1,18)
LexToken(Vertex,'type: from, name: 1, terminality: False',1,19)
LexToken(EdgeName,'abc',1,32)
LexToken(Vertex,'type: to, name: 2, terminality: True',1,58)
LexToken(Edge,'Close',1,71)
LexToken(Edge,'Open',1,72)
LexToken(Vertex,'type: from, name: 2, terminality: True',1,73)
LexToken(EdgeName,'abc',1,86)
LexToken(Vertex,'type: to, name: 2, terminality: True',1,112)
LexToken(Edge,'Close',1,125)
LexToken(Machine,'Close',1,126)
```
2)
```
LexToken(Machine,'Open',1,0)
LexToken(Edge,'Open',1,1)
LexToken(EdgeName,'',1,2)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,4)
LexToken(Edge,'Close',1,17)
LexToken(Edge,'Open',1,18)
LexToken(Vertex,'type: from, name: 1, terminality: False',1,19)
LexToken(EdgeName,'1',1,32)
LexToken(Vertex,'type: to, name: 2, terminality: False',1,42)
LexToken(Edge,'Close',1,55)
LexToken(Edge,'Open',1,56)
LexToken(Vertex,'type: from, name: 1, terminality: False',1,57)
LexToken(EdgeName,'0',1,70)
LexToken(Vertex,'type: to, name: 3, terminality: True',1,80)
LexToken(Edge,'Close',1,93)
LexToken(Edge,'Open',1,94)
LexToken(Vertex,'type: from, name: 2, terminality: False',1,95)
LexToken(EdgeName,'0',1,108)
LexToken(Vertex,'type: to, name: 3, terminality: True',1,118)
LexToken(Edge,'Close',1,131)
LexToken(Edge,'Open',1,132)
LexToken(Vertex,'type: from, name: 3, terminality: True',1,133)
LexToken(EdgeName,'1',1,146)
LexToken(Vertex,'type: to, name: 2, terminality: False',1,156)
LexToken(Edge,'Close',1,169)
LexToken(Edge,'Open',1,170)
LexToken(Vertex,'type: from, name: 3, terminality: True',1,171)
LexToken(EdgeName,'0',1,184)
LexToken(Vertex,'type: to, name: 3, terminality: True',1,194)
LexToken(Edge,'Close',1,207)
LexToken(Machine,'Close',1,208)
```
3)
```
LexToken(Machine,'Open',1,0)
LexToken(Edge,'Open',1,1)
LexToken(EdgeName,'',1,2)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,4)
LexToken(Edge,'Close',1,17)
LexToken(Edge,'Open',1,18)
LexToken(Vertex,'type: from, name: 1, terminality: False',1,19)
LexToken(EdgeName,'1',1,32)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,42)
LexToken(Edge,'Close',1,55)
LexToken(Edge,'Open',1,56)
LexToken(Vertex,'type: from, name: 1, terminality: False',1,57)
LexToken(EdgeName,'0',1,70)
LexToken(Vertex,'type: to, name: 2, terminality: False',1,80)
LexToken(Edge,'Close',1,93)
LexToken(Edge,'Open',1,94)
LexToken(Vertex,'type: from, name: 2, terminality: False',1,95)
LexToken(EdgeName,'0',1,108)
LexToken(Vertex,'type: to, name: 3, terminality: False',1,118)
LexToken(Edge,'Close',1,131)
LexToken(Edge,'Open',1,132)
LexToken(Vertex,'type: from, name: 3, terminality: False',1,133)
LexToken(EdgeName,'0',1,146)
LexToken(Vertex,'type: to, name: 4, terminality: True',1,156)
LexToken(Edge,'Close',1,169)
LexToken(Edge,'Open',1,170)
LexToken(Vertex,'type: from, name: 4, terminality: True',1,171)
LexToken(EdgeName,'1',1,184)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,194)
LexToken(Edge,'Close',1,207)
LexToken(Edge,'Open',1,208)
LexToken(Vertex,'type: from, name: 3, terminality: False',1,209)
LexToken(EdgeName,'1',1,222)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,232)
LexToken(Edge,'Close',1,245)
LexToken(Edge,'Open',1,246)
LexToken(Vertex,'type: from, name: 2, terminality: False',1,247)
LexToken(EdgeName,'1',1,260)
LexToken(Vertex,'type: to, name: 1, terminality: False',1,270)
LexToken(Edge,'Close',1,283)
LexToken(Machine,'Close',1,284)

```

Вывод работает следующим образом:  
1) у нас есть начало и конец автомата:  
```
LexToken(Machine,'Open',x_1,y_1)
...
LexToken(Machine,'Close',x_2,y_2)
```
а внутри - его описание  
2) у нас есть начало и конец ребра:
```
LexToken(Edge,'Open',x_1,y_1)
...
LexToken(Edge,'Close',x_2,y_2)
```
а внутри описания, состоящие из стартовой вершины: `LexToken(Vertex,'type: from, name: abc, terminality: False',x,y)
` (если она есть); из имени: `LexToken(EdgeName,'abc',x,y)`; и финишней вершины: `LexToken(Vertex,'type: to, name: abc, terminality: False',x,y)`.
