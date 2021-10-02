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
Пусть `S` - алфавит для описания языка, на котором задается названия ребер и вершин в автомате (пояснения к автомату, может быть его номер). Назовем его `L`. Возьмем 5 символов: `A`, `B`, `C`, `D`, `E`. Дальше нужно научиться записывать слова: "алфавит", "вершинa", "ребро" и "автомат". Параметра у вершины: является ли она терминальной и ее описание. Будем делать так: для начала оборачивать слово в буквы `A` (то есть для каджого слова будет верно, что он начинается и заканчивается на букву `A`), внутри первым символом будет `0` или `1` - в зависимости от терминальности, и дальше бинарный код описания на языке `L` (переведенное в бинарную строку длины `8`, так как `char` - это один байт), обернутое в `B`. Для слова ребро будем оборачивать его в `C`, внутри записать исходящую вершину, затем описание ребра, обернутое в `B`, а потом входящую. Слово алфавит: имя, обернутое в буквы `E`. И теперь осталось описать слово автомат: обернем в символы `D`, а внутри - алфавит, а затем - отсортированный список ребер. Таким образом, у нас каждый автомат описывается единственным образом, а слово не может относится к более чем одному автомату.
![](01.jpg)
Коды будут:
1) `DE011000010110001001100011ECBBA0B00110001BACCA0B00110001BAB011000010110001001100011BA1B00110010BACCA1B00110010BAB011000010110001001100011BA1B00110010BACD`
2) `DE0011000000110001ECBBA0B00110001BACCA0B00110001BAB00110001BA0B00110010BACCA0B00110001BAB00110000BA1B00110011BACCA0B00110010BAB00110000BA1B00110011BACCA1B00110011BAB00110001BA0B00110010BACCA1B00110011BAB00110000BA1B00110011BACD`
3) `DE0011000000110001ECBBA0B00110001BACCA0B00110001BAB00110001BA0B00110001BACCA0B00110001BAB00110000BA0B00110010BACCA0B00110010BAB00110000BA0B00110011BACCA0B00110011BAB00110000BA1B00110100BACCA1B00110100BAB00110001BA0B00110001BACCA0B00110011BAB00110001BA0B00110001BACCA0B00110010BAB00110001BA0B00110001BACD`


