from Utils.CustomLogging import CLogger
from Utils.CustomExceptions import CExcept
from datetime import datetime


class Opportunities:
    __blogs = list()
    __affiliates = list()

    def create_blog(self, p_title: str, p_subheading: str, p_content: str, p_created_by: str):
        title, subheading, content, created_by =\
            self.__validate_blog_creation(p_title, p_subheading, p_content, p_created_by)
        self.__blogs.append({
            "blog_id": len(self.__blogs) + 1,
            "title": title,
            "subheading": subheading,
            "content": content,
            "created_by": created_by,
            "created_at": datetime.now(),
            "claps": 0
        })
        return "Blog created successfully"

    def show_blogs(self, blog_id=-1):
        filtered_blogs = []
        if blog_id > 0:
            filtered_blogs = list(filter(lambda b: b.blog_id == blog_id, self.__blogs))
        else:
            filtered_blogs = self.__blogs
        return len(filtered_blogs), filtered_blogs

    def become_an_affiliate(self, p_affiliate_name: str, p_promoted_social_networks: list, p_min_num_of_proms_per_week: int, p_social_status: int):
        affiliate_name, promoted_social_networks, min_num_of_proms_per_week, \
        social_status, desc_social_status, min_earn = \
            self.__validate_affiliates(p_affiliate_name, p_promoted_social_networks, p_min_num_of_proms_per_week, p_social_status)
        self.__affiliates.append({
            "affiliate_id": len(self.__affiliates) + 1,
            "affiliate_name": affiliate_name,
            "promoted_social_networks": promoted_social_networks,
            "min_num_of_proms_per_week": min_num_of_proms_per_week,
            "id_social_status": social_status,
            "description_social_status": desc_social_status,
            "min_earn": min_earn
        })
        return "Congratulations on your role"

    def get_affiliates(self, affiliate_id=-1):
        filtered_affiliates = []
        if affiliate_id > 0:
            filtered_affiliates = list(filter(lambda b: b.blog_id == affiliate_id, self.__affiliates))
        else:
            filtered_affiliates = self.__affiliates
        return len(filtered_affiliates), filtered_affiliates

    @staticmethod
    def __validate_blog_creation(title: str, subheading: str, content: str, created_by: str):
        if title.strip() == "":
            CExcept("Title cannot be blank.")
        elif content.strip() == "":
            CExcept("Content cannot be blank.")
        elif created_by.strip() == "":
            CExcept("Created by cannot be blank")

        ret_title = title
        if len(title) > 100:
            ret_title = title[0:100]
            CLogger("Title should be less than or equal to 100 characters length")

        ret_subheading = subheading
        if len(subheading) > 150:
            ret_subheading = subheading[0:150]
            CLogger("Subheading should be less than or equal to 150 characters length")

        return ret_title, ret_subheading, content, created_by

    @staticmethod
    def __validate_affiliates(p_affiliate_name: str, p_promoted_social_networks: list, p_min_num_of_proms_per_week: int, p_social_status: str):
        if p_affiliate_name.strip() == "":
            CExcept("Affiliate cannot be anonymous")
        elif len(p_promoted_social_networks) == 0:
            CExcept("Minimum on one social network to be posted")
        affiliate_name = p_affiliate_name
        promoted_social_networks = p_promoted_social_networks
        min_num_of_proms_per_week = p_min_num_of_proms_per_week
        social_status = p_social_status
        desc_social_status = ""
        min_earn_per_month = 25000

        if p_min_num_of_proms_per_week <= 0:
            CLogger("Minimum on one promotion per week is needed")

        if p_social_status == 0:
            min_earn_per_month = min_earn_per_month * 10
            desc_social_status = "International Actor/Sports/Business person"
        elif p_social_status == 1:
            min_earn_per_month = min_earn_per_month * 6
            desc_social_status = "National Public Figure/Actor"
        elif p_social_status == 2:
            min_earn_per_month = min_earn_per_month * 4
            desc_social_status = "Dedicated working professional"
        elif p_social_status == 3:
            min_earn_per_month = min_earn_per_month * 2
            desc_social_status = "Part-time working professional"
        else:
            desc_social_status = "Unknown"
            CLogger(f"Please maintain the status to get better earn")

        return affiliate_name, promoted_social_networks, min_num_of_proms_per_week, social_status, desc_social_status, min_earn_per_month


# o = Opportunities()
# t_c, b = o.show_blogs()
# print(f"Total number of blogs are {t_c}, blogs: {b}.")
# my_blog = {
#     "p_title": "This is my first blog",
#     "p_subheading": "This blog is about how to write blog",
#     "p_content": """
#     There are no rules or standards to write a blog.
#     Blog should be sensible and useful to recognition, that's all.
#     Chrees.
#     """,
#     "p_created_by": "subramanyam.sista@gmail.com"
# }
# o.create_blog(**my_blog)
# print(f"Total number of blogs are {t_c}, blogs: {b}.")
#
# myaffiliation = {
#     "p_affiliate_name": "Zubuza",
#     "p_promoted_social_networks": ["manga"],
#     "p_min_num_of_proms_per_week": 1,
#     "p_social_status": 0
# }
# status = o.become_an_affiliate(**myaffiliation)
# if status == "success":
#     print(f"Congratulations!!")
# print(o.get_affiliates())
