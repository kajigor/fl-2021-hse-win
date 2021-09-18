# Особенности лексического синтаксиса C++ #

Мною был выбран `C++`, так как недавно на несколько таких
особенностей попал (:) ):

* Объявление переменной внутри цикла `while`: 
  
  https://en.cppreference.com/w/cpp/language/while


  Подобный механизм объявление есть у условного оператора `if`,
  однако там объявление происходит через `;` как отдельный вид
  оператора. Здесь же объявление происходит как внутри цикла `for`.
  Например, малосдодержательный, но показательный пример:
  ```cpp
  while(bool ok = 1) {
  // бесконечный цикл
  }
  ```
* Вызов дефолтного конструктора без круглых скобок
  
  https://en.cppreference.com/w/cpp/language/constructor

  (Сам попался недавно)
  При отсутствии конструктора по умолчанию, нельзя создавать объект класс как `class()`,
  а только `class` или `class{}`.
  Например:
  ```cpp
  struct SegTree {
    int n;
    void build();
  }

  SegTree s(); // нельзя
  SegTree s{}; // можно
  SegTree s; // можно
  s.build();
  ```
* Указание атрибутов
  
  https://en.cppreference.com/w/cpp/language/attributes

  Можно указывать разные атрибуты из одного `namespace` внутри одного объявления: `[using CC: a, b] `
  и возможность комментировать причину для атрибута `[[nodiscard]]`.
  Пример для объявления из одного `namespace` из ссылки:
  ```cpp
  [[using gnu : const, always_inline, hot]] [[nodiscard]]
  int f[[gnu::always_inline]](); // an attribute may appear in multiple   specifiers
  ```