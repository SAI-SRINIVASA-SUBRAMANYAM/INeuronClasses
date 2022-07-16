from Utils import CustomLogging

# Accessing and updating private variables within class and outside the class


class Students:
    __total_count = 0


class DataScience(Students):
    __mentor = "Sudhanshu"

    def __init__(self):
        CustomLogging.CLogger("Default mentor name" + self.__mentor, 'i')

    def get_class_info(self):
        print ("Total students are:", self._Students__total_count)

    def update_students(self, count):
        self._Students__total_count = count

    def get_mentor_name(self):
        print("Your mentor: ", self.__mentor)

    def set_mentor_name(self, new_mentor_name):
        self.__mentor = new_mentor_name

ds = DataScience()
ds.get_class_info()
ds.update_students(157)
ds.get_class_info()
ds.get_mentor_name()
ds.__mentor = "Sudhanshu Kumar"
ds.get_mentor_name()
ds.set_mentor_name("Sudhanshu Kumar")
ds.get_mentor_name()