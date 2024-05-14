## 코틀린 4부

### 44장 람다
코틀린에서 람다함수의 값은 it으로 대체 가능하다
``` kotlin
fun base() {
    val list = listOf(1, 2, 3)
    val result = list.map ({n: Int -> "[$n]"})
    Int와 n은 생략가능하다
    val result2 = list.map { "[$it]" }
}

fun index() {
    val list = listOf(1, 2, 3)
    list.mapIndexed(index, element -> "[$index -> $element]"
}
```

### 45장 람다의 중요성

람다를 활용하면 코드가 짧아지고 읽기 쉬워진다
또한 자바의 스트림과 다르게 재활용 된다.
``` kotlin

fun main() {
    val list = listOf(1, 2, 3, 4)
    val isEven = { e: Int -> e % 2 == 0 }
    val even = list.filter { it % 2 == 0 }
    val biggerThanTwo = list.filter { it > 2 }
    val even2 = list.filter(isEven)
    val even3 = list.filter(isEven)
}

public void java() {
    val list = List.of(1, 2, 3, 4);
    val even = list.stream().filter(it -> it % 2 == 0).toList();
    val biggerThanTwo = list.stream().filter(it ->  it > 2 ).toList();
}

fun main2() {
    val list = listOf(1, 5, 7, 10)
    var sum = 0
    val divider = 5
    list.filter { it % divider == 0 }
        .forEach { sum += it }
}

public class Main {
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 5, 7, 10);
        final int[] sum = {0}; // 자바에서 지역 변수를 람다식 내부에서 변경하기 위해서는 배열이나 래퍼 클래스를 사용해야 합니다.
        int divider = 5;

        list.stream() // 스트림 생성
            .filter(i -> i % divider == 0) // 조건에 맞는 요소 필터링
            .forEach(i -> sum[0] += i); // 각 요소에 대해 주어진 작업 실행

        System.out.println(sum[0]); // 결과 출력
    }
}
```


### 46장 컬렉션에 대한 연산
### 변환 연산
    map: 컬렉션의 각 요소에 변환 함수를 적용
    filter: 주어진 조건에 맞는 요소만을 포함하는 새 컬렉션을 반환
    filterNot:  주어진 조건에 맞는 요소만을 포함하지 않는 새 컬렉션을 반환

### 집계 연산
    reduce: 컬렉션의 요소를 순차적으로 누적하여 하나의 값으로 합산
    groupBy: 특정 조건에 따라 요소들을 그룹화하고, 결과를 맵으로 반환
    sumOf: 컬렉션의 요소에 대한 합계를 계산
    sorted, sortedBy: 값 정렬 혹은 기준에 따라 정렬

### 접근 연산
    first, last: 컬렉션의 첫 번째 또는 마지막 요소를 반환
    find: 주어진 조건에 맞는 첫 번째 요소를 반환
    filterNotNull: null이 아닌 요소만 포함하는 새 컬렉션을 반환
    take, takeLast: N개 만큼의 요소 반환
    drop, dropLast: N개만큼의 요소 제거
### 상태 확인 연산
    isEmpty, isNotEmpty: 컬렉션이 비어있음 or 비어있지 않음
    all: 모든 요소가 조건을 만족
    any: 하나라도 조건을 만족
    none: 모든 요소가 조건을 만족하지 않음

Pair
``` kotlin
fun main() {
    val (i, s) = Pair(A, "B")
}
```

### 47장 멤버 참조

``` kotlin
data class Person(val name: String, val age: Int)

fun main() {
    val people = listOf(Person("철수", 29), Person("밥", 31))
    
    val getAge = Person::age
    println(people.map(getAge)) 

    val personNames = people.map(Person::name)
    println(personNames)
    
    val 철수 = Person("철수", 29)
    val 철수나이 = 철수::age
    println(철수나이())
    
    // 생성자 참조
    val 생성기 = ::Person
    val person = 생성기("고양이", 2)
    println(person)
}
```

### 48장 고차함수

