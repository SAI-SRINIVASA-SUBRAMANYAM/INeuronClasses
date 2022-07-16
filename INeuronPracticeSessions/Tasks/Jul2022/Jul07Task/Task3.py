from Utils import CustomLogging

# Focused scenario's creating of
#  inheritance
#  polymorphism
#   - Overriding


class Courses:

    def get_number_of_courses_available(self):
        CustomLogging.CLogger("Base class invoked")
        print("Total 100+ courses are available")


class DataScience(Courses):

    def get_number_of_courses_available(self):
        print("Total 20+ courses are available")


class WebStack(Courses):

    def get_number_of_courses_available(self):
        print("Total 5 courses are available")


class MernStack(Courses):

    def get_number_of_courses_available(self):
        print("Total 2 courses are available")



ds = DataScience()
ds.get_number_of_courses_available()

ws = WebStack()
ws.get_number_of_courses_available()

ms = MernStack()
ms.get_number_of_courses_available()
