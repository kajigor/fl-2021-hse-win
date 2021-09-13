
## Задание 3
Начиная с версии 1.5.0 в языке программирования [Kotlin](https://kotlinlang.org/) появилась синтаксическая возможность делать следующие вещи: можно в переменную или return выражение присваивать if-expression или when-expression, возвращающие объект нужного типа во всех случаях.
Это было сделано, чтобы код стал более читаемый и интуитивно понятный, а так же это несколько сокращает написание кода и загруженность блоков ключевыми словами типа return.
(на самом деле котилн мой любимый язык, просто про плюсы я ничего писать не хотел...)

## Пример 1
```kotlin
fun foo(param: Int) {
    val result = if (param == 1) {
        "one"
    } else if (param == 2) {
        "two"
    } else {
        "three"
    }
}
```
Это примерно равносильно 
```kotlin
fun foo(param: Int) {
    var result: String
	if (param == 1) {
        result = "one"
    } else if (param == 2) {
        result = "two"
    } else {
        result = "three"
    }
}
```
[Ссылка](https://kotlinlang.org/docs/idioms.html#if-expression) на документацию
## Пример 2
```kotlin
fun transform(color: String): Int {
    return when (color) {
        "Red" -> 0
        "Green" -> 1
        "Blue" -> 2
        else -> throw IllegalArgumentException("Invalid color param value")
    }
}
```
Это равносильно
```kotlin
fun transform(color: String): Int {
    when (color) {
        "Red" -> return 0
        "Green" -> return 1
        "Blue" -> return 2
        else -> throw IllegalArgumentException("Invalid color param value")
    }
}
```

[Ссылка](https://kotlinlang.org/docs/idioms.html#return-on-when-statement) на документацию






















