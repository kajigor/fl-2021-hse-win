Автомат, принимающий ответ на главный вопрос жизни, вселенной и всего такого.
```python
States = {
    q0,
    q1,
    q2,
    stok,
};

Start = q0;

End = {
    q2,
};

Alphabet = {
    4,
    2,
};

Function = {
    q0 (4)-> q1,
    q0 (2)-> stok,
    q1 (4)-> stok,
    q1 (2)-> q2,
    q2 (4)-> stok,
    q2 (2)-> stok,
    stok (4)-> stok,
    stok (2)-> stok,
};
```