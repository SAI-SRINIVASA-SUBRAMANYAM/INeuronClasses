from Utils import CustomLogging


# Focused scenario's creating of
#  inheritance
#  abstraction
#  protected variables

class CourseClasses:

    _greetings = "Good Luck"

    def get_course_class_info(self):
        CustomLogging.CLogger("This is the abstract method")
        pass


class FullStackDataScience(CourseClasses):

    def get_course_class_info(self):
        print("Course related to python, database, machine learning")

    def greet_students(self):
        print(self._greetings)


class FullStackWeb(CourseClasses):
    _greetings = "All the best"

    def get_course_class_info(self):
        print("Course related to Java with springboots")


class FullStackMernStack(CourseClasses):
    def get_course_class_info(self):
        print("Course related to node & react")


ds = FullStackDataScience()
ds.get_course_class_info()
ds.greet_students()

web = FullStackWeb()
web.get_course_class_info()
print(web._greetings)

ms = FullStackMernStack()
ms.get_course_class_info()
print(ms._greetings)
ms._greetings = "Mern stack is just awesome"
print(ms._greetings)

