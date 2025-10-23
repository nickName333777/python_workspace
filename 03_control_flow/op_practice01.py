# 문제1.
def test1(weight, height):
    #print(f"체중입력(kg) : {weight}")
    #print(f"신장입력(cm) : {height}")
    #print("--------------------------")
    
    BMI = weight/(height/100)**2
    
    status = ''
    if (BMI < 18.5):
        status = "저체중"
    elif (18.5 <= BMI <23 ): # elif BMI <23: 로도 충분
        status = "정상체중"
    elif (23 <= BMI <25 ):
        status = "과체중"
    elif (25 <= BMI <30 ):
        status = "비만"
    elif (30 <= BMI ): # else 로도 충분
        status = "고도비만"   
    print(f"BMI 지수 : : {BMI:.2f}")
    print(f"{status}입니다")

#test1(67, 172)

while True:
    weight = int(input("체중입력(kg) : "))
    height = int(input("신장입력(cm) : "))
    print("--------------------------")
    test1(weight, height)
    
    break
    


def test2():
    while True:
        num1 = int(input("정수1 입력: "))
        op = input("연산자 입력: ") # + - * / %
        num2 = int(input("정수2 입력: "))
        
        # 입력값 검증
        if num1 < 0 or num2 < 0 or op not in [ '+', '-', '*', '/', '%']:
            print("연산자를 잘못입력하셨습니다. 프로그램을 종료합니다.")
            return
        if num2 == 0:
            print('0으로 나눌 수 없습니다')
            #return
            continue
        
        if op == '+':  #, '-', '*', '/', '%' 
            print(f"{num1} {op} {num2} = {num1 + num2}")
        elif op == '-': #, '*', '/', '%'
            print(f"{num1} {op} {num2} = {num1 - num2}")
        elif op == '*': # , '/', '%'
            print(f"{num1} {op} {num2} = {num1 * num2}")
        elif op == '/': # '%'
            print(f"{num1} {op} {num2} = {num1 / num2}")
            # if num2 != 0:
            #  print(f"{num1} {op} {num2} = {num1 / num2}")
            # else:
            #     print("0으로 나눌 수 없습니다.")
            
            
        elif op == '%':
            print(f"{num1} {op} {num2} = {num1 % num2}")
            # 여기서 3항 연산자로 처리가능
            #print(f'{num1} {cal} {num2} = {num1%num2}') if num2 != 0 else print("0으로 나눌 수 없습니다."
#test2()