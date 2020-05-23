# Chapter03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형을 저장 [list, tuple, collections.deque]
# 플랫(Flat) : 한개의 자료형만을 저장 [str, bytes, bytearray, array.array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending lists)

# Non Comprehending Lists - ord() 문자의 아스키코드 값을 반환하는 함수
chars = '!@#$%^&*()~_+'
codes1 = []
for s in chars:
    codes1.append(ord(s))
print('EX1-1', codes1)

# Comprehending Lists - Non Comprehending에 비해 속도가 빠름
codes2 = [ord(s) for s in chars]
print('EX1-2', codes2)

# Comprehengind Lists - 조건문 조합
codes3 = []
codes3 = [ord(s) for s in chars if ord(s) > 40]
print('EX1-3', codes3)

# Comprehending Lists - lambda 조합
codes4 = list(filter(lambda x : x > 40, (map(ord, chars))))
print('EX1-4', codes4)

# Comprehending Lists - unicode를 문자로 반환
print('EX1-5', [chr(s) for s in codes1])
print('EX1-6', [chr(s) for s in codes2])
print('EX1-7', [chr(s) for s in codes3])
print('EX1-8', [chr(s) for s in codes4])

# Generator : 한번에 한개의 항목 생성(메모리 저장하지 않고 필요한 만큼만 끌어옴), 성능에 좋음
import array

# Array
array_g = array.array('I', (ord(s) for s in chars))

tuple_g = (ord(s) for s in chars) # 식만 생성하고 값은 반환하지 않음 (EX2-1)
print('EX2-1', tuple_g) 
print('EX2-2', next(tuple_g))
print('EX2-3', next(tuple_g))
print('EX2-4', array_g.tolist())

print()

# Generator 예제
print('EX3-1', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('EX3-2', s)

print()

# 리스트 주의할 점
marks1 = [['~'] * 3 for n in range(3)] # 연산이 3번 반복 (id값이 다름)
marks2 = [['~'] * 3] * 3 # 결과가 3번 반복 (id값이 일치)

print('EX4-1', marks1)
print('EX4-2', marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print('EX4-3', marks1)
print('EX4-4', marks2)

# 증명 - id값 출력
print('EX4-5', [id(i) for i in marks1])
print('EX4-6', [id(i) for i in marks2])

# Tuple Advanced

# Packing & Unpacking - 보따리를 싸서 넘김, 보따리를 풀어서 보여줌
# *args - 값을 묶어서 반환
print('EX5-1', divmod(100, 9))
print('EX5-2', divmod(*(100, 9)))
print('EX5-3', *(divmod(100, 9)))

print()

x, y , *rest = range(10)
print('EX5-4', x, y ,rest)

x, y , *rest = range(2)
print('EX5-5', x, y, rest)

x, y , *rest = 1, 2, 3, 4, 5
print('EX5-6', x, y, rest)

print()

# Mutable(가변) vs Immutable(불변)
t = (10, 15, 20)
l = [10, 15, 20]

print('EX6-1', t, l, id(t), id(t))

t = t * 2
l = l * 2
print('EX6-2', t, l, id(t), id(l)) # 튜플 - 값이 변경되지 않고 append 됨, 리스트 - 값 * 2로 바뀜

t *= 2
l *= 2

print('EX6-3', t, l, id(t), id(l)) # 튜플 - id가 바뀌면서 새로운 객체 생성, 리스트 - id 바뀜