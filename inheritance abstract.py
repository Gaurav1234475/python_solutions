from abc import ABC
class ClassName(ABC):

    class Mobiles(ABC): 
        def RAM(self): 
            pass

    class Redmi(Mobiles): 
        def RAM(self): 
            print("The RAM is 2GB") 
    class Realme(Mobiles): 
        def RAM(self): 
            print("The RAM is 4GB") 
    class OnePlus(Mobiles): 
         def RAM(self): 
            print("The RAM is 6GB") 
    class Ipohones(Mobiles): 
           def RAM(self): 
                print("The RAM is 8GB") 

    t= Redmi() 
    t.RAM() 
    r = Realme() 
    r.RAM() 
    s = OnePlus() 
    s.RAM() 
    d = Ipohones() 
    d.RAM()