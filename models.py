class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}"

    def to_dict(self) -> dict:
        return {"type": "Person", "name": self.name, "age": self.age}


class Student(Person):
    def __init__(self, name: str, age: int, field_of_study: str, year_of_study: int, score_avg):
        super().__init__(name, age)
        self.field_of_study= field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg

    def getFieldOfStudy(self):
        return self.field_of_study


    def getYearOfStudy(self):
        return self.year_of_study
    

    def getScoreAvg(self):
        return self.score_avg

    def display(self) -> str:
        return (
        super().display() +
        f"\nRole: Student\nField of Study: {self.getFieldOfStudy()}\nYear of Study: {self.getYearOfStudy()}\nAverage Score: {self.getScoreAvg()}" )


    def to_dict(self) -> dict:
        return {
         **super().to_dict(),
         "type": "Student",
        "field_of_study": self.field_of_study,
        "year_of_study": self.year_of_study,
        "score_avg": self.score_avg
        }


class Worker(Person):
    def __init__(self, name: str, age: int, field_of_work: str, salary: int):
        super().__init__(name, age)
        self.field_of_work = field_of_work
        self.salary = salary

    def get_field_of_work(self):
        return self.field_of_work

    def getSalary(self):
        return self.salary
    
    def display(self) -> str:
        return (
        super().display() +
        f"\\nRole: Worker\\nField of Work: {self.get_field_of_work()}\\nSalary: {self.getSalary()}")


    def to_dict(self) -> dict:
        return {
        **super().to_dict(),
        "type": "Worker",
        "field_of_work": self.field_of_work,
        "salary": self.salary}
