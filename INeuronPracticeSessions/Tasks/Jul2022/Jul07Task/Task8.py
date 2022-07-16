from Utils.CustomExceptions import CExcept
from Utils.CustomLogging import CLogger
from Task7 import ClassCourses


class Students(ClassCourses):

    def __init__(self):
        self._students = list()
        super().__init__()

    def create_student(self, **kwargs):
        """
        Call this function to create a student.\n
        :param kwargs: dict
        :return: str
        """
        __student = dict()
        __student, error_field = self.__validate_student(kwargs)
        if __student is None:
            CExcept(f"Unable to create student. Missing '{error_field}' field.")
        self._students.append(__student)
        message = "Enrolled successfully"
        return message

    def get_students(self, student_id=-1):
        """
        Get all the students (Or) specific student having student id
        :param student_id: int
        :return: list
        """
        if student_id == -1:
            return self._students, len(self._students)
        elif student_id > 0:
            filtered_students = list(filter(lambda s: s.get("student_id") == student_id, self._students))
            if len(filtered_students) == 0:
                CLogger(f"Unable find details with student id: {student_id}")
            return filtered_students, len(filtered_students)

    def __validate_student(self, args):
        """
        validate student and return student object.\n
        :param args: dict
        :return: dict|None
        """
        course = args.get("course_opted")
        if course not in ClassCourses.get_all_courses(self):
            CExcept(f"Student '{args.get('first_name')}', opted an unlisted course of '{course}'.")
        required_fields = self.__student_fields().get("required_fields")
        optional_fields = self.__student_fields().get("optional_fields")

        __new_student = dict()
        for support_field in self.__student_fields().get("support_fields"):
            if support_field == "student_id":
                __new_student.update({support_field: len(self._students)+1})

        for required_field in required_fields:
            if args.get(required_field) is None:
                return None, required_field
            __new_student.update({required_field: args.get(required_field)})

        for optional_field in optional_fields:
            value = ""
            if args.get(optional_field):
                value = args.get(optional_field)
            __new_student.update({optional_field: value})
        return __new_student, "OK"

    @staticmethod
    def __student_fields():
        __fields = {
            "required_fields": ["first_name", "last_name", "email", "course_opted", "class_batch"],
            "optional_fields": ["status", "address", "is_internship_required", "is_job_assistance_required", "referred_by"],
            "support_fields": ["student_id"]
        }
        return __fields


# s = Students()
# new_students = [{
#     "first_name": "subbu",
#     "last_name": "sista",
#     "email": "subbu.sista@fb.com",
#     "course_opted": "Data Science",
#     "class_batch": "IV",
#     "is_intership_required": True,
#     "is_job_assistance_required": True,
#     "status": "student",
#     "referred_by": "Social media"
# }, {
#     "first_name": "anukool",
#     "last_name": "singh",
#     "email": "singh.ankool@ymail.com",
#     "course_opted": "Development",
#     "class_batch": "VI",
#     "is_intership_required": True,
#     "is_job_assistance_required": False,
#     "status": "employee",
#     "referred_by": "subbu.sista@fb.com"
# }, {
#     "first_name": "jeevitha",
#     "last_name": "sangivi",
#     "email": "sangivi.jeevitha@kore.ai",
#     "course_opted": "Data Science",
#     "class_batch": "IV",
#     "is_intership_required": True,
#     "is_job_assistance_required": True,
#     "status": "employee",
#     "referred_by": "subbu.sista@fb.com"
# }, {
#     "first_name": "annie",
#     "last_name": "shiek",
#     "email": "shiek.annie@gaintcloud.org",
#     "course_opted": "Big Data",
#     "class_batch": "IV",
#     "is_intership_required": True,
#     "is_job_assistance_required": True,
#     "status": "employee",
#     "referred_by": "sangivi.jeevitha@kore.ai"
# }, {
#     "first_name": "zetch",
#     "last_name": "makker",
#     "email": "makker.zetch@gaintcloud.du",
#     "course_opted": "Hadoop",
#     "class_batch": "IV",
#     "is_intership_required": True,
#     "is_job_assistance_required": True,
#     "status": "employee",
#     "referred_by": "sangivi.jeevitha@kore.ai"
# }]
# for new_student in new_students:
#     status = s.create_student(**new_student)
#     print(f"Dear {new_student.get('first_name').capitalize()}, Your are {status.lower()}.")
#
# s, total_count = s.get_students(99);
# print("", s, total_count, sep="\n")