# Section07-2 
# 파이썬 클래스 상세 이해
# 상속, 다중 상속

# 예제 1
# 상속 기본
# 슈퍼 클래스(부모) 및 서브 클래스(자식) -> 모든 속성, 메소드를 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 클래스의 속성으로 지정

class car:
  """Parent Class"""
  def __init__(self, type, color):
    self.type = type
    self.color = color

  def show(self):
    return 'Car Class "Show Method!"'

class BmwCar(car):
  """Sub Class"""
  def __init__(self, car_name, type, color):
    super().__init__(type, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name : %s" % self.car_name

class BenzCar(car):
  """Sub Class"""
  def __init__(self, car_name, type, color):
    super().__init__(type, color)
    self.car_name = car_name

  def show_model(self) -> None:
    return "Your Car Name : %s" % self.car_name

  def show(self):
    print(super().show())
    return "Car Info : %s %s %s" % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # sub
print(model1.show()) # Super
print(model1.show_model()) # sub
print(model1.__dict__)

# Method Overriding(오버라이딩) - 부모와 자식에 같은 메소드가 선언된다면 자식의 메소드가 우선함
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

# Parent Method Call - 부모의 메소드 끌어오기
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info - 상속 구조 리스트 타입으로 반환 .mro
print(BmwCar.mro())
print(BenzCar.mro())

# 예제 2
# 다중 상속 - 복잡한 다중 상속은 코드 분석이 어려워짐 (2depth 이하 권장)
class X():
  pass

class Y():
  pass

class Z():
  pass

class A(X, Y):
  pass

class B(Y, Z):
  pass

class M(B, A, Z):
  pass

print(M.mro())