# 파일 하나하나가 다 모듈이다.

# scope 유효범위
# - 변수에 접근 가능한 범위
# - 전역 변수(global variable): 
#   -> "함수 블록" 밖에서 선언된 변수. 어디서든 접근 가능

# - 지역 변수(local variable): 
#   -> "함수 블록" 안(if, for문 블록은 해당않됨), 특정 모듈(.py), 특정 클래스/인스턴스에서 선언된 변수 

a = 100 # 전역 변수

def test1():
    print(a) # 전역변수 a (어디서든 접근가능)
    
    b = 200
    print(b) # 지역변수 b
    
test1()
print(a)
# print(b) # NameError: name 'b' is not defined ==> b는 test1()안에서 선언된 지역변수


for i in range(3):
    print(i) # 0, 1, 2
    
print(i) # 2 ==> for문 바깥에서도 쓸수 있다.(전역변수 i선언 한 것과 같다) => 전역변수 i

if True:
    value =100
    print(value)
    
print(value) # 100 ==>  if문 바깥에서도 쓸수 있다.(전역변수 value선언 한 것과 같다) => 전역변수 value

################################
# 변수 구분
glo = 10 # 전역
bal = 5  # 전역

def test2(a):
    glo = a + 10 # 지역변수 glo (전역변수 glo를 쓰고 있지 않다.) ==> 전역변수와 지역변수 같이 있으면 지역변수가 우선
    b = a + glo + bal # 
    # 지역 b = 지역 a + 지역 glo + 전역 bal 
    return b

print(test2(10)) # 35
print(test2(bal)) # 25

# 우선 순위
# - 가깝게 선언된 변수가 우선순위가 높다

##################################
# call by value | call by reference
# - immutable타입(int, float, bool, str, tuple; 불변타입) : call by value (값이 복사되어 처리)
# - mutable (원본값 바로바로 바꿀수 있는 애들: list, dict, set) : call by reference (참조값이 공유되어 처리)

def test3(a): # a는 int(immutable) ==> call by value
    a = 200 # a = 100은 100값만 복사 => 함수안에 a과 global a는 다른 주소값 가진다. ==> a는 "값" (call by value)
            # global a와 test3(a) 매개변수 a는 둘다 call stack에 생성되어 다른 주소값 갖는 다른 변수
    
a = 100
test3(a)
print(a) # 100

# heap : 실제 객체가 저장되는 메모리 공간

def test4(b): # ==> b는 "주소값" ==> call by reference
    b[1] *= 100  # b는 callstack에 생기는 주소값 담는변수고, 그 주소는 heap의 주소로, heap에 실제 리스트 객체가 그 주소에 생성되어 있다.
    
b = [1,2,3]
test4(b)
print(b) # [1, 200, 3]