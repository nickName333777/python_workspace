# Function 함수
# 선언 후 호출해서 사용
# 호출(실행)시에 함수 쪽으로 값을 전달할 수 있고, 결과값을 반환 받을 수 있다.

def add(a, b): # 선언부
    print(f'a = {a}, b={b}')
    return a + b

result = add(10, 20)
print(result)
print(add, type(add)) # <function add at 0x000001A5C6F13920> <class 'function'>

result = add('Hello', 'world')
print(result)

result = add([1,2,3], ['가', '나', '다']) # 호출부
print(result)

result = add([], ['가나다']) # 호출부
print(result)

# 매개변수 | 매개인자(인수)
# - 매개변수(parameter) : 함수 선언부의 변수
# - 매개인자(arguments) : 함수 호출부의 전달되는 값

def fruit(a, b): # 선언부
    print(f'a = {a}, b = {b}')    

result = fruit('사과', '딸기') # 호출부
print(result) # None

# 리턴값
# - 함수 호출 시 함수 선언부의 코드를 실행하고, 
#   이를 마치면 호출부로 반드시 돌아온다. (return)
# - 리턴시에 값 "하나"를 함께 가져올 수 있다. (return 선언부가 없으면 None반환)

def color():
    print('color')
    return 0

print(color())

# 함수는 하나의 값(리터럴)로 처리될 수 있다.(JS와 같다)
# - 1급 시민 객체(First-class citizen): 값처럼 다룰 수 있는 자료형/객체
c = color # 함수명만 변수에 담고
c() # 호출부에서 호출
print(c, color, type(c)) # <function color at 0x000001FA2E704540> <function color at 0x000001FA2E704540> <class 'function'>
print(color is c) # true


def runner(f):
    """함수 실행기"""
    f()
    
runner(c) # color;     c     -> <function color at 0x00000188793E4540>
runner(color) # color  color -> <function color at 0x00000188793E4540>

# 호출 방식
# 1. 위치 매개인자 전달: 작성한 순서대로 전달
# 2. 키워드 매개인자 전달: key=value에 따라 동일한 이름의 key 매개변수에 전달

def test(a, b):
    print(f'a = {a}, b = {b}')
    
test(10, 20)
test(a=1, b=2)
test(b=1, a=2)
#test(b=1, a=2, c=3) # TypeError: test() got an unexpected keyword argument 'c'
test(100, b=200) # 혼용가능, but 위치매개인자가 앞에 와야함, 그 뒤에 키워드 매개인자 순으로 작성해야 한다.
#test(b=200, 100) # SyntaxError: positional argument follows keyword argument



#  매개변수 기본값 지정(key=value의 형태로 기본값이 지정되므로, 항상 positional parameter뒤에 와야함)
# - 기본값이 지정된 매개변수는 항상 오른쪽에 위치해야 한다.

#def test2(name='김', age, married=False): # SyntaxError: parameter without a default follows parameter with a default   
def test2(name, age, married=False):
    print(f'name = {name}, age = {age}, married = {married}')

test2('홍길동', 33) 
# 선언부에 기본값 지정않된 경우: TypeError: test2() missing 1 required positional argument: 'married'

test2('박철수', 22, True)

#test2('영희') # TypeError: test2() missing 1 required positional argument: 'age'



#################
# packing 연산자
# - 반드시 "매개변수" 또는 "좌항"에서 사용된다.
# - *args : n개의 위치"매개인자"가 대입될 "매개변수"


def test3(*args):
    print(args, type(args))
    return sum(args)
    
print(test3(1,2,3))     #  (1, 2, 3) <class 'tuple'>; 6 
print(test3(1,2,3,4,5,6,7,8,9,10))     #  55

def test4(emoji, *args) :
    print(f'emoji = {emoji}, args = {args}')
    
test4('🥓', 1, 2, 3) # emoji = 🥓, args = (1, 2, 3)
test4('🥓', 1) # emoji = 🥓, args = (1,)
test4('🥓') # emoji = 🥓, args = ()


# - **kwargs : n개의 키워드 매개인자가 대입될 매개변수
def test5(**kwargs):
    print(kwargs, type(kwargs))
    
test5() # {} <class 'dict'>
test5(name='홍길동', age=30, hobby = ['등산', '배드민턴']) # {'name': '홍길동', 'age': 30, 'hobby': ['등산', '배드민턴']} <class 'dict'>


# 매개변수 작성 시 주의사항
# - 일반매개변수 - *args - **kwargs 순서로 작성
# - 기본값이 있는 매개변수 오른쪽에 작성하면 된다.

def test6(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)
    
test6(10, 20, 30, 40,50, 60, color='red', fruit='딸기')
    
    
# unpacking
# - *list : 리스트의 요소를 꺼내어 나열하는 연산자. 매개인자 자리에서 사용
# - **dict : 사전의 요소를 꺼내어 키워드 방식으로 나열하는 연산자.
# -> 매개인자 자리에서 사용

names = ['홍길동', '박철수', '김영희']
def test7(*args): # *args : packing
    print(args)
    
test7(names) # (['홍길동', '박철수', '김영희'],)
test7(names[0], names[1], names[2]) # ('홍길동', '박철수', '김영희')
test7(*names) # # *names : unpacking, ('홍길동', '박철수', '김영희') <=== unpacking

info = {'date': '2025-10-23', 'time': "15:40"}

def test8(date, time):
    print(date, time)
    
test8(date ='2025-10-23', time= "15:40")
test8(date =info['date'], time= info['time'])
test8(**info) # dict unpacking해도 같은 효과

# 위치전용 positional-only, 키워드전용 keyword-only ==> 3.8버전부터
# / : /앞은 위치 전용으로만 호출 가능
# * : *뒤는 키워드 전용으로만 호출 가능
def test9(name, /, greeting="안녕"):
    print(name, greeting)
    
test9('길동아')
#test9(name='길동아') # TypeError: test9() got some positional-only arguments passed as keyword arguments: 'name'

def test10(a, *, b, c):
    print(a, b, c)
    
#test10(1, 2, 3) # TypeError: test10() takes 1 positional argument but 3 were given
test10(1, b=2, c=3) # 1 2 3


###########
# 함수 type_hint
def test11(a: str, b: int) -> str: #결과값도 str이라는 type_hint
    #return a + b # Error:  # TypeError: can only concatenate str (not "int") to str
    return a + str(b)

print(test11('안녕', 123))