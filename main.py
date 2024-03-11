# 예제 계산기
import cal


while True:

    # 계산할 값을 입력
    a = int(input("첫번째 값을 입력하세요."))
    if a == 'q':
        break
    b = int(input("두 번째 값을 입력하세요."))
    mark = input("입력하세요 : [+, -, /, *]")

    # 사칙연산을 골라야 함.
    if mark == '+':
        print("결과값 : {}".format(cal.add(a, b)))
    elif mark == '-':
        print("결과값 : {}".format(cal.minus(a, b)))
    elif mark == '*':
        print("결과값 : {}".format(cal.doble(a, b)))
    elif mark == '/':
        print("결과값 : {}".format(cal.divide(a, b)))

    

    # 변경확인
    