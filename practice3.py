class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    def print_language(self):
        print(self.show)

    @classmethod # 일본어 > English > 일본어
    def class_my_language(cls):
        return cls()
    
    @staticmethod # 일본어 > English, 부모클래스(Language) 의 값을 가져옴
    def static_my_language():
        return Language()



class KoreanLanguage(Language):
    default_language = "일본어"

a = Language.static_my_language()
a.print_language()

b = Language.class_my_language()
b.print_language()