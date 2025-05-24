import unittest
from src.students import StudentManagement


class TestStudentManagement(unittest.TestCase):

    def test_add_student(self):

        #given
        student_management = StudentManagement()
        expected = True

        #when
        result = student_management.add_student(321,"Jola", 17)

        #then
        self.assertEqual(expected, result)

    def test_add_student_id_none(self):

        #given
        student_management = StudentManagement()
        expected = False

        #when
        result = student_management.add_student(None,"Jola", 18)

        #then
        self.assertEqual(expected, result)

    def test_update_students(self):

        #given
        student_management = StudentManagement()
        student_management.add_student(333, "Ilona", 21)
        expected = True
        #print(student_management.students)

        #when
        result = student_management.update_student(333, "Ewa", 22)
        #print(student_management.students)
        
        #then
        self.assertEqual(expected, result)
    
    def test_remove_student(self):
        #given
        student_management = StudentManagement()
        student_management.add_student(222, "Iza", 20)
        expected = True

        #when
        result = student_management.remove_student(222)

        #then
        self.assertEqual(expected, result)
    
    def test_add_grade(self):
        #given
        student_management = StudentManagement()
        student_management.add_student(123, "michal", 13)
        expected = True
        
        #when
        result = student_management.add_grade(123, "muzyka", 2.0)
        
        #then 
        self.assertEqual(result, expected)
        
    def test_avg_grades(self):
        
        #given 
        student_management = StudentManagement()
        student_management.add_student(112, "Karolina", 12)
        student_management.add_grade(112, "muzyka", 3.0)
        student_management.add_grade(112,"muzyka", 5.0)
        student_management.add_grade(112, "wf", 4.0)
        expected = 4.0
        
        #when
        result = student_management.avg_grades("wf")

        #then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
