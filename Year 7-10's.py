import csv# Import the end of term year 9's marks
import math
import openpyx1

def get_file_input():
    file_path = input("Please enter your excel file: ")
    
    try:
        workbook = openpyx1.load_workbook(file_path)
        sheet = workbook.activate
        
        sheet.cell(row=row, column =10, value=calculate_gpa())

        
        workbook.save("Updated_" + file_path)
class Student:
    def __init__(self,studentcode,studentname,englishmarks,hassmarks,mathmarks,sciencemarks,englishmarks2,hassmarks2,mathsmarks2,sciencemarks2):
        self.studentcode = studentcode
        self.studentname = studentname
        self.englishmarks = int(englishmarks)
        self.hassmarks = int(hassmarks)
        self.mathmarks = int(mathmarks)
        self.sciencemarks = int(sciencemarks)
        self.englishmarks2 = int(englishmarks2)
        self.hassmarks2 = int(hassmarks2)
        self.mathsmarks2 = int(mathsmarks2)
        self.sciencemarks2 = int(sciencemarks2)
        
        
    def calculate_gpa(self):
        """Calculate the gpa of every student."""
        gpa = (self.englishmarks + self.hassmarks + self.mathmarks + self.sciencemarks + self.englishmarks2 + self.hassmarks2 + self.mathsmarks2 + self.sciencemarks2)/4
        return round(gpa)
        
students = []

filename = 
with open(mode = 'r') as file:
    csv_reader = csv.reader(file)
    index = 0
    
    for row in csv_reader:
        index = index + 1
        print(row)
        if index ==1 or index == 2 or index == 3 or index == 4:
            continue
        for i in range(2,10):
            if row[i] == "":
                row[i] = 0
        
            
        student = Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
        students.append(student)
            
        if index == 50:
            break       
storing_gpa = []

print("number of students", len(students))
for student in students:
    all_names.append(student.studentname)
    current_gpa = student.calculate_gpa()
    storing_gpa.append(current_gpa)









    
    

 
