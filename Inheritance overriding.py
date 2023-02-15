# Defining parent class
class Teacher():
      
    # Constructor
    def __init__(self):
        self.value = "Im Parent class"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Student(Teacher):
      
    # Constructor
    def __init__(self):
        self.value = "Im child class"
          
    # Child's show method
    def show(self):
        print(self.value)
          
obj1 = Teacher()
obj2 = Student()
  
obj1.show()
obj2.show()