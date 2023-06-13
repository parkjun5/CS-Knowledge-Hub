def recursion_fun(i):
    if i == 10:
        return
    print(i, '번째 재귀 함수 에서 ', i + 1, '번째 재귀 함수를 호출합니다')
    recursion_fun(i + 1)
    print(i, '번째 재귀 함수를 종료합니다')


recursion_fun(1)
