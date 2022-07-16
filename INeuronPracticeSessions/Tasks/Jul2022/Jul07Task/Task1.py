from Utils import CustomLogging


# Focused scenario's creating of
#  Class
#  Object
#  Constructor
#  Private variables

class INeuron:
    geo_location = {"india": {"hq": "bangalore", "dc": "hyderabad"}}
    __description = "Some description"

    def __init__(self):
        self.__premium_mentors = ["Sudhanshu", "Sunny", "Navin reddy", "Hitesh choudhary"]

    def get_all_mentors(self):
        print(", ".join(self.__premium_mentors))
        return self.__premium_mentors

    def get_ineuron_locations(self, p_country="india"):
        result = self.__convert_dict_to_string(p_country.lower())
        if result is None:
            CustomLogging.CLogger(f"No defined branches at specified location: {p_country.upper()}")
            return ""
        else:
            return result

    def __convert_dict_to_string(self, country):
        location_by_country = self.geo_location.get(country)
        if location_by_country:
            list_of_locations = ""
            for key, value in location_by_country.items():
                if list_of_locations == "":
                    list_of_locations = key.upper() + ": " + value.capitalize()
                else:
                    list_of_locations += ", " + (key.upper() + ": " + value.capitalize())
            return list_of_locations
        else:
            return None


i = INeuron()
print("Courses offered: ", end = "")
i.get_all_mentors()

print("india:", end=", ")
print(i.get_ineuron_locations())

print("US", end=", ")
print(i.get_ineuron_locations("us"))

# Accessing & Updating private reference type variable.
print("__premium_mentors:", i._INeuron__premium_mentors)
i.__premium_mentors = ["Zuck"]
print(i._INeuron__premium_mentors)

# Accessing & Updating private primitive type variable.
print("Before update, '__description':", i._INeuron__description)
i.__description = "This is new description"
print("After update, '__description':", i._INeuron__description)

# When we see the help of INeuron class we wont be able see the private members or methods
print(help(INeuron))


