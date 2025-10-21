# 논리형 Boolean
# - bool

t = True
f = False

print(t, type(t)) # True <class 'bool'>
print(f, type(f)) # False <class 'bool'>

# 비교 연산 결과값
result = 1 > 0.5 # 좌항을 기준으로 연산자를 읽어야 한다. gt(greater than)
result = 1 < 0.5 # lt(less than); 대입연산(=), 비교연산(<)
result = 1 >= 0.5 # ge (greater than or equal to)
result = 1 <= 0.5 # le (less than or equal to)
result = 1 == 1 # 동등비교연산자
result = (1 != 1) # 부정동등비교연산자

print(result, type(result))

print(not t) # 논리형 반전
# and 연산
# - (좌항)과 (우항)이 모두 참일때만 참
# T and T -> T
# T and F -> F
# F and T -> F
# F and F -> F
print('--- and ---')
print(100 > 0 and 1 == 1) # True
print(30 > 20 and 11 != 11) # False
print(3 <= 0 and 1 == 1) # False

# or 연산
# - (좌항) 또는 (우항) 하나라도 참이면 참
# T or T -> T
# T or F -> T
# F or T -> T
# F or F -> F
print('--- or ---')
print(100 > 0 or 1 == 1) # T
print(30 > 20 or 11 != 11) # T
print(3 <= 0 or 1 == 1) # T

# 합격 여부(과목별 60점 이상인 경우 합격, 아니면 불합격)
kor = 70
eng = 65
print('합격' if kor >= 60 and eng >= 60 else '불합격')

# 할인 대상 여부
# -> 금일 생일자 혹은 쿠폰 소지자
#    둘중 하나라도 해당하면 할인가능, 아니라면 할인 불가 출력
is_birthday = True
has_coupon = False
print('할인가능' if is_birthday or has_coupon else '할인불가')