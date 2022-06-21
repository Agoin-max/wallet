from django.test import TestCase

# Create your tests here.


class Person(object):

    def __init__(self, name, gender, age, **kwargs):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):

    def __init__(self, name, gender, age, school, score, **kwargs):
        self.name = name.upper()
        self.gender = gender.upper()
        self.school = school
        self.score = score
        super(Student, self).__init__(name, gender, age, **kwargs)


if __name__ == '__main__':
    s = Student("Alice", "female", 18, "Middle Schoole", 87)
    print(s.school)
    print(s.name)
    print(s.gender)