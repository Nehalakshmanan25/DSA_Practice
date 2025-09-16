class employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    
    def set_salary(self,amount):
        if amount > 0 :
            print(f"Set salary: {amount}")
            self.__salary = amount
        else:
            print("Invalid salary amount")
            
    def get_salary(self):
        print (f"Salary now: {self.__salary}")
        
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")
        
e1 = employee("Neha", 5000)
e1.set_salary(-90000)
e1.set_salary(40000)
e1.get_salary()
e1.display_info()
