# Comprehension 내포 [ FEAT. KSY ]
# - 한줄짜리 반복문을 통해 쉽게 list, dict를 생성하는 방법
# - list comprehension
# - dict comprehension

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def test1():
    lst:list = []
    for n in range(1,11) :
        lst.append(n)
    return lst

# print(test1())

def test2():
    """list 내포"""
    return [n + 2 for n in range(1, 11)]

# print(test2())

def test3():
    """1~100 사이 짝수만 리스트 내포로 생성"""
    # lst : list = []
    # for n in range(1,101):
    #     if n % 2 == 0:
    #         lst.append(n)
    # return lst
    
    return [n for n in range(1, 101) if n % 2 == 0]
# print(test3())

def test4(lst : list[object]):
    """전달된 list 객체에서 정수만 필터링 해서 다시 리스트로 반환"""
    return [n for n in lst if isinstance(n, int) ]
    # isinstance(객체, int) -> bool
    
print(test4([1, '열두시', 123.456, 27, 0.012, '🍟']))
print(isinstance(1, int)) #True
print(isinstance('🍟', int)) #False

# 중첩반복문
def test5():
    # lst : list[tuple[int, int]] = []
    # for row in range(0,3) : # 0 1 2
    #     for col in range(0, 5) : # 0 1 2 3 4
    #         lst.append((row, col))
    # return lst
    return [(row, col) for row in range(0,3) for col in range(0,5) ]
print(test5())

# dict 내포
def test6():
    """dct = {1:1, 2:4, 3:9, 4:16, 5:25}"""
    return {k:k ** 2 for k in range(1, 6) }
print(test6())

def test7(lst: list[str]):
    """주어진 무자열 리스트에 대해서 key(문자열) : value(문자열의 길이)로 구성된 dict 반환"""
    return { str : len(str) for str in lst if len(str) >= 3}
print(test7(['hello', 'hi', 'friday']))

# list -> dict 변환
def test8():
    """{'홍길동' : 22, '철수' : 31, '영희' : 45}"""
    names: list[str] = ['홍길동', '철수', '영희']
    ages : list[int] = [22, 31, 45]
    # return {name : age for name, age in zip(names, ages)}
    return dict(zip(names, ages))
# print(test8())

# dict -> list(tuple)로 변환
def test9():
    info : dict[str,int] = {'홍길동': 22, '철수': 31, '영희': 45}
    print(info.items())
    print(zip(*info.items()))
    # list unpacking
    # -> zip(('홍길동', 22),
    #        ('철수', 31),
    #        ('영희', 45))
    
    names, ages = zip(*info.items())
    return names, ages
print(test9())