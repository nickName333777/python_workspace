# 모듈 module
# - .py 파일을 의미
# - 프로그램내에서 코드 재사용성을 높이기 위해 모듈 단위로 관리
# - 모듈 하위에 작성된 변수, 함수, 클래스 등은 외부에서 import해 사용 가능
# - 단, __ 로 시작하는 private한 자원은 외부에서 사용 불가 (getter/setter만들어 주어야 접근가능)

import math

print(math.pi) # 3.141592653589793

# dir: 빌트인 함수 - 특정 모듈의 사용 가능한 속성/메서드 나열
print(dir(math))#[ '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 
                #  'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 
                #  'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 
                #  'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 
                #  'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print(dir())    # 현재 모듈에서 사용 가능한 속성/메서드 나열
                # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math']


##########################################################
# 모듈명 확인
# - 현재 모듈을 실행 시에는 __main__ 반환
print(math.__name__) # "math" 반환
print(__name__) # __main__

# 사용자 모듈 가져오기
# - 파이썬 패키지로 모듈을 관리
# - 파이썬 패키지 하위 __init__.py 생성

x = 100

##########################
# from jr import my_math
# print(my_math.pi) # 3.143

# print(my_math.x) # 55 (my_math.py에 있는 x 값)

# print(my_math.__v) # 바밤바 (private인데도 접근가능 => 직접접근일때만  )
# # private 변수 직접 참조하면 접근 가능

# print(my_math.get_circle_area(5)) # 78.57499999999999

##########################
# from jr.my_math import *
# print(pi) # 3.143
# print(x) # 55  (global x는 import *시 덮어써진다.)
# #print(__v) # NameError: name '__v' is not defined ==> import *일때는 않됨
# # private 변수는 import * 시에는 제외된다.

# print(get_circle_area(5)) # 78.57499999999999


###########################
# 별칭 처리
from jr import my_math as m # import할때 my_math의 모든코드가 실행된다.
print(m.pi) # 3.143
print(m.x)  # 55
print(x)    # 100
print(m.__v)# 바밤바
print(m.get_circle_area(5)) # 78.57499999999999


# 이름 충돌을 주의해야 한다
# str = 'abc'
# print(str(123)) # TypeError: 'str' object is not callable => str()를 위에서 str = 'abc'로 덮어쓰기 해버려서 발생하는 오류

import math
math = 123 # ==> 모듈도 덮어쓰기 되버린다.

# 현재 모듈을 실행하는 경우만 하위 코드를 실행
# - 현재 모듈을 다른곳에서 import해서 사용하는 경우에는 하위 코드 실행하지 마라 (X)
if __name__ == "__main__":
    pass