from Utils.CustomLogging import CLogger


class TechLang:
    _hadoop = "Hadoop"
    _maths = "Maths"
    _reasoning = "Reasoning"
    _c = "C"
    _cpp = "C++"
    _java = "Java"
    _js = "Javascript with React"
    _python = "Python"
    _ansible = "Ansible"
    _git = "Git"
    _jenkins = "Jenkins"
    _aws = "Amazon Web Services"
    _azure = "Azure"
    _gcp = "Google Cloud Platform"
    _mysql = "MySQL"
    _mssql = "Microsoft SQL Server"

    def __init__(self):
        CLogger(f"Defining basic available languages at INeuron", 'i')


class Mentor:
    _sudhan = "Sudhanshu Kumar"
    _hitesh = "Hitesh Choudary"
    _navin = "Navin Reddy"
    _sunny = "Sunny"

    def __init__(self):
        CLogger("Defining core mentors of INeuron", "i")







# t = TechLang()
# print(t.mysql)
# print(TechLang.mssql)
#
# m = Mentors()
# print(m.navin)
# print(Mentors.sudhan)
# m.sunny = "Sunny"
# # This is valid & available
# print(m.sunny)
# try:
#     # This is unavailable
#     print(Mentors.sunny)
# except Exception as e:
#     print(e)
#
# i = INeuron()
# print(i.show_about_us())
