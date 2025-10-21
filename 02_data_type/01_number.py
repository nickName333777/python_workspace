# 정수 int (cf. Java: int, long, short, byte; Java의 기본자료형은 8가지)
number = 123
print(number, type(number)) # 123 <class 'int'>

price = 123_456_789
print(price, type(price))  # 123_456_789 <class 'int'>

# 실수 float (cf. Java: float, double)
f_num = 123.456
print(f_num, type(f_num)) # 123.456 <class 'float'>

# 산술 연산
print(1 + 2)
print(7 - 5)
print(4 * 8)
print(6 / 2)

# 몫
print(10/3) # 3.3333333333335
print(10//3) # 3

# 나머지
print(10%3) # 1

# 거듭제곱
print(3**2) # 9
print(2**4) # 16

# 홀수 / 짝수
num = input('정수를 입력하세요 : ')
print(num, type(num)) # 333 <class 'str'> ==> 숫자로 입력했지만 얘는 String으로 인식

# print(num % 2 == 0) # Error => num은 String

num = int(input('정수를 입력하세요 : ')) # 입력한 값을 int 타입으로 변환: <class 'str'> -> <class 'int'>
print(num, type(num)) # 9 <class 'int'> ==> 숫자로 입력했지만 얘는 String으로 인식
print(num % 2 == 0) # True 짝수, False 홀수

print('짝수' if num%2 == 0 else '홀수') # 삼항연산자
# (True일때 값) if (조건식) else (False일때 값)