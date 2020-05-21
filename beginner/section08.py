# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

from pkg.fibonacci import Fibonacci

Fibonacci.fib(400)

print("ex2 :", Fibonacci.fib2(400))
print("패키지 타이틀 :", Fibonacci().title)

# 사용2 (클래스) -> * 로 다가져 오는거 메모리를 많이 잡아먹으므로 권장하지 않음
from pkg.fibonacci import *

Fibonacci.fib(1000)

print("ex2 :", Fibonacci.fib2(1000))
print("패키지 타이틀 :", Fibonacci().title)

# 사용3 (클래스) - 이름바꾸기 (alias)
from pkg.fibonacci import Fibonacci as fb

fb.fib(3000)

print("ex2 :", fb.fib2(1000))
print("패키지 타이틀 :", fb().title)

# 사용4 (함수) - alias
import pkg.calculations as c 

print("ex 4-1 : ", c.add(10, 100))
print("ex 4-2 : ", c.multi(10, 100))

# 사용 5 (함수) - 필요한 함수만 가져오기
from pkg.calculations import div as d

print("ex 5 : ", int(d(100, 10)))

# 사용 6 
import pkg.prints as p 
p.prt1()
p.prt2()

# 사용 7 - 파이썬 기본 제공 함수 (builtins) 가져오기 
import builtins
print(dir(builtins))