# Chapter 01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드
# 코드를 모듈화하여 만들 수 있음 > 패키지로 발전함

# 기본 인스턴스 메소드
class Student(object):
    '''
    Student Class
    Author : kim
    Date : 2020.05.21
    Description : Class, Static, Instance Method
    '''
    # 등록금인상률 - 전역 적용되는 class 변수
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method - 각각의 인스턴스를 구분할 수 있는 고유한 값
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    def get_fee(self):
        return 'Before Tuition -> Id : {}, Tuition : {}'.format(self._id, self._tuition)

    def get_fee_calc(self):
        return 'After Tuition -> Id : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)
    
    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email : {}'.format(self.full_name(), self._grade, self._email)


    # Class Method
    @classmethod
    def raise_fee(cls, percent):
        if percent <= 1:
            print("Please Enter 1 or More")
            return
        cls.tuition_per = percent # cls == Student
        print("Succeed! Tuition increased!")
    
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst._last_name)
        return 'Sorry. {} is not a scholarshp receipient.'.format(inst.full_name())

# 학생 인스턴스
student_1 = Student(1, 'Kim', 'Sarang', 'test@test.com', 1, 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student@nest.com', 2, 500, 4.3)

# 기본정보
print(student_1)
print(student_2)

# 전체정보
print(student_1.detail_info())
print(student_2.detail_info())

# 학비 정보 (인상전)
print(student_1.get_fee())
print(student_2.get_fee())

# 학비 인상(클래스 메소드 미사용) : 직접 접근 NOT GOOD!
# Student.tuition_per = 1.2

# 학비 정보 (인상후)
print(student_1.get_fee_calc())
print(student_2.get_fee_calc())

# classmethod로 인상률 변경
Student.raise_fee(1.3)

print(student_1.get_fee_calc())
print(student_2.get_fee_calc())

# 클래스 메소드를 활용한(line 51) 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'gmail@student.com', 3, 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghan', 'line@student.com', 4, 600, 4.1)

# 학생 정보
print(student_3.detail_info())
print(student_4.detail_info())

# 학비가 올랐는지 확인, 53행으로 인해 인상된 가격 적용
print(student_3._tuition)
print(student_4._tuition) 


# Static Method
# 장학금 혜택 여부 (static method 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst._last_name)
    return 'Sorry. {} is not a scholarshp receipient.'.format(inst.full_name())

# is_scholarship 함수가 종속된 class가 없음
print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

# 장학금 혜택 여부 (static method 사용)
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

# 상속으로 이것도 됨
print(student_1.is_scholarship_st(student_4))