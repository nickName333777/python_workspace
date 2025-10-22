# dict
# - dictionary 사전 자료형
# - 하나의 요소(item)를 key-value 형식으로 저장 cf: JS 객체, Java Map 
# - 하나의 dict안에는 key 중복 불가
# - key는 immutable 자료형(int, float, str, tuple)만 가능하다.
# - value는 모든 자료형 가능, 중복 가능
# - 저장된 순서를 기억하지 않는다. (key를 통해 value 조회)

dct = {}
dct = { 
       'a': 10,
       'b': 20, # {'a': 10, 'b': 20} <class 'dict'>
       'a': 30 # {'a': 30, 'b': 20} <class 'dict'> 중복된 key를 작성하면 덮어쓰기 된다
       }

print(dct, type(dct)) # {} <class 'dict'>

# 요소 조회
print(dct['a'], dct['b']) # key값 직접쓰기
key = 'a'
print(dct[key]) # key값을 변수에 담아써도 같다


#print(dct['c']) # KeyError: 'c'
print(dct.get('a')) # 30
print(dct.get('c')) # None -> 존재하지 않는 key값 조회 시 기본값(None) 처리
print(dct.get('c', '값 없음')) # None -> 존재하지 않는 key값 조회 시 '값 없음'으로 처리

# 요소 추가
dct['c'] = 50
dct.update(d=100) # key=value형식으로 작성
dct.update({'e': 55, 'f':70})
print(dct)

# 값(value) 제거: 파이선 값없음은 None 타입이므로, 값제거는 None으로 바꿔주는것
dct['f'] = None
print(dct)

# 요소(item) 제거
dct.pop('f')
print(dct)

# dict 내장함수
dct2 = dict(name='홍길동', age=38)
print(dct2)

# key, value로 구성된 tuple을 list로 전달
dct3 = dict([('name', '김철수'), ('age', 33)])
print(dct3)


# dict api
# - https://docs.python.org/ko/3.13/library/stdtypes.html#dict


# dict.keys()
keys = dct3.keys()
print(keys, type(keys)) # dict_keys(['name', 'age']) <class 'dict_keys'>

# dict.values()
values = dct3.values()
print(values, type(values)) # dict_values(['김철수', 33]) <class 'dict_values'>

# dict.items()
items = dct3.items()
print(items, type(items)) # dict_items([('name', '김철수'), ('age', 33)]) <class 'dict_items'>

# dict 반복 순회(iterable)
#for key in dct3.keys():
for key in dct3:
    print(f'{key} = {dct3[key]}')
    
for key in dct3.keys(): # 위와 같은 결과
    print(f'{key} = {dct3[key]}')    

for value in dct3.values(): # 
    print(f'{value}')   
    

for item in dct3.items(): # item은 tuple
    print(item, type(item))    # ('age', 33) <class 'tuple'>
    
    
for key, value in dct3.items(): # 위와 같은 결과 (dct3.items()는 tuple을 generate한다)
    print(item, type(item))    # ('age', 33) <class 'tuple'>
    
# 얕은 복사(shallow copy) : 특정 객체에 대한 참조주소값만 복사
# 깊은 복사(deep copy)    : 특정 객체 내용에 대한 복사
sample = {
    'name' : '기계식 키보드',
    'price': 30000,
    'origin' : 'KR', # python에서는 마지막 항목에 ','써도되고, 않써도 된다.(콤마 선택사항)
}

# 얕은 복사
other = sample
print(id(sample), id(other)) # 같은 아이디(주소)

sample['name'] = '나이스한 키보드'
print(other['name'])

# 같은 객체 여부 검사(is: 얕은 복사가 같은지 검사)
print(sample is other) # True
print(sample is dct3) # False


# 깊은 복사
another = sample.copy()
print(id(sample), id(another)) # 다른 아이디(주소)
print(sample is another) # False

sample['price'] *= 10
print(sample)
print(another) # 다른 price볼수 있다

# 리스트 얕은/깊은 복사
prices = [10000, 20000, 30000]

# 얕은 복사
print(prices)
prices_cp = prices
prices.append(40000)
print(prices_cp)

# 깊은 복사
# prices의 복사본을 만들어서 각각 10% 값 올리기 (원본은 변경되면 않됨!)
prices_cp2 = prices.copy()
prices_cp2[0] *= 1.1
prices_cp2[1] *= 1.1
prices_cp2[2] *= 1.1
prices_cp2[3] *= 1.1
# for i, price_cp2_i in enumerate(prices_cp2):
#     # price_cp2[i] = price_cp_i *1.1 # ok
#     prices_cp2[i] *= 1.1
    
print(prices)
print(prices_cp2)


