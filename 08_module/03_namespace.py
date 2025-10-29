# namespace
# - 변수/함수등을 그룹핑해서 이름 충돌을 방지하는 개념
# - module, class, instance등을 namespace로 활용 가능

x = 10 # 전역 변수

# from jr.my_math import x
# print(x) # 55 => my_math에 있는 x값

from jr import my_math
print(my_math.x) # 55, my_math모듈의 x

print(f'x = {x}') # 10, 전역변수

class MyClass :
    x = 33 # 클래스 속성
    
    def __init__(self, x):
        self.x = x # 인스턴스 속성
        
# class 속성 (namespace)
print(MyClass.x) # 33 (클래스 객체 생성 필요없다. 클래스도 객체)

# instance 속성 (namespace)
my_cls = MyClass(777) # 인스턴스 속성은 일단 인스턴스 객체를 생성해야한다.
print(my_cls.x) # 777

##########    ==> 같은 x라도 클래스, 인스턴스에 의해 구분가능하게 된다.        