#### 프로그래밍 언어에서 함수를 다른 함수의 인자로 넘길 수 있거나 함수가 반환값으로
#### 넘겨줄 수 있으면, 언어가 고차 함수를 지원한다고 한다.

``` kotlin

val isPlus: (Int) -> Boolean = { it > 0 }

val hello: () -> "Hello World"

fun main() {
    listOf(1, 2, -3).any(isPlus)
    repeat(10) { println(hello()) }
}

```

### 49장 리스트 조작하기


``` kotlin
fun main() {
    // 순서대로 매핑된다.
    val names = listOf("커피", "설탕", "엔젤")
    val ages = listOf(2, 2, 4)
    val cats = names.zip(ages) { name, age -> "Name: $name, Age: $age" }
    println(cats)

    val names2 = listOf("커피")
    val ages2 = listOf(2, 2, 4)
    val cats2 = names2.zip(ages2) { name, age -> "Name: $name, Age: $age" }
    println(cats2)  --> "커피", 2 

    val listOfLists = listOf(
        listOf(1, 2, 3),
        listOf(4, 5, 6),
        listOf(7, 8, 9)
    )
    val flattenedList = listOfLists.flatten()
    println(flattenedList)
}
```


### 50장 맵 만들기

``` kotlin
fun main() {
    val mutableMap = mutableMapOf("a" to 1, "b" to 2)
    mutableMap["c"] = 3
    mutableMap["a"] = 10
    
    mutableMap.map { (key, value) -> "${key} => ${value}" }
    
    val originalMap = mapOf("Coffee" to 4, "설탕" to 6, "Angel" to 5)
    val nameLengthWithMap = originalMap.keys.associateWith { it.length }
    val nameLengthByMap = originalMap.keys.associateBy { it.length } --> 키가 중복되면 일부 값이 날라감
    println(nameLengthWithMap) "Coffee" to 6, "설탕" to 2, "Angel" to 5
    println(nameLengthWithMap) 6 to "Coffee", 2 to "설탕", 5 to "Angel"
    
    
    map.getElse(1)
}
```

### 51장 시퀀스

    코틀린에서 List에 대한 연산은 즉시(Eager) 처리되며 수평적 평가로 각 단계가 진행된다.
    코틀린에서 시퀀스(Stream 이라고도 부르는)에 대한 연산은 필요시에(Lazy) 처리되며 수직적 평가로 하나 하나 계산된다.


``` kotlin
지연 연산 예제
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val sumOfEvenSquares = numbers.asSequence()
        .map { it * it }
        .filter { it % 2 == 0 }
        .sum()
}

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        int sumOfEvenSquares = numbers.stream()
            .mapToInt(i -> i * i)
            .filter(i -> i % 2 == 0)
            .sum(); 
    }
}
```

#### 지연 연산 (Lazy Evaluation)
- 장점:
    - 효율성: 모든 중간 결과를 메모리에 저장하지 않아도 되므로, 큰 데이터셋을 처리할 때 메모리 사용량을 줄일 수 있습니다.
    - 성능 최적화: 최종 결과를 생성하는 데 필요한 요소만 처리하기 때문에 불필요한 연산을 피할 수 있습니다.
- 단점:
    - 디버깅 어려움: 지연 연산의 체인이 복잡해지면, 중간 결과를 확인하기 어려워 디버깅이 어려워질 수 있습니다.
    - 오버헤드: 아주 작은 데이터셋에서는 지연 연산의 오버헤드가 성능을 저하시킬 수 있습니다.

#### 즉시 연산 (Eager Evaluation)
- 장점:
    - 간결성: 즉시 연산은 더 익숙하고 이해하기 쉬운 패러다임을 제공합니다.
    - 디버깅 용이성: 각 단계에서 중간 결과를 쉽게 확인할 수 있어 디버깅이 더 간단합니다.
- 단점:
    - 메모리 사용: 각 중간 연산마다 새로운 컬렉션을 생성하기 때문에, 큰 데이터셋을 처리할 때 메모리 사용량이 증가할 수 있습니다.
    - 성능 저하: 불필요한 중간 컬렉션 생성과 데이터 복사로 인해 성능이 저하될 수 있습니다.


