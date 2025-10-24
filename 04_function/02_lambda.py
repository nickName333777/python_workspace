# lambda 람다
# - 함수를 한 줄로 간결히 선언하는 문법
# - lambda x, y : z
# - x, y : 매개변수
# - z: 리턴값
# lambda도 1급 시민 객체

#def square(x):
#    return x**2

square = lambda x: x**2
    
#print(square(2))
#print(square(3))

def test1():
    #return [ n**2 for n in range(1, 101)]
    #return [square(n) for n in range(1, 101)]
    return [(lambda x: x**2)(n) for n in range(1, 101)] # n을 lambda함수 안에서 x라고 부른다.
            # (lambda x: x**2): 함수 선언
            # (lambda x: x**2)(n): 호출

#print(test1())

def test2():
    """ 하나 이상의 매개변수 선언 가능 """
    add = lambda a, b : a + b # 1급 시민 객체
    print(add(10, 20))
    
# test2()

def test3():
    """ 
    기본값 선언, 
    packing연산자 *args, **kwargs 모두 사용 가능 
    """
    multiple = lambda x, y=1: x*y # keyword 기본값 = 1
    print(multiple(10))
    print(multiple(10, 20))
    
    adder = lambda *args : sum(args)
    print(adder(1,2,3,4)) # 10
    print(adder(1,2,3,4, 5, 6, 7, 8, 9)) # 45

    
test3()