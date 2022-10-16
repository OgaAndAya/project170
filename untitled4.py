from tkinter import*
root= Tk()
root.geometry("600x600")

percentage_grade_3_label= Label(root)
percentage_grade_5_label= Label(root)
percentage_grade_8_label= Label(root)
percentage_grade_12_label= Label(root)

class grade_3():
    def __init__(self,language_arts,mathematics):
        self.language_arts= language_arts
        self.mathematics= mathematics
    def percentage(self):
        total_marks= self.language_arts + self.mathematics
        total_marks_with_100= total_marks*100
        grade_3_percentage= total_marks_with_100/200
        percentage_grade_3_label["text"]= grade_3_percentage
        
class grade_5():
    def __init__(self,language_arts,mathematics,science):
        self.language_arts= language_arts
        self.mathematics= mathematics
        self.science= science
    def percentage(self):
        total_marks= self.language_arts + self.mathematics + self.science
        total_marks_with_100= total_marks*100
        grade_5_percentage= total_marks_with_100/300
        percentage_grade_5_label["text"]= grade_5_percentage\
            
class grade_8():
    def __init__(self,language_arts,mathematics,science,history):
        self.language_arts= language_arts
        self.mathematics= mathematics
        self.science= science
        self.history=history
    def percentage(self):
        total_marks= self.language_arts + self.mathematics + self.science + self.history
        total_marks_with_100= total_marks*100
        grade_8_percentage= total_marks_with_100/400
        percentage_grade_8_label["text"]= grade_8_percentage\

class grade_12():
    def __init__(self,language_arts,mathematics,science,history,gym):
        self.language_arts= language_arts
        self.mathematics= mathematics
        self.science= science
        self.history=history
        self.gym=gym
    def percentage(self):
        total_marks= self.language_arts + self.mathematics + self.science + self.history + self.gym
        total_marks_with_100= total_marks*100
        grade_12_percentage= total_marks_with_100/500
        percentage_grade_12_label["text"]= grade_12_percentage\
                        
            
object_grade_3= grade_3(40,50)
grade_3_btn= Button(root,text= "Grade 3", command= object_grade_3.percentage)
grade_3_btn.pack(padx=20,pady=20)
percentage_grade_3_label.pack(padx=20,pady=20)

object_grade_5= grade_5(40,50,90)
grade_5_btn= Button(root,text= "Grade 5", command= object_grade_5.percentage)
grade_5_btn.pack(padx=20,pady=20)
percentage_grade_5_label.pack(padx=20,pady=20)

object_grade_8= grade_8(40,50,90,120)
grade_8_btn= Button(root,text= "Grade 8", command= object_grade_8.percentage)
grade_8_btn.pack(padx=20,pady=20)
percentage_grade_8_label.pack(padx=20,pady=20)

object_grade_12= grade_12(40,50,90,120,150)
grade_12_btn= Button(root,text= "Grade 12", command= object_grade_12.percentage)
grade_12_btn.pack(padx=20,pady=20)
percentage_grade_12_label.pack(padx=20,pady=20)

root.mainloop()


