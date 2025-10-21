import math

''' 함수 선언 '''
def test():
    num = 123
    print(num)
    
    
""" 함수 호출(실행)"""
#test()


def test1():
    """1번 실습문제 풀이"""
    num = float(input("입력 : ")) # String -> 숫자(float)으로 바꿔 주어야함
    print(round(num, 0), '(반올림)', math.ceil(num), '(올림)'
          , math.trunc(num), '(버림)', math.floor(num), '(내림)' )
    # .앞은 객체나 모듈이 온다
    # -3.14: trunk -> -3 , floor-> -4 
    '''
    (참고) 파이썬의 반올림
    - 일반 반올림 : 0.5이상이면 올림
    - Banker's Rounding : 소수점아래가 0.5일때, 바로 앞 숫자가
                          짝수면 그대로 유지, 홀수면 올림해서 짝수로 만든다
      0.5 + 1.5 + 2.5 + 3.5 +4.5+ 5.5+6.5+7.5+8.5+9.5 => 그냥 다 올리면 숫자가 커진다(사사오입) ==> 반올림 경계값 .5 일때
      1   + 2   + 3   + 4   + 5  + 6 + 7 + 8 + 9 + 10 => 그냥 다 올리면 숫자가 커진다(사사오입)
      0   + 2   + 2   + 4   + 4  + 6 + 6 + 8 + 8  + 10 => Banker's Rounding(파이썬에서의 방식)
    '''
    
# test1()

def test2():
    """2번 실습문제 풀이"""
    num1 = float(input("숫자입력1 : "))
    num2 = float(input("숫자입력2 : "))    
    print('True' if num1==num2 else 'False')    
    
#test2()



def test3():
    """3번 실습문제 풀이"""
    x = int(input("정수입력:"))
    print('True' if x >= 10  and x <= 100 else 'False' )

# test3()





def test4():
    """4번 실습문제 풀이"""
    num = float(input("실수 입력:"))
    print
    print('True' if (int(num)%2 == 0 and round(num) == int(num)+1) 
          or (int(num)%2 ==1 and round(num) > int(num))  else 'False')
    
#test4()  #  <===


def test5():
    """5번 실습문제 풀이"""
    num = float(input("실수입력:"))
    print(math.ceil(num) <10 and math.trunc(num) >= 5 )
    #print(math.ceil(num) < 10)
    #print(math.trunc(num) >= 5)
    
    
#test5()



def test3():
    """3번 실습문제 풀이"""
    
test3()



def test3():
    """3번 실습문제 풀이"""
    
test3()



def test3():
    """3번 실습문제 풀이"""
    
test3()



def test3():
    """3번 실습문제 풀이"""
    
test3()



def test3():
    """3번 실습문제 풀이"""
    
test3()


