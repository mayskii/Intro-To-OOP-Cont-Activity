from school_schedule.student import Student

def test_student_initialization():
#Arrange
    name = "Sam"
    grade = "freshmen"
    classes = ["math", "english", "art", "band"]

#Act
    student = Student(name, grade, classes)

#Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes


def test_add_new_class():
#Arrange
    name = "Alice"
    grade = "freshmen"
    classes = ["math", "band", "music"]
    student = Student(name, grade, classes)

#Act
    result = student.add_class("art")

#Assert
    assert result == ["math", "band", "music", "art"]


def test_return_correct_number_of_classes():
#Arrange
    name = "Vivian"
    grade = "freshmen"
    classes = ["math", "band", "music", "biology"]
    student = Student(name, grade, classes)

#Act
    result = student.get_num_classes()

#Assert
    assert result == 4


def test_return_zero_for_empty_list_of_classes():
#Arrange
    name = "Maya"
    grade = "freshmen"
    classes = []
    student = Student(name, grade, classes)

#Act
    result = student.get_num_classes()
    
#Assert
    assert result == 0

