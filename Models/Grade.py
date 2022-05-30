class Grade:
    gradingCompany: str
    date: str
    newGrade: str
    idx: str

    def __init__(self, grading_company: str, date: str, new_grade: str):
        self.gradingCompany = grading_company
        self.date = date
        self.newGrade = new_grade
        self.idx = grading_company + ': ' + new_grade
