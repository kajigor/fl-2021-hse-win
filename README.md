# Домашняя работа 1
## Задание 1
![](https://raw.githubusercontent.com/Fawentus/For-some-files/FLHW1/pictures/first.jpg)
## Задание 2
![](https://raw.githubusercontent.com/Fawentus/For-some-files/FLHW1/pictures/second.jpg)
## Задание 3
Язык: c++
1. [Regular expressions library](https://en.cppreference.com/w/cpp/regex)  
Можно работать с регулярными выражениями: создавать регулярные выражения, искать совпадения с ними, находить нужные подпоследовательности, заменять их на другие символы и многое другое
```c++
const std::string fnames[] = {"foo.txt", "bar.txt", "baz.dat", "zoidberg"};
const std::regex txt_regex("[a-z]+\\.txt"); // само регулярное выражение
 
for (const auto &fname : fnames) {
    std::cout << fname << ": " << std::regex_match(fname, txt_regex) << '\n'; // выводит, соответствует ли строка регулярному выражению
}
```
2. [std::span](https://en.cppreference.com/w/cpp/container/span)  
std::span появился в C++20. Объекты этого класса ссылаются на некоторую непрерывную последовательность необязательно фиксированного размера. 
Это более удобная и безопасная альтернатива использования указателей для доступа к элементам последовательности.
```c++
template<class T, size_t Extent = dynamic_extent> // так размер последовательности будет указан во время выполнения
class span;
```
3. [std::all_of, std::any_of, std::none_of](https://en.cppreference.com/w/cpp/algorithm/all_any_none_of)  
Эти функции позволяют проверять условие на некотором диапазоне
```c++
std::vector<int> v(10, 2);
if (std::all_of(v.cbegin(), v.cend(), [](int i){ return i % 2 == 0; })) {
    std::cout << "All numbers are even\n";
}
```
