class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student(person):
    def __init__(self,name,age,student_id,course):
        super().__init__(name,age)
        self.student_id = student_id
        self.course = course
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Student ID: {self.student_id}, Course: {self.course}")
class professor(person):
    def __init__(self,name,age,emp_id,dept):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.dept = dept
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Emp_ID: {self.emp_id}, Dept: {self.dept}")
 
people = [
    student("Neha", 22, 3116, "CSE"),
    professor("Shreya", 35, 9909, "CSE")
]

for Person in people:
    Person.display_info() 
    print("---")