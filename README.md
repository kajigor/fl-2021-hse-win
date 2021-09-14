# HW02

1. Равны ли данные регулярные выражения над алфавитом `{a, b}`? Обосновать. Можно построить минимальные детерминированные конечные автоматы и сравнить их. Альтернативно можно доказать, что любая строка, задаваемая первым регулярным выражением, принадлежит языку второго регулярного выражения и наоборот (или привести контрпример).

   a. `b* a ((a | b) b* a)*`

   b. `((a | b)* b a | a) (a a)*`

2. Улучшить язык описания конечных автоматов из предыдущего домашнего задания таким образом, чтобы символами алфавита автомата могли быть произвольные последовательности символьного типа `char`. То есть если у вас в языке есть ключевые слова или специальные операторы (например, `,` в качестве разделителя или `-->` для обозначения перехода), должна быть возможность использовать их как метки переходов автомата.

3. Реализовать лексер при помощи генератора лексеров (например, семейства lex) для вашего языка описания конечных автоматов.

   * Можно писать на любом языке.
   * Можно использовать любой генератор лексеров.
   * Задание должно быть оформлено как консольное приложение, принимающее как аргумент командной строки путь ко входному файлу. Результат лексического анализа должен быть записан в файл с тем же именем, но добавочным расширением `.out` (если вход -- `input.txt`, то результат работы записать в `input.txt.out`).
   * Каждый токен должен содержать тип, значение и координаты во входном файле.
   * Если вход лексически некорректен, сообщить об ошибке цивилизованно: исключениями в пользователя бросать не стоит.
   * Обязательно привести тесты для вашего лексера.