# for 반복문
# - iterable(반복 가능한) 객체 (str, list, tuple, dict, set) 여러개 요소를 가지고 있어서, 각 요소를 접근가능한 객체

name:str = '홍길동' # ctrl+shift+P 로 커맨드 창에서 >Terminal: Select Default Profile  => Command Prompt로 선택/설정( power shell prompt로 안간다)

for ch in name:
    print(ch)
    
foods: list[str] = ['피자', '햄버거', '국밥']
for food in foods:
    print(food)
    
cake: tuple[str] = ('딸기 케이크', '초코 케이크', '티라미수')
for c in cake:
    print(c)

##### type_hint에서 
# object : 모든 타입
# Any : 아무 타입
#user_info: dict[str, object] = {
from typing import Any

user_info: dict[str, Any] = {
    'name' : '홍길동',
    'age' : 42,
    'hobby' : ['독서', '개발']
}

for k in user_info:
    print(f'{k} = {user_info[k]}')
    
for k in user_info.keys():
    print(f'{k} = {user_info[k]}')
    
for k, v in user_info.items():
    print(f'{k} = {v}')
    
numbers : set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 짝수만 출력
for num in numbers:
    #print(num if num%2==0 else ' ', sep="; ")
    if num % 2 == 0:
        print(num)
        
# range 객체
# - range(start, end, step=1): start부터 end미만까지
r :range = range(1, 10)
print(r)

for n in range(1, 10, 1):
    print(n)
    
# 1부터 10까지 정수의 합: 55
n_sum = 0
for n in range(1, 11, 1):
    n_sum += n
print(n_sum)

# 1부터 100 사이의 홀수의 합: 2500
n_sum = 0
# for n in range(1, 101, 1):
#     if (n%2 != 0):
#         n_sum += n
for n in range(1, 101, 2): # step=2 => 1, 3, 5, 7, ... 홀수
    n_sum += n        
        
print(f'1 ~ 100 사이 홀수 합 : {n_sum}')

# 구구단 2단
'''
2*1 = 2
2*2 = 4
...
2*9 = 18
'''

for i in range(1, 10):
    print(f'2 * {i} = {2*i}')
    
    
# 구구단 2단 ~ 9단
'''
2*1 = 2
2*2 = 4
...
2*9 = 18

3*1 = 3
3*2 = 6
...
3*9 = 27
...

'''
for dan in range(2, 10):
    print(f'===== {dan}단 =====')
    for i in range(1, 10):
        print(f'{dan} * {i} = {dan*i}')
    print() # 개행
    
    
    
'''
행렬구조
- 행 : 바깥 반복문의 반복 횟수
- 열 : 안쪽 반복문의 반복 횟수
🍙🍙🍙🍙🍙
🍙🍙🍙🍙🍙
🍙🍙🍙🍙🍙
'''
for row in range(1, 4):
    for col in range(1, 6):
        print("🍙", end="") 
    print()
    
    
# 10행 5열 🍔출력
for row in range(1, 11):
    for col in range(1, 6):
        print("🍔", end="") 
    print()
    
#print(["🍔"+str(row) for row in range(1, 11) for col in range(1, 6)])

# zip 객체
# - 여러개의 iterable 객체를 묶어서 처리
names: list[str] = ['홍길동', '박철수', '김영희']
scores: list[int] = [70, 82, 95]
data = zip(names, scores)
print(data, type(data)) # <zip object at 0x000001F8C2397640> <class 'zip'>

for name, score in data: # zip으로 묶은데이터 한번 사용하면 끝
    print(f'{name}: {score}점')
    
for d in data: # 한번꺼내쓰면, 또 꺼내서 못쓴다
    print(d) # 아무것도 출력않됨, 바로 data다 꺼내서 iterate해서 위에서 다 썻음 => 출력 X
    
    
# enumerate 객체 
# - 인덱스와 함께 iterable 객체 순회 가능
foods: list[str] = ['포도', '사과', '바나나'] 
enum_foods = enumerate(foods)
print(enum_foods, type(enum_foods)) # <enumerate object at 0x0000017EA5375B70> <class 'enumerate'>

for index, food in enum_foods:
    print(f'{index} : {food}')
    

# enumerate 객체의 순회 결과는 인덱스, 요소 2개 이다.    
for index, (name, score) in enumerate(zip(names, scores)): # 다시 zip으로 묶어 data 생성
    print(f'index: {index}, name: {name}, score: {score}')
    
    
# 평균 점수
scores: list[int] = [100, 80, 43, 72, 55]
score_sum = 0
avg = sum(scores)/len(scores)

score_sum = 0
for score in scores:
    score_sum += score
print(score_sum/len(scores))
print(f'평균점수: {avg}')

# 학생 list에서 평균 점수 
students: list[dict[str, object]] = [
    {'name': '홍길도', 'score': 77},
    {'name': '박철수', 'score': 100},
    {'name': '김영희', 'score': 42},
]
score_sum = 0
for student in students:
    score_sum += student['score']
print('학생평균점수:', score_sum/len(students))

    
