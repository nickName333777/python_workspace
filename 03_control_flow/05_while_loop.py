# while 반복문
# - 조건식에 따라 반복 횟수가 정해지는 반복문
# - 조건식이 True면 실행, False면 실행 중지

# # 1 ~ 10까지 출력
# i = 1
# while i <= 5: # 조건식
#     print(i)
#     i += 1 # 증감식
    
# # 무한 반복 케이스
# i = 1
# while True:
#     print(i)
    
#     i += 1
#     # 반복문에서 break실행 시, 해당 반복문 즉시 종료(위와 같다)
#     if i > 5: 
#         break
    
    
# 점심 메뉴 주문(while이용)
menu = """
==========
점심 메뉴
==========
1. 쌀국수
2. 비빔밥
3. 삼겹살
0. 종료
==========
선택: 
"""

# #menu = ["쌀국수", "비빔밥", "삼겹살"]
# menu_dct = {"1": "쌀국수", "2": "비빔밥", "3":"삼겹살", "0": "종료"}
# order : list = [] 
# while True:  # 손님이 얼마나 주문할지 모르므로 끝을 모르는 무한 반복문
#     #choice = input(menu)
#     choice = input("메뉴선택: ")
    
#     print("$$$", order)
#     if choice == "0":
#         print(f"주문하신 메뉴는: {order}입니다.")
#         break
        
#     #order += menu[int(choice)-1]
#     #order.extend("".join(menu[int(choice)-1]))
#     if len(order) == 0:
#         #order = menu_dct[choice] # NG;; # NOK ==> $$$ 쌀국수비빔밥
#         order.append(menu_dct[choice]) # ok ==> $$$ ['쌀국수', '비빔밥']
#         #order.extend(menu_dct[choice]) # NOK==>  $$$ ['쌀', '국', '수', '비', '빔', '밥']
#     else:
#         #order += menu_dct[choice] # NG  # NOK 
#         order.append(menu_dct[choice]) # ok
#         #order.extend(menu_dct[choice]) # NOK
    
###### python idiosyncrasy: "문자열"을 빈 리스트에 추가할때는 주의!! ==> .append()가 제일 safe
# >>> ll=[]; ll += "abc"; ll
# ['a', 'b', 'c']
# >>> ll=[]; ll.append("abc"); ll
# ['abc']
# >>> ll=[]; ll.extend("abc"); ll
# ['a', 'b', 'c']
######    
    

# order : list = [] 
# while True:  # 손님이 얼마나 주문할지 모르므로 끝을 모르는 무한 반복문
#     #choice = input(menu)
#     choice = input("메뉴선택: ")
#     match choice:
#         case "1":
#             order.append("쌀국수")
#         case "2":
#             order.append("비빔밥")
#         case "3":
#             order.append("삼겹살") 
#         case '0':
#             break # 중지 주문
#         case _:
#             print("잘못입력하셨습니다.")   
            
#     #print(f"주문한 메뉴: {order}")
# print(f"주문한 메뉴: {order}")    


# Comprehension (=내포)
# - 한줄짜리 반복문을 통해 쉽게 list, dict를 생성하는 방법
# - list comprehension
# - dict comprehension

# lst = [1,2,3,4,5,6,7,8,9,10]
def test1():
    lst:list = []
    for n in range(1, 11):
        lst.append(n)
    return lst

#print(test1())


def test2():
    """list 내포"""
    return [n for n in range(1, 11)]

#print(test2())

def test3():
    """ 1~100 사이 짝수만 리스트 내포로 생성 """
    # lst : list = []
    # for n in range(1, 101):
    #     if n%2 == 0:
    #         lst.append(n)
            
    # return lst
    return [n for n in range(1, 101) if n%2==0] # 조건이 있는 경우

#print(test3())


def test4(lst: list[object]):
    """ 전달된 list객체에서 "정수"만 필터링해서 다시 리스트로 반환"""
    return [n for n in lst if isinstance(n, int)]
    # isinstance(객체, int) -> bool값 (True or False)
    
# print(test4([1, "열두시", 123.456, 27, 0.022, '🍟']))
# print(isinstance(1, int)) # True
# print(isinstance('🍟', int)) # False

# 중첩반복문
def test5():
    # lst : list[tuple[int, int]] = []
    # for row in range(0, 3) : # 0 1 2
    #     for col in range(0, 5): # 0 1 2 3 4
    #         lst.append((row, col))
            
    # return lst
    return [(row, col) for row in range(0, 3) for col in range(0, 5)]

# print(test5())


# dict 내포
def test6():
    """dct = {1:1, 2:4, 3:9, 4:16, 5:25}"""
    #return { f'{k}':k**2 for k in range(1, 6) }
    return { k:k**2 for k in range(1, 6) }

# print(test6())

def test7(lst : list[str]):
    """ 주어진 문자열 리스트에 대해서 key(문자열) : value (문자열의 길이)로 구성된 dict반환 & 문자열 길이가 3 이상 """
    return { k:len(k) for k in lst if len(k) >= 3 }

#print(test7(['abc', 'de', "fffffff"]))
#print(test7(['hello', 'hi', "friday"]))


# list -> dict 변환
#def test8(lst1 : list[str], lst2 : list[str]):
def test8():
    """ {'홍길동': 22, '철수' : 31, '영희': 45} """
    names: list[str] = ['홍길동', '철수', '영희']
    ages : list[int] = [22, 31, 45]
    #return { name:age for name, age in zip(names, ages)}
    return dict(zip(names, ages)) # dict()함수 이용

print(test8())


# dict -> list(tuple)로 변환
def test9():
    info: dict[str, int] = {'홍길동': 22, '철수' : 31, '영희': 45}
    print(info.items())
    print(*info.items()) # * : list unpacking 연산자 ==> tuple들로만 따로, 따로 나옴: ('홍길동', 22) ('철수', 31) ('영희', 45)
    # list unpacking -> zip ('홍길동', 22) ('철수', 31) ('영희', 45)
    
    names, ages = zip(*info.items())
    # -> zip(('홍길동', 22),
    #         ('철수', 31),
    #         ('영희', 45),
    # )
    
    return names, ages
    

print(test9()) # (('홍길동', '철수', '영희') (22, 31, 45))
print(*test9()) # ('홍길동', '철수', '영희') (22, 31, 45)