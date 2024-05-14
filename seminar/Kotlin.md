## 코틀린 2부

### 16장 객체는 모든 곳에 존재한다

- 클래스: 사용자 지정 타입 -> 상태와 행동을 정의
- 멤버: 클래스에 속한 속성, 함수
- 멤버 함수: 사용자 지정 타입 내부 함수
- 객체 생성: 사용자 지정 타입을 인스턴스로 바꾸는 과정

``` text
IntRange(x, y) -> 클래스
val A = IntRange(x, y) -> 객체 생성
A::sum -> 멤버 함수
A.sum() -> 멤버 함수 호출 
```

### 17장 클래스 만들기

``` kotlin
class Cat() {
    fun meow() = "냐옹"
}

fun main() {x`xx
    val cat = Cat()
    val m1 = cat.meow()
    println(m1)
}
```


### 18장 프로퍼티

클래스에 속한 var or val

프로퍼티를 통해 클래스 안에서 상태를 유지한다

``` kotlin
class Cat {
    val age = 0
    fun meow() = "냐옹"
    
    fun add(increase: Int) {
        age += increase
        
        if( age < 0) {
            age = 0
        }
        return age
    }
    
    co
}

fun main() {
    val cat = Cat()
    println(cat.age)
    cat.age = 15
    println(cat.age)
    cat.add(15)
    println(cat.age)
}
```

### 19장 생성자

``` kotlin
class Cat(name: String) {
    fun meow() = "$name 냐옹"
}

class Cat2(val name: String) {
    fun meow() = "$name 냐옹"
}


fun main() {
    val cat = Cat("커피")
    println(cat.meow())
    println(cat.name) --> 에러 발생!
    
    val cat2 = Cat2("설탕")
    println(cat2.meow())
    println(cat2.name)
}
```

### 20장 가시성 제한하기

``` kotlin
private var index = 0

private class Animal(val name: String)

private fun recordAnimal(
    animal: Animal
) {
   println("Animal #$index: ${animal.name}" 
   index++
}

fun recordAnimals() {
    recordAnimal(Animal("Tiger")
    recordAnimal(Animal("Antelope")
}

fun recordAnimalCount() {
    println("$index animal!")
}
```
파일 자체가 클래스처럼 사용된다

### 21장 패키지


``` kotlin
import kotlin.math.PI as 파이

fun main() {
    println(파이)
    println(kotlin.math.PI)
}
```

### 24장 리스트

    kotlin은 List가 기본으로 포함되어있어서 import가 필요없음
    리스트는 listOf를통해 만들어지며 자바처럼 기본은 불변리스트이다
    mutableListOf로 해야 가변 리스트
    기본적으로 타입 추론을 지원한다
    불변 리스트 listOf도 var에 넣으면 가변이 된다.
    +=, -= 연산자로 연소를 추가하거나 삭제할 수 있다.

### 가변 인자 목록

    이 값은  array로 처리됨
    *를 붙이면 array가 아니라 인자 목록이 전달된다