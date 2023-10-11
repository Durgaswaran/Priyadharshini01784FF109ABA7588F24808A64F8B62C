class Student:

  def __init__(self, name, roll_no, cgpa):
    self.name = name
    self.roll_no = roll_no
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Student("priya", "ucs025", 6.5),
    Student("vishnu", "ucs035", 8.9),
    Student("aarthi", "ucs001", 8.5),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll_no: {}, CGPA: {}".format(student.name, student.roll_no,
                                                 student.cgpa))         