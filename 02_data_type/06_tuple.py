# tuple
# - 변경 불가한 (immutable) list
# 저장 순서 기억

t1 = () # 빈 tuple
t2= (10) # 그냥 10과 동일 
t3= (10,) # , 필수 10 <class 'tuple'>
t4 =(10, 15)
t5 = 10, 15

print(t1, type(t1)) # () <class 'tuple'>
print(t2, type(t3)) # () <class 'tuple'>
print(t3, type(t3)) # () <class 'tuple'>
print(t4, type(t4)) # () <class 'tuple'>
print(t5, type(t5)) # () <class 'tuple'>


# Tuple: 일기전용(쓰기불가)
# -indexing
# -slicing

tp1 = ('a', 'b', 'c', 'd', 'e')
print(tp1[0], tp1[1], tp1[2], tp1[3]) # a b c d
#print(tp1[50]) # IndexError: tuple index out of range
print(tp1[:3]) # ('a', 'b', 'c')

#tp1[0] = 'e' # TypeError: 'tuple' object does not support item assignment
#tp2 = 'e', tp1[1], tp1[2], tp1[3] # ('e', 'b', 'c', 'd')
#tp2 = 'e', tp1[1:] # ('e', ('b', 'c', 'd', 'e'))
tp2 = 'e', *tp1[1:] # unpacking 연산자 ('e', 'b', 'c', 'd', 'e')


print(tp2)

# tuple 활용
# - 복수개의 값을 변수에 할당
# a = 100
# b = 200
a, b = 100, 200
print(a, b)

# - 값 교환
x, y = 33, 55
print(f'x={x}, y={y}')

x, y = y, x
print(f'x={x}, y={y}')