### 52장 지역 함수

``` kotlin
fun main() {
    val logMessage = StringBuilder()
    fun log(message: String) = logMessage.appendLine(message)
    log("Start computation")

    val x = 42
    log("computation result = $x")
    logMessage.toString() == """
        Start computation
        computation result = 42
    """
    fun String.Hi() = "Hello"
    "World".Hi() == "Hello"

    val lists = listOf(1, 2, 3, 4, 5)
    lists.any(
        fun(n: Int): Boolean {
            if (n % 2 == 0 && n > 3) {
                return true
            }
            return false 
        }
    )

}

fun 지역함수1() {
    val list = listOf(1, 2, 3, 4)
    val value = 3
    var result = ""
    list.forEach {
        result += "$it"
        if (it == value) {
            if (result == "123") {
                return
            }
        }
    }
    // 여기까지 오지 못함
    println(result)
}

fun 지역함수2() {
    val list = listOf(1, 2, 3, 4, 5)
    val value = 3
    var result = ""
    list.forEach {
        result += "$it"
        if (it == value) {
            if (result == "123") {
                return@forEach
            }
        }
    }
    result ==> "12345"
}

```

### 53장 리스트 접기

리스트를 단일 결과로 도출하기 위해서는 fold(), reduce()를 사용할 수 있다.\
fold는 초기 값을 가지고 시작하고, reduce는 첫 번째 요소를 시작값으로 시작한다.\
이에 fold는 빈 컬렉션에서도 안전하고, reduce는 빈 컬렉션의 경우 NoSuchException이 나온다.\
right를 붙이면 마지막 값부터 계산한다. ex: foldRight\
running을 붙이면 계산한 단계 값들을 저장한다. ex: runningFold

``` kotlin
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)

    val sumWithInitial = numbers.fold(10) { sum, element ->
        sum + element
    }

    sum ==> 25

    val sum = numbers.reduce { sum, element ->
        sum + element
    }
    sum ==> 15

    val runningSums = numbers.runningFold(0) { sum, element ->
        sum + element
    }

    runningSums ==> [0, 1, 3, 6, 10, 15]

}
```

### 54장 재귀 함수

코틀린에서 꼬리 재귀(Tail Recursion)는 특정 함수가 자기 자신을 호출하는 재귀 호출의 마지막 동작으로 수행될 때,
해당 호출을 최적화할 수 있는 기법입니다.\
이 최적화는 꼬리 재귀 최적화(Tail Call Optimization, TCO)라고 하며,
스택 오버플로우(Stack Overflow)와 같은 문제를 방지하고 재귀 함수의 성능을 개선하는 데 도움이 됩니다.

일반적인 재귀 호출에서는 각 호출마다 함수의 호출 스택이 쌓이게 되는데,
이는 메모리 사용량을 증가시키고, 호출 스택이 너무 깊어지면 스택 오버플로우 오류를 발생시킬 수 있습니다.\
반면, 꼬리 재귀에서는 컴파일러가 재귀 호출을 반복문(loop)으로 변환하여 실행하기 때문에,
호출 스택이 쌓이지 않습니다.

``` kotlin
tailrec fun sum(n: Int, accumulator: Int = 0): Int {
    return if (n <= 0) {
        accumulator
    } else {
        sum(n - 1, accumulator + n) // 꼬리 재귀 호출
    }
}

fun main() {
    val result = sum(100)
    println(result) // 5050
}

public class 꼬리재귀_자바로 {
    public static void main(String[] args) {
        int result = sum(100, 0);
        System.out.println(result); // 5050
    }

    public static int sum(int n, int accumulator) {
        while (n > 0) {
            accumulator += n;
            n -= 1;
        }
        return accumulator;
    }
}

public class 일반_재귀_자바로 {
    public static void main(String[] args) {
        int result = sum(100);
        System.out.println(result); // 5050
    }

    public static int sum(int n) {
        if (n <= 0) {
            return 0;
        } else {
            return n + sum(n - 1); // 재귀 호출
        }
    }
}

```