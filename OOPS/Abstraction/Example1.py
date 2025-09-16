from abc import ABC, abstractmethod

class device(ABC):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    @abstractmethod
    def specs(self):
        pass
class laptop(device):
    def __init__(self,brand,model,ram,processor):
        super().__init__(brand,model)
        self.ram = ram
        self.processor = processor
    def specs(self):
        print("Laptop specs")
        print(f"Brand: {self.brand}, Model: {self.model}")
        print(f"RAM: {self.ram}, Processor: {self.processor}")

l1=laptop("Dell", "Inspiron", "16GB", "Intel i7")
l1.specs()