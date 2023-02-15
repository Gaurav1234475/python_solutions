class College:
    def __init__(self,name,city,grade):
        self.name = name 
        self.city = city
        self.grade = grade
class Student(College):
    def __init__(self,name,year,role_no,percentage):
        self.name = name 
        self.year = year
        self.role_no = role_no
        self.percentage = percentage
    def details(self):
        print("details of Student")
    def info(self):
        self.details()
        print(f"i am {self.name} and im studying in {self.year}year and my role no is {self.role_no} and my percentage are {self.percentage}%")
Single = Student("david",2,24,80)
Single.info()