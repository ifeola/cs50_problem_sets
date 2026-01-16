import re, csv


subjects = ["mathematics", "english", "chemistry", "physics", "biology", "economics", "agric science", "government"]
levels = ["JS1", "JS2", "JS3", "SS1", "SS2", "SS3"]


class Student:
    def __init__(self, name, student_id, level):
        self.name = name
        self.student_id = student_id
        self.level = level
        self.grades = {}

    def add_grade(self, subject, score):
        self.grades[subject] = score

    def get_total_score(self):
        return sum(self.grades.values())

    def get_average_score(self):
        if len(self.grades) == 0:
            return 0
        return self.get_total_score() / len(self.grades)

    def get_grade(self):
        average = self.get_average_score()
        if average < 40:
            return "F"
        elif average < 50:
            return "E"
        elif average < 60:
            return "D"
        elif average < 70:
            return "C"
        elif average < 80:
            return "B"
        else:
            return "A"

def is_name_valid(student_name):
    match = re.fullmatch(r"[A-Za-z]+ [A-Za-z]+", student_name)
    return match

def is_student_id_valid(student_id):
    valid = re.fullmatch(r"[A-Za-z0-9]{6}", student_id)
    return valid

def is_new(student_id):
    with open("./db.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if student_id.strip() == row["student_id"].strip():
                return False
        return True


def get_student_details():
    while True:
        student_name = input("Enter student's name: ").strip().lower()
        match = is_name_valid(student_name)
        if match:
            break
        print("Enter a valid name (first and last name).")

    while True:
        student_id = input("Enter student's id: ")
        valid = is_student_id_valid(student_id)
        checked = is_new(student_id)
        if valid and checked:
            break
        print("Enter a valid student ID.")

    while True:
        level = input("Enter student's level (Example: SS1 or JS1): ")
        if level in levels:
            break
        print("Enter a valid student level.")
    student = Student(student_name, student_id, level)
    return student

def get_student_scores(student):
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter score for {subject}: "))
                if 0 <= score <= 100:
                    student.add_grade(subject, score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Enter a valid number")
    return student


def store_student(student):
    if type(student) != Student:
        raise ValueError("This student is not a type Student.")
    with open("./db.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "student_id", "level", "mathematics", "english", "chemistry", "physics", "biology", "economics", "agric science", "government", "total_score", "average_score", "grade"])
        writer.writerow({"name": student.name, "student_id": student.student_id, "level": student.level, "mathematics": student.grades["mathematics"], "english": student.grades["english"], "chemistry": student.grades["chemistry"], "physics": student.grades["physics"], "biology": student.grades["biology"], "economics": student.grades["economics"], "agric science": student.grades["agric science"], "government": student.grades["government"], "total_score": student.get_total_score(), "average_score": student.get_average_score(), "grade": student.get_grade()})

def result_template(student):
    template = f"""
        ========================================
                  STUDENT RESULT SHEET
        ========================================
        ========================================
        Student ID   :   {student.student_id}
        Name         :   {student.name}
        Class        :   {student.level}
        ----------------------------------------
        Subject          Score
        ----------------------------------------
        Mathematics      {student.grades["mathematics"]}
        English          {student.grades["english"]}
        Chemistry        {student.grades["chemistry"]}
        Physics          {student.grades["physics"]}
        Biology          {student.grades["biology"]}
        Econimics        {student.grades["economics"]}
        Agric Science    {student.grades["agric science"]}
        Government       {student.grades["government"]}
        ----------------------------------------
        Total Score      {student.get_total_score()}
        Average Score    {student.get_average_score()}
        Grade            {student.get_grade()}
        ========================================
        """
    return template

def main():
    student = get_student_details()
    get_student_scores(student)
    store_student(student)
    result = result_template(student)
    print(result)


if __name__ == "__main__":
    main()