from Utils.CustomLogging import CLogger
from Utils.CustomExceptions import CExcept
from Task8 import Students
from Task9 import Opportunities
import re


class INeuron(Students, Opportunities):
    __about_us = "iNeuron is a all-rounder which provides jobs, tech education, internship, job assistance.\nPropound to build an sophisticated software cum industry standard solutions.\nBridge the gap between companies expectation against profession's knowledge,\nwith training, internship, hackathon programs"
    __options = [
        {'student': 'Become a Student'},
        {'blogger': 'Become a Blogger'},
        {'affiliate': 'Become an Affiliate'},
    ]

    def __init__(self):
        super().__init__()
        CLogger("Welcome INeuron!!", 'i')

    def show_options(self):
        print("Welcome to INeuron.\nWe provide following services please choose an option from below menu:")
        options = [value for option in self.__options for value in option.values()]
        for index, value in enumerate(options):
            print(f"{index+1}. {value}")
        user_input = self.__capture_validate_user_input(len(options))
        selected_option = options[user_input - 1]
        for option in self.__options:
            for key, value in option.items():
                if value == selected_option:
                    self.functional_unit = key
        self.handle_functionality(selected_option)

    def student_functionality(self):
        key = 'yes'
        while re.search("yes|y", key, re.IGNORECASE) :
            new_student = self.__get_student_details()
            if len(new_student.keys()) == 0:
                CExcept("Unable to create student with empty fields")
            else:
                status = self.create_student(**new_student)
                print(f"Dear {new_student.get('first_name').capitalize()}, {status}")
                _, total_count = self.get_students()
                print(f"Total number of students are {total_count}")
            key = input("Do you want to create a student? Press 'Y' to continue... ")

    def blogger_functionality(self):
        key = 'yes'
        while re.search("yes|y", key, re.IGNORECASE):
            new_blog = self.__get_blog_details()
            if len(new_blog.keys()) == 0:
                CExcept("Unable to create blog with empty fields")
            else:
                status = self.create_blog(**new_blog)
                total_count, all_blogs = self.show_blogs()
                print(all_blogs)
                print(f"Total number of blogs are {total_count}")
                print(f"Congratulations, {status}")
            key = input("Do you want to create a blog? Press 'Y' to continue... ")

    def affiliate_functionality(self):
        key = 'yes'
        while re.search("yes|y", key, re.IGNORECASE):
            new_affiliate = self.__get_affiliate_details()
            if len(new_affiliate.keys()) == 0:
                CExcept("Unable to create affiliate with empty fields")
            else:
                status = self.become_an_affiliate(**new_affiliate)
                total_count, all_affiliates = self.get_affiliates()
                print(all_affiliates)
                print(f"Total number of affiliates are {total_count}")
                print(f"{status}")
            key = input("Do you want to create a affiliate? Press 'Y' to continue... ")

    def handle_functionality(self, selected_option):
        CLogger(f"User selected, '{selected_option}' under functional unit: {self.functional_unit}", "i")
        if self.functional_unit == "student":
            self.student_functionality()
        elif self.functional_unit == "blogger":
            self.blogger_functionality()
        elif self.functional_unit == "affiliate":
            self.affiliate_functionality()

    def show_about_us(self):
        return self.__about_us

    def __get_student_details(self):
        fields = self._Students__student_fields()
        _student = dict()
        for required_field in fields.get('required_fields'):
            value = self.capture_required_field(required_field)
            _student.update({required_field: value})
        return _student

    def __get_blog_details(self):
        fields = ["p_title", "p_subheading", "p_content", "p_created_by"]
        _blog = dict()
        for required_field in fields:
            value = self.capture_required_field(required_field)
            _blog.update({required_field: value})
        return _blog

    def __get_affiliate_details(self):
        fields = ["p_affiliate_name", "p_promoted_social_networks", "p_min_num_of_proms_per_week", "p_social_status"]
        new_affiliate = dict()
        for required_field in fields:
            value = self.capture_required_field(required_field)

            try:
                if required_field == "p_min_num_of_proms_per_week" or required_field == "p_min_num_of_proms_per_week":
                    value = int(value)
                elif required_field == "p_promoted_social_networks":
                    if value.count(",") > 0:
                        value = value.split(",")
                    else:
                        value = [value]
            except Exception as e:
                CExcept(e)

            new_affiliate.update({required_field: value})
        return new_affiliate

    def capture_required_field(self, field_name):
        while True:
            if field_name == 'course_opted':
                print(self.get_all_courses())

            value = input(f"Enter {field_name}: ")
            if value.strip() == "":
                continue
            return value

    @staticmethod
    def __capture_validate_user_input(max_option_value):
        while True:
            try:
                user_input = int(input("Enter an option number from above list:"))
                if user_input > max_option_value:
                    message = "Enter invalid input. Please try again"
                    CLogger(message)
                    print(message)
                    continue
                return user_input
            except Exception as e:
                CExcept("ERROR: Please enter an option only number from above list")


i = INeuron()
print(i.show_about_us())
i.show_options()
