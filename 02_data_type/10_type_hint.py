# type_hint
# - 파이썬은 동적 타이핑을 지원한다.
# - 변수에는 자료형이 없고, 대입되는 리터럴에 따라서 자료형이 결정된다.
# - 정적 코드 작성시에 타입 검사를 수행하는 type_hint를 지원
# - 실제 실행 시에는 무시된다(즉, 힌트만 주고, 실제 실행때 바인딩하는 동적 타이핑 수행)

x = 11
x = '8분전'
def act(x): # x에 뭐가 들어 올지 알수 없어서, x에 들어올게 무엇인지 지정해주는 것이 type_hint, but 실제 실행시에는 무시
    '''
    x를 가지고 문자열로 바꿔주는 함수: 
    '''
    print(x)
    
    
# type hint
# 콜론(:) 옆에 써주는 경우
greeting: str = 'hello'
greeting = 123
print(greeting)

num: float = 123.45
score : int = 100
has_coupon: bool = True

# 대괄호안에 type_int 넣어주는 경우:
nums: list[int] = [1, 2, 3]
user: tuple[int, str, str] = (33, '홍길동', 'hong')
info: dict[str, str | int] = {"name": "김길동", "age":40} # key:str, value: str|int
chars : set[str] = {'a', 'b', 'c'}

# 상수 표현
# - 상수 : 한번 값이 지정되면 바뀌어서는 안되는 변수
# - 파이썬 관례상 대문자로 작성된 변수는 상수로 취급
MAX_COUNT = 10
# MAX_COUNT = 5 # 재대입 하면 않된다.

from typing import Final
MIN_COUNT: Final[int] = 20
MIN_COUNT = 50 # Final인데 왜 재할당하는지 불평 -> 힌트만 주는것으로 실행시는 무시

print(MAX_COUNT)
