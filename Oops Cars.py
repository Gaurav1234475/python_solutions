class Car:

    def Set_Car(self, model, year, make):
        self.__model = model
        self.__year = year
        self.__make = make

    def Display_Car(self):
        print("Model\t:", self.__model)
        print("year\t:", self.__year)
        print("Make\t:", self.__make)

    #Create the employee objects
cr = Car()
cr.Set_Car('Safari', 2022, "TATA")
cr.Display_Car()
