# 형변환
# - 암묵적 또는 명시적으로 자료형을 변환하는 것
# - 자동형변환 / 강제형변환

# 1. 암묵적 형변환 (자동형변환)
print(1 + 2.3) # int + float -> float + float -> float
print(True + 2) # bool + int -> int + int -> int (True는 1, False는 0)
print(True + False) # bool + bool -> int + int -> int

# 2. 명시적 형변환 (강제형변환)
#print("점심시간" + 1320) # TypeError: can only concatenate str (not "int") to str
print("점심시간" + str(1320)) # 점심시간1320 # str + str -> str  

height = 168.53
print(int(height)) # 168

value = "3.141592"
print(value*10) # 3.1415923.1415923.1415923.1415923.1415923.1415923.1415923.1415923.1415923.141592
print(float(value)*10) # 31.41592

# 3. 논리형으로의 암묵적 형변환
# - 값이 있으면 True, 값이 없으면 False
#
# True
print(100, bool(100)) # 100 True
print(-100, bool(-100)) # -100 True (음수도 어쨋든 값이 있는것)
print(' ', bool(' ')) # (띄어쓰기도 어쨋든 값이 있는것)
print('문자', bool('문자')) # 문자열
print([1,2], bool([1,2])) # 리스트
print((1,2), bool((1,2))) # 튜플
print({'is_friday':True}, bool({'is_friday':True})) # 딕셔너리

# False
print(0, bool(0))
print(0.0, bool(0.0))
print('', bool(''))
print([], bool([]))
print((), bool(()))
print({}, bool({}))


lst = [1, 2, ]
if lst : # 암묵적으로 리스트를 boolean으로 쓴것
    print('list에 요소가 존재합니다.')
else : 
    print('list에 요소가 존재하지 않습니다.')
