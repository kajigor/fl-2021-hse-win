# Задача №1
![](01.jpg)
# Задача №2
![](02.jpg)
# Задача №3
Мой любимый язык программирование - Java, второй - Python, документация к которому есть [на сайте](https://docs.python.org/).
Иснересно было посмотреть, какие фичи будут в новой версии: `Python 3.9.7`. Это можно посмотреть [тут](https://docs.python.org/3/whatsnew/3.9.html).
## Dictionary Merge
Первое, что я заметил, это - добвление нового опратора для словарей: `Megre (|)`. Он позволяет сливать 2 словаря в один, есть пример на сайте:
```python
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
```
## String Methods to Remove Prefixes and Suffixes
Также в новой версии есть новый функии, связанные со строками: [`str.removeprefix`](https://docs.python.org/3/library/stdtypes.html#str.removeprefix) и [`str.removesuffix`](https://docs.python.org/3/library/stdtypes.html#str.removesuffix). Они позволяют удалять суффикс или префикс строки.
```python
>>> 'TestHook'.removeprefix('Test')
'Hook'
>>> 'BaseTestCase'.removeprefix('Test')
'BaseTestCase'
>>> 'MiscTests'.removesuffix('Tests')
'Misc'
>>> 'TmpDirMixin'.removesuffix('Tests')
'TmpDirMixin'
```
# Задача №4
# Задача №5
