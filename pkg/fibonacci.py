# 피보나치 수열 클래스 패키지
class Fibonacci:
  def __init__(self, title = "Fibonacci"):
    self.title = title

  def fib(self):
    a, b = 0, 1
    while a < self:
      print(a, end=' ')
      a, b = b, a+b
    print()
    
  def fib2(self):
    result = []
    a, b = 0, 1
    while a < self:
      result.append(a)
      a, b = b, a+b
    return result
    
