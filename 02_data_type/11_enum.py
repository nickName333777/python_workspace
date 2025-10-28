# enum   (cf: JPA에서 나왔던 개념)
# - 상수 모음클래스
# - Enum의 자식클래스로 생성

from enum import Enum

class Gender(Enum): # Enum상속
    # 클래스 속성으로 name=value형식으로 지정
    M = '남' # Gender.M
    F = '여'

class Size(Enum):
    S = 0
    M = 1 # Size.M (같은 M이라도, Class이름 다르므로 구분 가능)
    L = 2
    


class Person:
    #def __init__(self, name:str, gender:str) -> None: # return type hint : None
    def __init__(self, name:str, gender:Gender) -> None: # return type hint : None
        self.__name = name
        self.__gender = gender
        
    def __str__(self) -> str: # return type hint : str
        return f'Person(name = {self.__name}, gender = {self.__gender})'
    
    def get_gender(self):
        return self.__gender

#hong = Person("홍길동", "M")
hong = Person("홍길동", Gender.M)
#sinsa = Person("신사임당", "F")
sinsa = Person("신사임당", Gender.F)
#sinsa = Person("신사임당", Gender.T) # Gender에 없는값 입력은 오류발생: AttributeError: type object 'Gender' has no attribute 'T'
print(hong)
print(sinsa)


print(Gender.M, type(Gender.M)) # Gender.M <enum 'Gender'>  ### => M, F는 키값으로 봐라.
print(Gender.F, type(Gender.F)) # Gender.F <enum 'Gender'>

# name/value 속성
print(Gender.M.name, type(Gender.M.name)) # M <class 'str'>
print(Gender.F.value, type(Gender.F.value)) # 여 <class 'str'>

# enum값 비교
print(hong.get_gender()) # Gender.M (클래스명.속성명)
print(hong.get_gender() == Gender.M) # True
print(hong.get_gender() == "M") # False
print(hong.get_gender().name == "M") # True
print(hong.get_gender().value == "남") # True

# 순회
for gender in Gender:
    print(gender) # Gender.M, Gender.F
    
    
# while True:
#     g = input(f"성별을 입력하세요. 1. {Gender.M.value} 2.{Gender.F.value}")
#     print(g)


#######################################
# 문자열 -> enum으로 변환하기
print("#"*40)
gender_input = 'M' # 문자열
gender = Gender[gender_input] # enum
print(gender) # Gender.M
print( "$$$", Gender[gender_input].value)


# # 사용자입력으로부터 Person 객체 생성하기
# name = input("이름 : ")
# gender_input = input("성별 (M/F) : ") # 만약 사용자가 'T'입력하면
# gender = Gender[gender_input] # 사용자 입력을 enum에 넣어 enum에 있는 형식인지 검사 (M/F가 아닌것 넣으면 오류발생: KeyError: 'T' )
# person = Person(name, gender)
# print(person) # Person(name = 김, gender = Gender.M)

# enum 각 속성별로 가져오기
# __members__ : Enum클래스가 가진 모든 멤버를 "멤버 객체"로 담아준다.
print(Gender.__members__) # {'M': <Gender.M: '남'>, 'F': <Gender.F: '여'>}
# dictionary 객체에 담기
print(Gender.__members__.keys()) # dict_keys(['M', 'F'])
print(Gender.__members__.values()) # dict_values([<Gender.M: '남'>, <Gender.F: '여'>])
print(Gender.__members__.items()) # dict_items([('M', <Gender.M: '남'>), ('F', <Gender.F: '여'>)])

