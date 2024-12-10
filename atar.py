    import csv
    import openpyx1

    def get_file_input():
        file_path = input("Please enter your excel file: ")
        
        try:
            workbook = openpyx1.load_workbook(file_path)
            sheet = workbook.activate
            
            sheet.cell(row=row, column =28, value=calculate_atar())
            sheet.cell(row=row, column =29, value=calculate_tea())
            sheet.cell(row=row, column =30, value=count_cs())
            
            workbook.save("Updated_" + file_path)
    for row in csv_reader: 
        index = index + 1 
        print(row) 
        if index ==1 or index == 2 or index == 3 or index == 4: 
                continue 
        for i in range(2,27): 
            if row[i] == "": 
                row[i] = 0 
    # Open the output file for writing
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows_without_header)  # Write the remaining rows to the output file


    index = 0 
        
     for row in csv_reader: 
             index += 1 
             print(row) 
                

    import csv# Import the end of term year 12’s subject marks 

    class Student: 

        def __init__(self,studentcode,studentname,acc,acf,app,ara,bme,bme2,cae,che,che2,com,eng,eng2,hea,hea2,hum,hum2,mat,mat2,mat3,mat4,oed,pes,phy,psy,var):

            self.studentcode = studentcode 
            self.studentname = studentname 
            self.acc = int(acc) 
            self.acf = int(acf) 
            self.app = int(app) 
            self.ara = int(ara)         
            self.ara = int(ara) 
            self.bme = int(bme) 
            self.bme2 = int(bme2) 
            self.cae = int(cae) 
            self.che = int(che) 
            self.che2 = int(che2) 
            self.com = int(com) 
            self.eng = int(eng)
            self.eng2 = int(eng2)
            self.hea = int(hea) 
            self.hea2 = int(hea2) 
            self.hum = int(hum) 
            self.hum2 = int(hum2) 
            self.mat = int(mat) 
            self.mat2 = int(mat2) 
            self.mat3 = int(mat3) 
            self.mat4 = int(mat4) 
            self.oed = int(oed) 
            self.pes = int(pes) 
            self.phy = int(phy) 
            self.psy = int(psy) 
            self.var = int(var) 

     

    student = [] 

     
       student = Student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10], row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27])
       students.append(student) 

            
    top_4_marks = []
    all_subject = []
    for student in students:
        top_4_marks = get_top_4_marks()
        all_subjects.append(student.acc,student.acf,student.app,student.ara,student.bme,student.bme2,student.cae,student.che,student.che2,student.com,student.eng,student.eng2,student.hea,student.hea2,student.hum,student.hum2,student.mat,student.mat2,student.mat3,student.mat4,student.oed,student.pes,student.phy,student.psy,student.var)
        
    # Constants 
    C_threshold = 50  # Minimum average score to achieve a "C"  

        def get_top_4_marks(self,):
            """Retrieve the top 4 subject marks for a student."""
            return sorted (self.acc,self.acf,self.app,self.ara,self.bme,self.bme2,self.cae,self.che,self.che2,self.com,self.eng,self.eng2,self.hea,self.hea2,self.hum,self.hum2,self.mat,self.mat2,self.mat3,self.mat4,self.oed,self.pes,self.phy,self.psy,self.var, reverse=True)[:4]
            
            
    def calculate_tea(): 
        """Calculate their tea score"""
        return (top_4_marks * 100)
        
    # def calculate_atar(): 
    #     """Calulate Atar using their top 4 subject marks"""
        

    def count_cs():
        """Checks if the student passes (based on C_threshold) and assigns them two C's if they passed that subject"""
        if any(all_subject >= C_threshold):
            return "Two C's"
        else:
            return 'No C'







     

