# match case
# - 값으로써 분기처라하는 제어문 (Java의 switch case와 동일)
# - 3.10(2020년) 지원 ( ==> python version 호환성 생각해야 한다.)
# - break없다, 그래도 무조건 하나만 수행

"""
match 표현식(변수):
    case 값1:
        실행문
    case 값2:
        실행문    
    ...
    case _:
        기본실행문
"""

def test1():
    menu = input("음료 선택 (1. 아아 2.라떼 3.쥬스) : ")
    match menu:
        case "1" : # 자료형 맞춰저야함. break없음에 주의
            print("아아는 1600원 입니다.")
        case "2" :
            print('라떼는 2500원 입니다.')
        case "3" :
            print("쥬스는 2200원입니다.")
        case _ : # default
            print("잘못 입력하셨습니다.")
            
    print("이용해 주셔서 감사합니다.")
    
#test1()


def test2(op, x, y):
    match op:
        case "+":
            print(f'{x}+{y} = {x+y}')
        case '-':
            print(f'{x}-{y} = {x-y}')
        case '*':
            print(f'{x}*{y} = {x*y}')
        case '/':
            print(f'{x}/{y} = {x/y}')
        case '//':
            print(f'{x}//{y} = {x//y}')
        case '%':
            print(f'{x}%{y} = {x%y}')            
        case _:
            raise ValueError(f'{x}-{y} = {x-y}')  
        
        
# test2("+", 10, 3) #13          
# test2("-", 10, 3) #7          
# test2("*", 10, 3) #30          
# test2("/", 10, 3) #3.33333333          
# test2("//", 10, 3) #3          
# test2("%", 10, 3) #1
# test2("#", 10, 3) # # ValueError: 10-3 = 7 연산자가 부적절합니다.
    
def test3():
    """if/ elif/ else 대체하는 match..case(docstring)"""
    num = int(input("정수 입력 :"))
    match num:
        case num if num > 0 :
            print("양수 입니다.")
        case num if num < 0:
            print("음수입니다.")
        case _:
            print("0입니다.")
            
#test3()


def test4(value): # 파이썬에만 있는 사용법
    """ tuple값 세부 검사"""
    match value:
        case (1, 2) :
            print('(1,2)가 전달되었습니다.')
        case (1, k) if k < 0 :
            print('(1, 음수)가 전달되었습니다.')
        case (1, _):
            print('(1, n)가 전달되었습니다.')
        case _ : 
            print('그 외의 경우')
            
# test4((1, 2))
# test4((1, -2))
# test4((1, 20))
# test4((10, 20))


def test5(application):
    """dict의 특정 key값 세부 검사"""
    match application:
        case {'type': 'dev', 'career': career} if career >= 10:
            print('중견 개발자 지원입니다.')
        case {'type': 'dev'} :
            print('개발자 지원입니다')
        case {'type': 'devops'} :
            print('운영/개발자 지원입니다')
        case _:
            print('기타 지원입니다.')    
            
# test5({'type' : 'dev', 'career': 14})
# test5({'type' : 'dev', 'career': 4})
# test5({'type' : 'devops', 'career': 0})
# test5({'type' : 'HR', 'career': 0})



def test6():
    
    score: int = int(input('시험 점수 입력 : '))  
    grade = None
    
    # 사용자 입력값 유효성 검사
    # 0 ~ 100 사이 점수가 아닌 경우
    if not(0 <= score <= 100):
        # -> 파이썬은 연쇄 비교 지원 : 0 <= score and score <= 100으로 자동 변환
        #print("test") 
        raise ValueError("0에서 100사이 점수를 입력해 주세요.") # 오류 던짐
                  
           
           
    # 등급지정
    match score: # 변하는 값
        case score if score >= 90 :
            grade = 'A'
        case score if score >= 80:
            grade = 'B'
        case score if score >= 70:
            grade = 'C'
        case score if score >= 60:
            grade = 'D'
        case _:
            grade = 'F'

    print(f'점수는 {score}점이고 등급은 {grade}입니다.')    
        
test6()   
    