from Utils.CustomExceptions import CExcept
from Utils.CustomLogging import CLogger
from Task6 import TechLang, Mentor
import re


class ClassCourses(TechLang, Mentor):
    _courses = {
        "data_science": "Data Science",
        "development": "Development",
        "aptitude": "Aptitude",
        "cloud": "Cloud",
        "dev_ops": "Dev Ops",
        "database": "Database",
        "big_data": "Big Data"
    }

    def __init__(self):
        self._course_by_lang = {
            self._courses.get("data_science"): [TechLang._python, TechLang._maths, TechLang._mssql, TechLang._mssql],
            self._courses.get("development"): [TechLang._java, TechLang._js, TechLang._python, TechLang._mysql],
            self._courses.get("aptitude"): [TechLang._maths, TechLang._reasoning],
            self._courses.get("cloud"): [TechLang._aws, TechLang._azure, TechLang._gcp],
            self._courses.get("dev_ops"): [TechLang._jenkins, TechLang._git, TechLang._ansible, TechLang._python],
            self._courses.get("database"): [TechLang._mysql, TechLang._mssql],
            self._courses.get("big_data"): [TechLang._hadoop, TechLang._mssql]
        }
        self._courses_by_mentor = {
            self._courses.get("data_science"): [Mentor._sudhan, Mentor._sunny],
            self._courses.get("development"): [Mentor._hitesh],
            self._courses.get("aptitude"): [Mentor._sudhan],
            self._courses.get("cloud"): [Mentor._hitesh, Mentor._navin],
            self._courses.get("dev_ops"): [Mentor._navin],
            self._courses.get("database"): [Mentor._sudhan, Mentor._sunny],
            self._courses.get("big_data"): [Mentor._sunny]
        }

    def get_all_courses(self):
        """
        Get list of all the courses available.\n
        :return: list
        """
        return sorted(self._course_by_lang.keys())

    def _get_langs(self, search_text=""):
        """
        Get list of all the available languages available.\n
        Pass search text to like search on languages.\n
        :param search_text: str
        :return: list
        """
        langs = set()
        for lang in self._course_by_lang.values():
            if search_text != "":
                CLogger(f"Fetching request languages by search text: {search_text}")
                for l in lang:
                    if re.search(search_text, l, re.IGNORECASE):
                        langs.update([l])
            else:
                langs.update(lang)
        return sorted(langs)

    def _get_langs_by_course(self, course):
        """
        Get all the languages for specific course.
        :param course:
        :return:
        """
        key = None
        for v in self._course_by_lang.keys():
            if v.lower() == course.lower():
                key = v
                break
        if key is None:
            CExcept(f"Invalid course '{course}', to get the available courses call 'get_courses()'")
        CLogger(f"Returning courses for '{course}':")
        return self._course_by_lang.get(key)

    def _get_courses_by_lang(self, param_lang):
        """
        Get all the courses available for specific language.\n
        Pass the valid language to get the courses.\n
        :param param_lang: string
        :return: list
        """
        courses = set()
        for course, langs in self._course_by_lang.items():
            for lang in langs:
                if lang.lower() == param_lang.lower():
                    courses.update([course])
        if len(courses) == 0:
            CExcept(f"Passed language is '{param_lang}' invalid, to get list of languages call 'get_langs()'")
        return sorted(courses)

    def get_mentors_by_course(self, p_course):
        """
        This function return all the mentors by courses.\n
        :param p_course: str
        :return: list
        """
        course_mentors = []
        for course, mentors in self._courses_by_mentor.items():
            if course.lower() == p_course.lower():
                course_mentors = mentors
        if len(course_mentors) == 0:
            CExcept(f"Invalid course '{p_course}' passed. Call 'get_all_courses()' to get the list of courses.")
        return course_mentors


# c = ClassCourses()
# print("All courses", c.get_all_courses())
# print("All languages", c._get_langs(""))
# print(c._get_langs_by_course('data science'))
# print(c._get_courses_by_lang('python'))
# print(c.get_mentors_by_course('data science'))