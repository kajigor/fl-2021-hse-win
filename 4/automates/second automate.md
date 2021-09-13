// Автомат, принимающий только строку размера 2 над алфавитом из букв a, b, c.
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
    a,
    b,
    c,
};

Function = {
    q0 (a)-> q1,
    q0 (b)-> q1,
    q1 (a)-> q2,
    q1 (b)-> q2,
    q2 (a)-> stok,
    q2 (b)-> stok,
    stok (a)-> stok,
    stok (b)-> stok,
};