Сайт для перевода чаров [тут](https://www.rapidtables.com/convert/number/ascii-to-binary.html).
## Задача №3
Код в файле `main.py`, тесты - коды из предыдущего задания.

Запуск: `python main.py input.txt`

Выводы для тестов:

1)
```
LexToken(machine,'Open',1,0)
LexToken(alphabet,'abc',1,1)
LexToken(edge,'Open',1,27)
LexToken(edge_name,'',1,28)
LexToken(vertex,'type: to, name: 1, terminality: False',1,30)
LexToken(edge,'Close',1,43)
LexToken(edge,'Open',1,44)
LexToken(vertex,'type: from, name: 1, terminality: False',1,45)
LexToken(edge_name,'abc',1,58)
LexToken(vertex,'type: to, name: 2, terminality: True',1,84)
LexToken(edge,'Close',1,97)
LexToken(edge,'Open',1,98)
LexToken(vertex,'type: from, name: 2, terminality: True',1,99)
LexToken(edge_name,'abc',1,112)
LexToken(vertex,'type: to, name: 2, terminality: True',1,138)
LexToken(edge,'Close',1,151)
LexToken(machine,'Close',1,152)
```
2)
```
LexToken(machine,'Open',1,0)
LexToken(alphabet,'01',1,1)
LexToken(edge,'Open',1,19)
LexToken(edge_name,'',1,20)
LexToken(vertex,'type: to, name: 1, terminality: False',1,22)
LexToken(edge,'Close',1,35)
LexToken(edge,'Open',1,36)
LexToken(vertex,'type: from, name: 1, terminality: False',1,37)
LexToken(edge_name,'1',1,50)
LexToken(vertex,'type: to, name: 2, terminality: False',1,60)
LexToken(edge,'Close',1,73)
LexToken(edge,'Open',1,74)
LexToken(vertex,'type: from, name: 1, terminality: False',1,75)
LexToken(edge_name,'0',1,88)
LexToken(vertex,'type: to, name: 3, terminality: True',1,98)
LexToken(edge,'Close',1,111)
LexToken(edge,'Open',1,112)
LexToken(vertex,'type: from, name: 2, terminality: False',1,113)
LexToken(edge_name,'0',1,126)
LexToken(vertex,'type: to, name: 3, terminality: True',1,136)
LexToken(edge,'Close',1,149)
LexToken(edge,'Open',1,150)
LexToken(vertex,'type: from, name: 3, terminality: True',1,151)
LexToken(edge_name,'1',1,164)
LexToken(vertex,'type: to, name: 2, terminality: False',1,174)
LexToken(edge,'Close',1,187)
LexToken(edge,'Open',1,188)
LexToken(vertex,'type: from, name: 3, terminality: True',1,189)
LexToken(edge_name,'0',1,202)
LexToken(vertex,'type: to, name: 3, terminality: True',1,212)
LexToken(edge,'Close',1,225)
LexToken(machine,'Close',1,226)
```
3)
```
LexToken(machine,'Open',1,0)
LexToken(alphabet,'01',1,1)
LexToken(edge,'Open',1,19)
LexToken(edge_name,'',1,20)
LexToken(vertex,'type: to, name: 1, terminality: False',1,22)
LexToken(edge,'Close',1,35)
LexToken(edge,'Open',1,36)
LexToken(vertex,'type: from, name: 1, terminality: False',1,37)
LexToken(edge_name,'1',1,50)
LexToken(vertex,'type: to, name: 1, terminality: False',1,60)
LexToken(edge,'Close',1,73)
LexToken(edge,'Open',1,74)
LexToken(vertex,'type: from, name: 1, terminality: False',1,75)
LexToken(edge_name,'0',1,88)
LexToken(vertex,'type: to, name: 2, terminality: False',1,98)
LexToken(edge,'Close',1,111)
LexToken(edge,'Open',1,112)
LexToken(vertex,'type: from, name: 2, terminality: False',1,113)
LexToken(edge_name,'0',1,126)
LexToken(vertex,'type: to, name: 3, terminality: False',1,136)
LexToken(edge,'Close',1,149)
LexToken(edge,'Open',1,150)
LexToken(vertex,'type: from, name: 3, terminality: False',1,151)
LexToken(edge_name,'0',1,164)
LexToken(vertex,'type: to, name: 4, terminality: True',1,174)
LexToken(edge,'Close',1,187)
LexToken(edge,'Open',1,188)
LexToken(vertex,'type: from, name: 4, terminality: True',1,189)
LexToken(edge_name,'1',1,202)
LexToken(vertex,'type: to, name: 1, terminality: False',1,212)
LexToken(edge,'Close',1,225)
LexToken(edge,'Open',1,226)
LexToken(vertex,'type: from, name: 3, terminality: False',1,227)
LexToken(edge_name,'1',1,240)
LexToken(vertex,'type: to, name: 1, terminality: False',1,250)
LexToken(edge,'Close',1,263)
LexToken(edge,'Open',1,264)
LexToken(vertex,'type: from, name: 2, terminality: False',1,265)
LexToken(edge_name,'1',1,278)
LexToken(vertex,'type: to, name: 1, terminality: False',1,288)
LexToken(edge,'Close',1,301)
LexToken(machine,'Close',1,302)

```

Вывод работает следующим образом:  
1) у нас есть начало и конец автомата:  
```
LexToken(machine,'Open',x_1,y_1)
...
LexToken(machine,'Close',x_2,y_2)
```
а внутри - его описание  
2) у нас есть начало и конец ребра:
```
LexToken(edge,'Open',x_1,y_1)
...
LexToken(edge,'Close',x_2,y_2)
```
а внутри описания, состоящие из стартовой вершины: `LexToken(vertex,'type: from, name: abc, terminality: False',x,y)
` (если она есть); из имени: `LexToken(EdgeName,'abc',x,y)`; и финишней вершины: `LexToken(vertex,'type: to, name: abc, terminality: False',x,y)`.
