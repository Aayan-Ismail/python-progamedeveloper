
class Student:
    def __init__(self,name,age,course,marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    
    def display(self):
        print("\nStudent Details")
        print("Name:",self.name)
        print("Age",self.age)
        print("Course",self.course)
        print("Marks",self.marks)

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average Marks:",avg)

student1 = Student("Alexander",16,"Computer Science",[90,85,92])
student2 = Student("Bob",19,"CODING",[75,80,78])

student1.display()
student1.average()

student2.display()
student2.average()

