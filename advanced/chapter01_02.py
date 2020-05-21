# Chapter 01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재선언
class Student():
    """
    Student Class
    Author : Daniel Kim
    Date : 2020.05.21
    """

    # 클래스 변수
    student_count = 0

    # (self) 포함 > 인스턴스 변수
    def __init__(self, name, number, grade, details, email=None):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)
    
    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1

# self의 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
studt2 = Student('Jang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'test@test.com')

# id 위치(레이블)을 비교
print(id(studt1) == id(studt2))
print(studt1 is studt2)

# 인스턴스의 값을 비교
print(studt1 == studt2)
print(studt1._name == studt2._name)


# attribute 확인 : dir(자세한 정보) & __dict__
print(dir(studt1)) # dir : Class 안에서 사용할 수 있는 속성(attribute) 모두 조회
print(dir(studt2))
print()
print(studt1.__dict__) # __dict__ , 인스턴스에 사용된 속성과 값 모두 조회
print(studt2.__dict__)

# 매개변수(parameter) : 속성(attribute)에 선택적으로 부여할 수 있는 옵션값
# email=None

# Docstring :  클래스의 주석 정보 확인
print(Student.__doc__) 
print()

# 실행
studt1.detail_info()
studt2.detail_info()

# 결론
# 클래스는 인스턴스를 정의하기 위한 붕어빵 틀
# 인스턴스의 속성을 클래스 안에서 선언할 때 관리가 용이함

# 에러
# Student.detail_info() 호출해야하는 인스턴스가 없기 때문에 호출할 값이 없어 에러
Student.detail_info(studt1)
Student.detail_info(studt2)

# 인스턴스의 원형 클래스(붕어빵틀)의 정보 확인
print(studt1.__class__, studt2.__class__)
print(studt1.__class__ == studt2.__class__)
print(id(studt1.__class__) == id(studt2.__class__))
# 같은 클래스에 종속되기때문에 class 정보가 일치

# 인스턴스 변수에 대한 직접 접근(PEP)을 권장하지 않음
studt1._name = 'HAHAHA'
print(studt1._name)

# 클래스 변수 > 클래스에 종속된 모든 인스턴스에서 적용됨 (상속)
print(studt1.student_count)
print(studt2.student_count)
print(Student.student_count)

# 클래스 변수가 공유되는지 확인
print(Student.__dict__) 
print(studt1.__dict__) 

# 인스턴스 > 상위 클래스 > 부모 클래스 순으로 변수 검색(아래 > 위) // 같은 이름으로도 변수 생성 가능

# __del__ 변수는 잘 안씀
del studt2

print(studt1.student_count) # 1
print(Student.student_count) # 1