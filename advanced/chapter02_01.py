# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Function), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체는 id로, type -> value
# 파이썬 -> 일관성
# 튜플은 불변이므로 리스트보다 속도가 빠름

# 일반적인 튜플 사용
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_len1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)
print('EX1-1', line_len1)

# 네임드 튜플 사용 (튜플 + 클래스)
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_len2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)
print('EX1-2', line_len2)
print('EX1-3', line_len1 == line_len2)

# 네임드튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename = True) # Default = False

# Dict to unpacking
temp_dict = {'x' : 75, 'y' : 55}

# 출력
print('EX2-1', Point1, Point2, Point3, Point4)

# 객체 생성
p1 = Point1(x = 10, y =35)
p2 = Point2(20, 40)
p3 = Point3(45, y = 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) # ** -> temp_dict 의 모든 인자를 가져옴

print('EX2-2', p1, p2, p3, p4, p5)

print()

# 사용
print('EX3-1', p1[0] + p2[1]) # Index Error 주의
print('EX3-1', p1.x + p2.y)  # 클래스 변수 접근 방식

# Unpacking
x, y = p3
print('EX3-3', x + y)

# Rename 테스트
print('EX3-4', p4)

print()

# namedtuple 메소드
temp = [52, 38]

# ._make() : 새로운 객체 생성
p4 = Point1._make(temp)
print('EX4-1', p4)

# ._fields : 필드 네임 확인
print('EX4-2', p1._fields, p2._fields, p3._fields)

# ._asdict() : OrderedDict 반환
print('EX4-3', p1._asdict(), p2._asdict(), p3._asdict())

# ._replace() : 수정된 새로운 객체 반환, 튜플은 불변이므로 id값이 바뀜
print('EX4-4', p2._replace(y = 100))

print()

# 사용 실습
# 학생 전체 그룹
# 반 20명, 4개의 반(A, B, C, D), 번호

# 네임드튜플
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# 리스트 컴프리헨션
# numbers2 = []
# for n in range(1, 21):
#     numbers2.append(str(n))

# List Comprehension               <-               <- 
students = [Classes(rank, number) for rank in ranks for number in numbers]
print('EX5-1', students)
print('EX5-2', len(students))
print('EX5-2', students[4])
print('EX5-2', students[4].rank)

# 가독성이 안좋은 케이스
students2 = [Classes(rank, number)                      # ^
                    for rank in 'A B C D'.split()       # ^
                        for number in [str(n)           # ^    
                            for n in range(1, 21)]]     # ^

print('EX6-1', len(students2))
print('EX6-2', students2)

print()

# 출력
for s in students:
    print('EX7-1', s)