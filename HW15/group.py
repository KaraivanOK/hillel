class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def student_info(self):
        studentinfo = '{:<20} {}  {}'.format(self.name, self.age,
                                             self.grades)
        return studentinfo

    def name_grades(self):
        namegrades = '{:<20} {}'.format(self.name, self.grades)
        return namegrades

    def name_age(self):
        nameage = '{:<20} {}'.format(self.name, self.age)
        return nameage


class Group:
    def __init__(self, name):
        self.name = name
        self.memlist = []

    def addmember(self, name):
        self.memlist.append(name)

    def getinfo(self):
        for i in range(len(self.memlist)):
            info = self.memlist[i].student_info()
            print(info)
        return ""

    def n_g(self):
        for i in range(len(self.memlist)):
            ng = self.memlist[i].name_grades()
            print(ng)
        return ""

    def n_a(self):
        for i in range(len(self.memlist)):
            na = self.memlist[i].name_age()
            print(na)
        return ''


student1 = Student('Андрей Говорухи', 20, 10)
student2 = Student('Василий Петров', 22, 8)
student3 = Student('Гавриил Варфаломеев', 18, 7)

group = Group("My_Group")

group.addmember(student1)
group.addmember(student2)
group.addmember(student3)

print('Полная информация о группе:')
print('{:<20} {} {}'.format('Name', 'Age', 'Grades'))
print(group.getinfo())
print('Имена студентов группы и их оценки:')
print('{:<20} {}'.format('Name', 'Grades'))
print(group.n_g())
print('Имена студентов группы и их возраст:')
print('{:<20} {}'.format('Name', 'Age'))
print(group.n_a())
