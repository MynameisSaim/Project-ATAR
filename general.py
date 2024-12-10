import csv# Import the end of term year 9's marks
import openpyx1

def get_file_input():
    file_path = input("Please enter your excel file: ")
    
    try:
        workbook = openpyx1.load_workbook(file_path)
        sheet = workbook.activate
        
        sheet.cell(row=row, column =26, value=calculate_gpa())
        sheet.cell(row=row, column =27, value=count_cs())
        
        workbook.save("Updated_" + file_path)
class Student:
    def __init__(self,studentcode,studentname,eng,tec,csi,wsi,acf,vdt,tec2,app,app2,bme,bsp,cae,che,eng2,hea,vho,hpe,hum,mat,oed,pes,var):
        self.studentcode = int(studentcode)
        self.studentname = studentname
        self.eng = int(eng)
        self.tec = int(tec)
        self.csi = int(csi)
        self.wsi = int(wsi)
        self.acf = int(acf)
        self.vdt = int(vdt)
        self.tec2 = int(tec2)
        self.app = int(app)
        self.app2 = int(app2)
        self.bme = int(bme)
        self.bsp = int(bsp)
        self.cae = int(cae)
        self.che = int(che)
        self.eng2 = int(eng2)
        self.hea = int(hea)
        self.vho = int(vho)
        self.hpe = int(hpe)
        self.hum = int(hum)
        self.mat = int(mat)
        self.oed = int(oed)
        self.pes = int(pes)
        self.var = int(var)
            
    def calculate_gpa(self):
        """Calculate the gpa of every student."""
        gpa = (self.eng + self.tec + self.csi + self.wsi + self.acf + self.vdt + self.tec2 + self.app + self.app2 + self.bme + self.bsp + self.cae + self.che + self.eng2 + self.hea + self.vho + self.hpe + self.hum + self.mat + self.oed + self.pes + self.var)/4
        return round(gpa)
        
students = []

filename = 
with open(mode = 'r') as file:
    csv_reader = csv.reader(file)
    index = 0
    
    for row in csv_reader:
        index = index + 1
        print(row)
        if index ==1 or index == 2 or index == 3:
            continue
        for i in range(2,25):
            if row[i] == "":
                row[i] = 0
        
            
        student = Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24])
        students.append(student)
            
             
storing_gpa = []
all_subject = []
    # Constants 
    C_threshold = 50  # Minimum average score to achieve a "C"  

for student in students:
storing_gpa = calculate_gpa()
all_subjects.append(student.eng,student.tec,student.csi,student.wsi,student.acf,student.vdt,student.tec2,student.app,student.app2,student.bme,student.bsp,student.cae,student.che,student.eng2,student.hea,student.vho,student.hpe,student.hum,student.mat,student.oed,student.pes,student.var)

    def count_cs():
        """Checks if the student passes (based on C_threshold) and assigns them two C's if they passed that subject"""
        if any(all_subject >= C_threshold):
            return "Two C's"
        else:
            return 'No C'









    
    

 

