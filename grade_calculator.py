class Grade_Calculator:

    def __init__(self, marks, totals, courses):
        self.courses_marks = marks
        self.total_marks = totals
        self.courses_names = courses
        self.courses_percentage = []


    def grade(self):
        for i in range(len(self.courses_names)) :
            self.courses_percentage.append(int((self.courses_marks[i] / self.total_marks[i]) * 100))

        for j in range(len(self.courses_percentage)) :
            if self.courses_percentage[j] >= 91 :
                grade = 'A'
            elif self.courses_percentage[j] >= 81 and self.courses_percentage[j] < 91 :
                grade = 'B'
            elif self.courses_percentage[j] >= 71 and self.courses_percentage[j] < 81 :
                grade = 'C'
            elif self.courses_percentage[j] >= 61 and self.courses_percentage[j] < 71 :
                grade = 'D'
            elif self.courses_percentage[j] >= 51 and self.courses_percentage[j] < 61 :
                grade = "D-"
            else :
                grade = 'Fail'

            print(f"In {self.courses_names[j]}, percentage : {self.courses_percentage[j]} and grade : {grade}")



no_of_courses = int(input("How many Courses you took this Semester? (provide in digits) "))
courses_names = []
courses_marks = []
total_marks = []
print(f"Provide course name, then obatined marks and lastly total marks of the course for all {no_of_courses} courses one by one ")
for n in range(no_of_courses) :
    course = input("\nCourse Name : ")
    courses_names.append(course)
    obtained = int(input(f"Marks you obtained in {course} : "))
    courses_marks.append(obtained)
    total = int(input(f"Total Marks of {course} : "))
    total_marks.append(total)

grade_calculator = Grade_Calculator(courses_marks, total_marks, courses_names) 
grade_calculator.grade()