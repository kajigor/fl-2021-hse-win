// Автомат, принимающий только строку с одним нулём над алфавитом из 0 и 1.
States = {
    q0, 
    q1,
    stok,
};

Start = q0;

End = {
    q1,
};

Alphabet = {
    0,
    1,
};

Function = {
    q0 (0)-> q1,
    q0 (1)-> q0,
    q1 (0)-> stok,
    q1 (1)-> q1,
    stok (0)-> stok,
    stok (1)-> stok,
};
