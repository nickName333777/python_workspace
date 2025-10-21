# 변수 variable : 값을 기록하기 위한 메모리 공간

age = 37 # age라는 변수(공간)에 37(literal)을 대입해라
name = '홍길동'

print(age)
print(name)

# 대입 연산자 '=' :  좌항의 변수에 우항의 값을 대입해라. 무조건 오른쪽에서 왼쪽으로 대입한다.
num = 100
num = 200
print(num)
num = name
print(num) # (왼쪽 파일 Explorer영역을 클릭하고) ctrl+K (누르고)+ ctrl+S 누르면 키바인딩 나타나고, 여기서 ... 을 F11로 바꾼다.
           # Python: Run Python File in dedicated terminal => F11로 키바인딩 해라


"""
변수명 작성요령
1. 대소문자를 구분한다.
2. 변수명은 snake casing을 사용한다. (단어와 단어사이를 _로 연결)
3. 한글 변수명을 지정할 수 있다. (하지만 인코딩 등의 문제를 야기할 수 있으므로 사용을 지양한다.)
4. 언더바(_)를 제외한 특수문자를 사용할 수 없고, 숫자로 시작할 수 없다.
5. 파이썬 예약어(if, elif, else, for, while, …)를 사용할 수 없다.
6. **직관적인 변수명**을 사용한다. 짧고 간편하다고, a, b, c와 같은 변수명을 사용하지 않는다.
"""

# 1.
X = 1
x = 11
print(X, x) # 1 11

# 2.
teamname = '오지라퍼스'
team_name = '오지라퍼스'
print(teamname, team_name)

# 3. 한글쓸수 있지만 인코딩 문제가 생길수 있으므로 한글을 변수명으로 쓰지는 마라
팀명 = '오지라퍼스'
print(팀명)

# 4.
# em@il = user01@og.kr # Error
# 1st_user = '유저일' # Error
_1st_user = '유저일'

#print(em@il)
print(_1st_user)

# 5. 파이썬 예약어(if, elif, else, for, while, ...)를 사용할 수 없다.
import keyword
print(keyword.kwlist)

# break = 'break'
# print(break) # Error


# 6. **직관적인 변수명**을 사용한다.
k = True

