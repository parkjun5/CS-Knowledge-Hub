## 코틀린 5부

### 67장 봉인된 클래스

    클래스 계층을 제한하려면 상위 클래스를 seal로 제한하라

``` kotlin

package withoutsealedclasses

open class Transport

data class Train(
    val line: String
): Transport()

data class Bus(
    val number: String,
    val capacity: Int
): Transport()

fun travel(transport: Transport) =
    when (transport) {
        is Train ->
            "Train ${transport.line}"
        is Bus ->
            "Bus ${transport.number}:" +
            "size ${transport.capacity}"
        else -> "$transport is in limbo!"
    }


```
open 되어 있을 경우 else가 필요하다

``` kotlin

package withsealedclasses

sealed class Transport

data class Train(
    val line: String
): Transport()

data class Bus(
    val number: String,
    val capacity: Int
): Transport()

fun travel(transport: Transport) =
    when (transport) {
        is Train ->
            "Train ${transport.line}"
        is Bus ->
            "Bus ${transport.number}:" +
            "size ${transport.capacity}"
    }


```
sealed 되어 있을 경우 경우 상속한 하위 클래스는 반드시 기반 클래스와 같은 패키지와 모듈안에 있어야한다.
또한 sealed로 설정한 클래스의 하위 객체들은 쉽게 찾을 수 있다.

``` kotlin

package withsealedclasses

sealed class Top
class Middle1: Top()
class Middle1: Top()
class Middle2: Top()
open class Middle3: Top()
class Bottom3: Middle()


fun findSealeds() {
    Top::class.sealedSubClasses
    .map {it.simpleName} eq {Middle1, Middle2, Middle3 }
}

```

여기서 sealedSubClasses는 리플랙션을 사용한다.\
다형성을 사용하는 시스템에서 유용하게 사용할 수는 있지만 모든 SubClass를 동적으로 찾아서 성능상 문제가 될 수 있다.

### 68장 타입 검사

    코틀린에서는 객체 타입에 기반해 원하는 동작을 쉽게 수행할 수 있다.
    일반적으로 이런 타입에 따른 동작은 다형성의 영역에 속하므로 타입 검사를 통해 흥미로운 설계가 가능하다.

``` kotlin

interface Insect {
    fun walk() = "$name: walk"
    fun fly() = "$name: fly"
}

class HouseFly: Insect

class Flea: Insect {
    override fun fly() =
    throw Exception("Flea cannot fly)
    fun crawl() = "crwal"
}

fun Insect.basic() =
    walk() + " " +
        if (this is Flea.)
            crawl()
        else
            fly()


fun Insect.basic2() =
    when(this) {
        is Flea -> crawl()
        is HouseFly -> fly()
        else -> walk()
    }

val Any.name
    get() = this::class.simpleName

```

### 69장 내포된 클래스

    내포된 클래스를 사용하면 객체 안에 더 세분화된 구조를 정의할 수 있다.

``` kotlin
class Airport(private val code: String) {
    open class Plane {
        fun contact(airport: Airport) = "Contacting ${airport.code}"
    }
    private class PrivatePlane: Plane()
    fun privatePlane(): Plane = PrivatePlane()

}
```

이너 클래스의 장점은 private code에 접근 할 수 있는 점이다.

####  정적 내포된 클래스(Static Nested Classes):

    정적 내포된 클래스는 외부 클래스의 인스턴스와 독립적이다
    코틀린에서는 내포된 클래스가 기본적으로 정적으로 간주 함
    즉, 자바의 static class와 유사하게 작동하고, 외부 클래스의 인스턴스 없이도 생성 및 사용이 가능하다.
