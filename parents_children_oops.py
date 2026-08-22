class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_student(self):
        print("Name:", self.name)
        print("Roll NO:", self.roll_no)
    
class Result(Student):
    def __init__(self, name, roll_no, marks):
            super().__init__(name,roll_no)
            self.marks = marks
        
    def display_result(self):
         self.display_student()
         print("Marks:", self.marks)
    

student = Result("Amelia", 101,87)
student.display_result()