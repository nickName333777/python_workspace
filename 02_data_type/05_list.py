# list  
# - 컨테이너 자료형
# - 여러 literal을 묶어서 관리
# - 저장된 "순서"를 기억
# - 시퀀스형(str, list, tuple)(인텍싱/슬라이싱, 멤버쉽 확인 가능)


lst = [1,2,3]
print(lst, type(lst)) # [1, 2, 3] <class 'list'>

print(lst[0], lst[1], lst[2])

# list는 요소를 추가/삭제 가능한 mutable 자료형이다
print('변경전 : ', id(lst))

# 맨 뒤에 요소 추가
lst.append(4)
print(lst)
print('변경후 : ', id(lst)) # 같은 id. (so, mutable)

#원하는 인덱스에 요소 추가
lst.insert(1, 1.5)
lst.insert(0, 0)
print(lst)

# 값 변경
lst[0] = -1
print(lst)

# 특정 인덱스 값 제거
lst.pop(2)
print(lst)

# 2차원 list
students = [['홍길동', 27], ['김철수', 33, '서울'], ['이영희', 45, '부산']]
print(students)

# 인덱싱
print(students[0])
print(students[0][0])
print(students[1][1])
print(students[1][2])

# csv데이터를 list로 관리
# - Comma Separated Value
data = "홍길동, 20, 서울, 종로구"
data_ = data.split(',')
print(data_, type(data_))  #  ['홍길동', ' 20', ' 서울', ' 종로구'] <class 'list'>

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list 반복 순회 가능(iterable 형)
lst = ['a', 'b', 'c']

# for 변수 in 순회객체
for str in lst:
    print(str)
    
# 인덱스 순회
# enumerate(iterable, start=0) : 반복 가능한 객체에 인덱스를 붙여서 (인덱스, 값) 반환
for index, v in enumerate(lst): 
    print(index, v)
    
# 더하기/곱하기 연산
foods = ['🍔', '🍟']
drinks = ['🍫']
print(foods + drinks) # ['🍔', '🍟', '🍫']

print(foods * 5 )

# list api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#list


# list.sort() - mutable 연산 (in-place)
# sorted()    - immutable 연산 (not-in-place)

fruits = ['orange', 'apple', 'banana', 'kiwi']
#fruits.sort()
fruits.sort(reverse=True) # 역순으로 출력
print(fruits)

numbers = [20, 25, 10, -10]
numbers.sort(reverse=True) # in-places
print(numbers)

# key 정렬 기준 함수
fruits.sort(key=len) # 단순 길이로 정렬
print(fruits) # 우선 길이순, 같은건 알파벳순으로, 알파벳도 같으면 아무거나 우선


# 커스텀 정렬 기준 함수
def my_sort(elem):
    return len(elem), elem # 처음에는 길이정렬, 그다음은 abc정렬

fruits.sort(key=my_sort)
print(fruits)

print('list.sort() 반환값 : ', fruits.sort()) # None(반환값없음 b/c in-place)


# sorted를 이용한 immutable 연산처리
fruits = ['melon', 'banana', 'orange', 'cherry']
fruits1 = sorted(fruits)
print(fruits)
print(fruits1)

# slicing을 통한 값 변겅 (mutable 방식)
texts = ['hello', 'hi', '안녕']
print(texts[:2], type(texts[:2])) # ['hello', 'hi'] <class 'list'>

texts[:2] = ["햄버거", "피자"]
texts[1:3] = ['🥞', '🥨']
print(texts)

# 연결연산결과를 기존 list반영
a= [1,2]
b = [3, 4]
#a = a + b
a += b
print(a, b) # [1, 2, 3, 4] [3, 4]
