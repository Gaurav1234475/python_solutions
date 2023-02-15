class Employee:

    def Set_Employee(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def Display_Employee(self):
        print("Name\t:", self.__name)
        print("Age\t:", self.__age)
        print("Salary\t:", self.__salary)

    #Create the employee objects
emp = Employee()
emp.Set_Employee('gaurav', 26, 15000)
emp.Display_Employee()
