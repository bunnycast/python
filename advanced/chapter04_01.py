# Chapter04-1
# 파이썬 심화
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화 가능
# 2. 변수 등에 할당 가능
# 3. 함수의 인수로 전달 가능
# 4. 함수 결과로 반환 가능 

# 함수 객체 예제

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print('EX1-1', factorial(5))
print('EX1-2', factorial.__doc__)
print('EX1-3', type(factorial), type(A))
print('EX1-4', set(sorted(dir(factorial))) - set(sorted(dir(A)))) # 함수가 클래스에 비교해 가진 특징들
print('EX1-5', factorial.__name__) # 함수 이름 호출
print('EX1-6', factorial.__code__) # 함수 코드 호출
print()

# 함수를 변수로 할당
var_func = factorial
print('EX2-1', var_func) # 할당만 해둠
print('EX2-2', var_func(5))
print('EX2-1', map(var_func, range(1, 6)))
print('EX2-2', list(map(var_func, range(1, 6))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)
print('EX3-1', list(map(var_func, filter(lambda x: x % 2, range(1, 6))))) # filter로 1-6 중 홀수만 실행됨 1, 3, 5
print('EX3-2', [var_func(i) for i in range(1, 6) if i % 2]) # list comprehension

print()

# reduce()
from functools import reduce
from operator import add

print('EX3-3', reduce(add, range(1, 11))) # 값을 누적
print('EX3-3', sum(range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용(for 가독성)
# 일반 함수 형태로 리팩토링 권장

print('EX3-5', reduce(lambda x, t: x + t, range(1, 11)))

print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인

import random

# 로또 추첨 클래스 선언
class lottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]
    
    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])
    
    def __call__(self):
        return self.pick()

# 객체 생성
game = lottoGame()

# 호출 가능 확인
print('EX4-1', callable(str), callable(list), callable(factorial), callable(3.14), callable(game))

# 게임 실행
print('EX4-2', game.pick())
print('EX4-3', game())
print('EX4-4', callable(game))

print()

# 다양한 매개변수 입력(*args, **kwargs)
def args_test(name, *contents, point=None, **attrs):
    return '<args_test -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)

print('EX5-1', args_test('test1'))
print('EX5-2', args_test('test1', 'test2'))
print('EX5-3', args_test('test1', 'test2', 'test3', id = 'admin'))
print('EX5-4', args_test('test1', 'test2', 'test3', id = 'admin', point = 7))
print('EX5-5', args_test('test1', 'test2', 'test3', id = 'admin', point = 7, password = '1234'))

print()

# 함수 Signatures
from inspect import signature
sg = signature(args_test)

print('EX6-1', sg)
print('EX6-2', sg.parameters)

print()

# 모든 정보 출력
for name, param in sg.parameters.items():
    print('EX6-3', name, param.kind, param.default)

# Partial 사용법 : 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된 함수의 새 버전 반환
from operator import mul
from functools import partial

print('EX7-1', mul(10, 100))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6) # mul, 5 가 고정됨

print('EX7-2', five(100))
print('EX7-3', six())
print('EX7-4', [five(i) for i in range(1, 11)])
print('EX7-5', list(map(five, range(1, 11))))
