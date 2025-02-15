## 2025 Kotlin Backend Meetup

### Kotlinx RPC

    kotlinx.rpc
    is a multiplatform Kotlin library
    Remote Procedure Calls using Kotlin languages constructs with as easy setup as possible

experimental -> 실험 단계의 라이브러리\
코틀린에서 배포할떄 가는 단계에서 초입

kotlin __X__

    코틀린의 확장함수 처럼 더 추가 기능을 제공해줄떄 확장 라이버러리 x 를 쓴다.

#### What is RPC
#### Remote Procedure Call
특징:
1. Network 를 라이브러리 한테 맡긴다
- local function call 같은 서버 내 
- RPC는 다른 서버에서의 실행
- 하지만 코드에서는 차이를 못느낌
- 마치 함수 호출처럼 다른 서버의 로직을 실행시키다.

2. RPC Client 와 RPC Server 가 transport 로 연결
- transport 는 흔히 말하는 전송계층

#### kotlinx.rpc
gRPC와 kotlinx의 공통점:
- 두 기술 다 비슷한 개념으로 개발

gRPC와 kotlinx의 차이점:
- 코틀린은 멀티플랫폼 코드이다.
  - 여러 언어에서 작동가능한 서버, 안드로이드, ios 등 여러 플랫폼에 적용가능
  - 모든 실행 환경에서 모든 환경에서 rpc를 쓸수 있다.
- 코틀린 x 시리얼라이즈를 지원 gRPC 는 JSON이 아님
  - kotlinx serialization!!! 확인 필요 >> 유뷰트 영상 참조
- 코루틴에서 지원하는 suspense ! withTImeOut 와 같은 처리 가능
- 전송 계층이 분리됬고 유저가 선택가능하다.
[코틀린 멀티팻폼 미지와의 조우 - JTK 매니지먼트](https://www.inflearn.com/course/%EC%BD%94%ED%8B%80%EB%A6%B0-%EB%A9%80%ED%8B%B0%ED%94%8C%EB%9E%AB%ED%8F%BC?srsltid=AfmBOopostaF-S34e7Joh7Y7G0dKXuNfLs1zcT0_GbWyFB1ZVdX4_yIf)

#### 이해를 높이려면 Ktor과 코루틴을 알아야한다!
#### dsl?????

###  코루틴 컴파일 과정 파헤치기

#### Coroutine 컴파일 
코루틴은 비동기 프로그래밍을 쉽게 하는 코틀린 문법
경량 쓰레드 
suspend 

suspend lambda?

```kotlin
var continuation: Continuation<Unit>? = null

suspend fun suspendIt(): Unit {
  return suspendCoroutine<Unit>{ c ->
    println(“Suspended”)
    continuation = c
  }
}

val cont = object : Continuation<Unit> {
    override val context = EmptyCoroutineContext
    override fun resumeWith(result: Result<Unit>) {
        result.getOrThrow()
    }
}

fun runBlocking(func: suspend () -> Unit) {
    func.startCoroutine(cont)
}

 fun main() {
    val lambda: suspend () -> Unit = {
      suspendIt()
      print(1)
      suspendIt()
      print(2)
    }
    
   runBlocking { 
       lambda()
   }
   continuation?.resume(Unit)
   continuation?.resume(Unit)
}

```

- COROUTINE_SUSPENDED? 
- 코루틴의 상태머신 처리 방법?

### Glided Rose 리팩터링 챌린지
Ktor 생태계?

[Gilded Rose refactoring!](https://github.com/parkjun5/GildedRose-Refactoring-Kata.git)

#### 목표
1. 점진적인 리팩터링 해보기
   - Ktlint plugin 으로 기본 포맷
   - 나중에 한번 깔끔하게 정리하기
2. 자주 사용하는 단축키

빌드 & 실행
- ⌘ + ⇧ + I : Gradle 새로고침 (Refresh Gradle)
- ⌃ + ⌃ (Control 두 번) : Gradle 태스크 실행

코드 편집
- ⌃ + G : 동일한 문자열 선택
- ⌘ + ⇧ + - : 클래스 내 모든 코드 블록 접기
- ⌘ + ⌥ + P : 변수를 파라미터로 추출
- ⌘ + F1 : 에러/경고 상세 설명 표시

유용한 코틀린 문법
- 숫자 범위 제한
```kotlin
// 값을 x와 y 사이로 제한
number.coerceIn(x, y)
```
범례:
- ⌘ (Command)
- ⌥ (Option/Alt)
- ⌃ (Control)
- ⇧ (Shift)
### Spring Webflux Overview

### 신입 개발자의 Kotlin, Kotest 입문기