``` kotlin
class Outer {
    class Nested {
        fun demo() = "This is a nested class"
    }
}
````
여기서 Nested 클래스는 Outer 클래스 내부에 정의되어 있지만, Outer 클래스의 인스턴스 없이도 Nested 클래스의 인스턴스를 생성할 수 있다

#### 내부 클래스(Inner Classes):

    내부 클래스는 외부 클래스의 인스턴스에 대한 참조를 유지함.
    내부 클래스를 선언하기 위해서는 클래스 앞에 inner 키워드를 추가해야함
    이로 인해 내부 클래스는 외부 클래스의 속성과 메소드에 접근할 수 있음
``` kotlin
class Outer {
    private val bar: Int = 1
        inner class Inner {
            fun foo() = bar
    }
}
```

Inner 클래스는 inner 키워드로 선언되어 Outer 클래스의 bar 속성에 접근한다.
이 경우 Inner 클래스의 인스턴스는 Outer 클래스의 인스턴스에 종속된다.

### 70장 객체

    object 키워드는 대충 보면 클래스처럼 보이는 무언가를 정의한다. 하지만 object의 인스턴스를 생성할 수는 없다.
    object의 인스턴스는 오직 하나만 존재한다. 이것을 싱글턴 패턴이라고 한다.

```kotlin
    object JustOne {
        val n = 2
        fun f() = n * 10
        fun g() = this.n * 20
    }

    fun main() {
        // val x = JustOne() <<= 에러 발생
        JustOne.f()
        JustOne.g()
    }
```

```kotlin
    open class Paint(val color: String) {
        open fun apply() = "Applying $color"
    }

    object Acrylic: Paint("blue") {
        override fun apply(): String = "Acrylic" +  super.apply()
    }

    interface PaintInterface {
        fun prepare(): String
    }

    object Prepare: PaintInterface {
        override fun prepare(): String = "Prepare"
    }

```

### 71장 내부 클래스

### 내포된 클래스 (Nested Classes):
- __정적 특성__: 코틀린에서 내포된 클래스는 기본적으로 '정적(static)'이다.\
즉, 외부 클래스의 인스턴스 없이도 내포된 클래스의 인스턴스를 생성할 수 있다.
- __독립성__: 내포된 클래스는 외부 클래스의 인스턴스와 독립적이다.\
내포된 클래스 내에서 외부 클래스의 멤버에 직접 접근할 수 없음(외부 클래스의 static 멤버는 접근 가능)
- __사용 사례__: 내포된 클래스는 주로 헬퍼 클래스나 테스트 클래스를 구현하는 데 사용되며,\
이들은 외부 클래스와 로직적으로 연결되어 있지만, 인스턴스 간의 직접적인 연결은 필요하지 않은 경우에 적합하다.

```kotlin
class Outer {
    class Nested {
        fun demo() = "This is a Nested class"
    }
}
val nested = Outer.Nested()
```

### 내부 클래스 (Inner Classes):
- __비정적 특성__: 내부 클래스는 inner 키워드를 사용하여 선언된다.\
이 키워드는 클래스가 외부 클래스의 인스턴스에 종속됨을 의미한다.
- __외부 클래스__ 멤버 접근: 내부 클래스는 외부 클래스의 모든 멤버(속성과 메서드)에 접근한다.\
이는 내부 클래스가 외부 클래스의 인스턴스와 연결된다.
- __사용 사례__: 내부 클래스는 외부 클래스의 인스턴스와 밀접하게 연관된 작업을 수행할 때 사용\
예를 들어, 외부 클래스의 상태를 수정하거나, 외부 클래스의 메서드를 호출하는 등의 작업을 내부 클래스에서 수행할 수 있음

```kotlin
class Outer {
    private val greeting: String = "Hello"

    inner class Inner {
        fun sayHello() = "$greeting from the inner class"
    }
}
val outer = Outer()
val inner = outer.Inner()
```

### 72장 gka
    멤버 함수는 클래스의 특정 인스턴스에 작용한다.
       함수가 아닐 수 있다. 이런 함수는 특정 객체에 매여 있을 필요가 없다.

#### 자바의 static 메소드와 필드와 유사한 기능을 제공

```kotlin
class MyClass1 {
    companion object Factory {
        const val CONSTANT = "constant"

        fun create(): MyClass1 = MyClass1()
    }
}

// 동반 객체의 멤버에 접근
val instance1 = MyClass1.create()
println(MyClass1.CONSTANT)


class MyClass2 {
    companion object {
        fun create(): MyClass2 = MyClass2()
    }
}

val instance2 = MyClass2.create() // 동반 객체의 이름 없이도 접근 가능

```