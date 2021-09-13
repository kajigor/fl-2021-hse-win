# JavaScript -- 2 место
## Конструктор
> Я был удивлен, что в `JS` есть возможность вызывать конструктор объекта без скобок, если тому не нужны никакие параметры.
```javascript
let d = new Date; // эквивалентно:
let d = new Date(); 
```
> Узнал, что здесь есть прикольная штука `with`. Вот в чём её суть:
```javascript
const Student = {
  course: 1,
  average_score: 10,
  name: "Имя Фамилия"
};
// есть какой-то объект student. Допустим, на надо вывести информацию о нём без лишнего кода:
with(Student) {
    console.log(`Это ${name}, его средний балл - ${average_score}, он учится на ${course} курсе`)
}
```
> У функции есть своего рода поля
```javascript
function foo() {
    if(foo.flag === true){
        console.log("TRUE")
    } else {
        console.log("FALSE")
    }
}
foo() // выведет FALSE
foo.flag = true
foo() // а теперь выведет TRUE
```