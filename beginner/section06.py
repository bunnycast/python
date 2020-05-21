# Sectino06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parpameter):
#    code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요 - 함수 정의 먼저, 그 후 선언

# 예제 1
def hello(world):
  print("Hello ", world)

hello("python!")
hello(7777)

# 예제 2
def hello_return(world):
  val = "Hello " + str(world)
  return val

n = hello_return("Python!!!!!")
print(n)

# 예제 3(다중 리턴)
def function_mul(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return y1, y2, y3

val1, val2, val3 = function_mul(100)

print(type(val1), val2, val3)

# 예제 4(데이터 타입 반환)
def function_mul2(x):
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return [y1, y2, y3]

lt = function_mul2(100)
print(lt, type(lt))

# 예제 4
# *args, *kwargs - * 가변함수를 튜플 형태로 반환, ** 가변함수를 딕셔너리 형태로 반환
def args_func(*args):
  for t in args:
    print(t)
  # for i, v in enumerate(args): enumerate > 이터레이트(인덱스를 만들어서 순회) 함수
  #   print(i, v)

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

# kwargs
def kwargs_func(**kwargs):
  # print(kwargs)
  for k, v in kwargs.items():
    print(k, v)

kwargs_func(name1='kim')
kwargs_func(name1='kim', name2='park', name3='lee')

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)

example_mul(10, 20, 'kim', 'park', age1=40, age2=35)

# 예제 5
# 중첩 함수(클로저) - 함수 안에 함수, 변수 선언 줄이고 메모리 관리에 효율적인 방식
def nested_func(num):
  def func_in_func(num):
    print(">>>", num)
  print("in func")
  func_in_func(num + 10000)

nested_func(10000)
# def nested_func(10000) def func_in_func(선언만 됨) > print("in func") > func_finc(10000 + 10000) > def func_in_func(20000) > print(">>>", 20000)

# cf. 파이썬 데코레이터 클로저

# 예제 6 - 힌트, 입력하는 변수의 자료형을 미리 알려줌
def function_mul3(x : int) -> list:
  y1 = x * 100
  y2 = x * 200
  y3 = x * 300
  return [y1, y2, y3]

print(function_mul3(5))

# lambda식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(x : int) -> int:
  return x * 10

var_func = mul_10
print(var_func)

print(var_func(10))

# 람다식 - 데이터 대량 처리에 유익함
lambda_mul = lambda n: n * 10
print(">>", lambda_mul(10))

def func_final(x, y, func):
  print("다아아압~", x * y * func(20))

func_final(10, 10, lambda_mul)

func_final(10, 10, lambda n: n * 1000)