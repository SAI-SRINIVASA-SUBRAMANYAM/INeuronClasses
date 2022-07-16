from Utils.CustomLogging import CLogger
from Utils.CustomExceptions import CExcept

# Multilevel inheritance


class INeuron:

    institute_name = "INeuron"

    def get_institute_info(self):
        print("INeuron provides training session come job aids")

class Courses(INeuron):

    _courses = ["Data science", "Java", "Mern"]

    def get_course_info(self):
        print("We offer:", self._courses)

    def get_institute_name(self):
        return self.institute_name



class Internship(Courses):
    __course = ""

    def __init__(self):
        self.internship_status = "not started"

    def get_intership(self, course):
        if course in self._courses:
            self.__course = course
            self.internship_status = "started"
            CLogger(f"Internship started on '{course}' successfully")
            print(f"Internship started on '{course}' successfully")
        else:
            CExcept(f"Given '{course}' is not a listed course.")

    def complete_internship(self):
        if self.internship_status != 'started':
            CExcept("Sorry, you haven't started any internship yet!!")
        message = f"Internship successfully completed on {self.__course} from {self.get_institute_name()}"
        self.internship_status = "completed"
        CLogger(message)
        print(message)



intern = Internship()
# intern.complete_internship()
intern.get_institute_info()
intern.get_intership("Data science")
intern.complete_internship()