# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator


    @property # getter : v.x 로 __x 변수에 접근 가능
    def x(self):
        print('Called Property x')
        return self.__x

    @x.setter # setter, getter 선언이 선행
    def x(self, v):
        print('Called Property x setter')
        self.__x = float(v)

    @property 
    def y(self):
        print('Called Property y')
        return self.__y

    @y.setter 
    def y(self, v):
        print('Called Property y setter')
        if v < 30:
            raise ValueError('30 below is not possible')
        self.__y = float(v)


# private : __변수는 접근 제한됨, 함수 선언 후 생성자에 초기화된 인자를 보호하기 위함 
# getter(read), setter(write)

# 객체 선언
v = VectorP(20, 20)
# print('EX1-1', v._x, v._y)

# getter, setter로 변수 변경
v.y = 44

# Getter, Setter
print('EX1-2', dir(v), v.__dict__)
print('EX1-3', v.x, v.y)

# Iter 확인
for val in v:
    print('EX1-4', val)

# __slot__
# 파이썬 인터프리터에게 홍보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 메모리 사용 공간 대폭 감소 (대략 20%)
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용

class TestA(object):
    __slots__ = ('a')

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('EX2-1', use_slot)
# print('EX2-2', use_slot.__dict__)
print('EX2-3', no_slot)
print('EX2-4', no_slot.__dict__)

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj): # closure
    def repeat_inner():
        obj.a = "TEST"
        del obj.a
    return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number = 500000))) 
print(min(timeit.repeat(repeat_outer(no_slot), number = 500000)))

print()

# 객체 슬라이싱
class Objects:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]
    def __len__(self):
        return len(self._numbers)
    def __getitem__(self, idx):
        return self._numbers[idx]

s = Objects()

print('EX3-1', s.__dict__)
