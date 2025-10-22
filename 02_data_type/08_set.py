# set 집합
# - 중복값 허용 X
# - set api에는 집합관련 연산 (합집합, 교집합, 차집합(=여집합?), 대칭차집합)

st = {2,3,2,3,1,2,3,4,3,2} # key값 없음
print(st, type(st)) # {1, 2, 3, 4} <class 'set'>

# list 중복제거
lst = [2,3,2,3,1,2,3,4,3,2]
st2 = set(lst)
print(st2, type(st2))
lst2 = list(st2)
print(lst2, type(lst2)) # 중복제거 [1, 2, 3, 4] <class 'list'>

# tuple 중복제거
tp = (2,3,2,3,1,2,3,4,3,2)
print(set(tp), type(tp))
print(tuple(set(tp)))

# 요소 추가
numbers = {20, 30, 40}
numbers.add(50)
print(numbers)

# 요소 제거
numbers.remove(50) # 삭제할 값 전달
#numbers.remove(100) # KeyError : 100 -> 존재하지 않는 값 삭제 시 오류
numbers.discard(100) # 삭제할 값이 없어도 오류 X (있으면 버리고, 없으면 말고)
print(numbers)

# 반복 순회 가능 (iterable 객체)
for v in numbers:
    print(v)
    
# 모든 요소 제거
numbers.clear()
print(numbers)

# 집합 연산
x = {1,2,3,4,5, 6, 7, 8, 9,10}
y = {1,3,5,7,9,11,13,15,17}

print("합집합: ", x.union(y)) # x 또는 y, 합집합:  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17}
print("교집합: ", x.intersection(y)) # x and y, 교집합:  {1, 3, 5, 7, 9}
print("차집합: ", x.difference(y)) # x - y, 차집합:  {2, 4, 6, 8, 10}
print("대칭차집합: ", x.symmetric_difference(y)) # x - y U y - x ; 합집합 - 교집합:  대칭차집합:  {2, 4, 6, 8, 10, 11, 13, 15, 17}