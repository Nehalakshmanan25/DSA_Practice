class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(self.brand,self.model,self.year)
        
car1 = Car("magnite","y24",2026)
car1.display_info()
car2 = Car("creta","v45",2027)
car2.display_info()