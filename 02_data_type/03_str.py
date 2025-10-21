# str
# - 문자열
# - '', "", ''' ''', """ """

hi = '안녕'
print(hi, type(hi))

str = """
문자열 입니다.
주석 주석아닙니다.
"""
print(str, type(str)) #  <class 'str'>

# 더하기 연산
print('🚒' + '🚋🚟') # 이모지: Window-key + .

# 곱하기 연산
print('🍕'*10)  # 문자열만 있고, CHAR의 개념이 없다. 

# # 빼기 연산 X
# print('가나다' - '마바사') 
# # TypeError: unsupported operand type(s) for : 'str' and 'str' 

# 문자열(문자 + 배열)
# - 인덱스를 통해 접근 가능
# - 0-based index : 0부터 시작, 마지막 인덱스는 길이 -1 (Java랑 같다)

day = 'Friday'
print('day의 길이 : ', len(day))
print(day[0], day[1], day[2], day[3], day[4], day[5])
#print(day[6]) # Error: IndexError: string index out of range

# 역인덱스
print(day[-1]) # y
print(day[-2]) # a
print(day[-6]) # f

# slicing : 문자열의 일부를 가져오는 방법
# - [start:end:step]
# - start : 시작하는 인덱스 (포함 inclusive)
# - end : 종료 인덱스 (포함X, exclusive)
# - step : 건너뛸 개수(기본값 1)
txt = "Hello World"
print('txt의 길이 : ', len(txt)) # 11
print(txt[:5]) # Hello
print(txt[0:5:1]) # start:end:step
print(txt[0:5]) # step 생략시 기본값 1로처리
print(txt[:5]) # start 생략시 기본값 0으로처리: 0번 인덱스부터 slicing

print(txt[6:11]) # world
print(txt[6:]) # end 생략시 끝까지 slicing

print(txt[:]) # 처음부터 끝까지 출력
print(txt[::2]) # 0,2,4,6,8,10

print(txt[::-1]) # step이 음수인 경우 뒤에서 부터 가지고 온다.

# 문자열 불변타입(immuntable)
# - 메모리에 할당된 값을 수정할 수 없다. 
# - 수정하면 새 값을 할당한다
str = 'hello'
print(id(str)) # 실제 메모리 값을 확인: 1793120883296

str = str + "world"
print(id(str)) # 메로리값 변경 1793120927088

# in : 특정값이 포함 되었는지 여부 (멤버쉽검사)
txt = '안녕하세요'
print('안녕' in txt) # True
print('졸려' in txt) # False
print('졸려' not in txt) # True

# formatting(포멧팅): 형식 문자열의 일부를 다른 변수/값으로 치환 (printf와 유사)
# - f-string : 3.6부터 지원
# - %
# - str.format()
x = 10
y = 5.5
print('%d + %.2f = %d'%(x, y, x+y)) # 15
print('{} + {} = {}'.format(x, y, x+y)) # 15.5
print(f'{x} + {y} = {x+y}') # 15.5


# str api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#str

# str.replace(old, new)
# - 특정문자열을 치환해서 새문자열 반환
today = '2025-10-21'
today = today.replace('-', '/')
print(today)

# str.strip() # 
# - 시작/끝부분 공백 제거
str = '      수업 종료 50분전!!           '
print(str)
print(str.strip())