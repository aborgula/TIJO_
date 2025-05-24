class StudentManagement:

    def __init__(self):
        self.students = {}

    def add_student(self, id: str, name: str, age: int) -> bool:

        if id is None or name is None or age is None:
            return False
        else:
            self.students[id] = {"name": name, "age": age}
            return True



    def update_student(self, id: str, name: str, age: int) -> bool:
        
        if id is None or name is None or age is None:
            return False
        
        if id in self.students:
            self.students[id]["name"] = name
            self.students[id]["age"] = age
            return True
        

    def remove_student(self, id: str) -> bool:
        
        if id in self.students:
            del self.students[id]
            return True
        
        return False
        

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        
        grades = {2.0, 3.0, 4.0, 5.0}
        
        if student_id not in self.students or grade not in grades:
            return False
        
        if "grades" not in self.students[student_id]:
            self.students[student_id]["grades" ] = {}
            
        if subject not in self.students[student_id]["grades"]:
            self.students[student_id]["grades"][subject] = []
            
        self.students[student_id]["grades"][subject].append(grade)
        return True
        

    def avg_grades(self, subject: str) -> float:
        
        sum = 0
        amount = 0
        for student_id in self.students:
            for grade in self.students[student_id]["grades"][subject]:
                sum += grade
                amount += 1
        
        return sum/amount
    
    
    def students(self):
        return self.students
    
    
