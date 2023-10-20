from .gfg_consts import gfg_endpoints

class GFGClass:
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
class Problem(GFGClass):
    def __init__(
        self,
        question_id: int,
        problem_name: str,
        problem_type: int,
        slug: str,
        difficulty: str,
        custom_input_format: str,
        tags: dict,
        problem_question: str
    ):
        self.question_id = question_id
        self.problem_name = problem_name
        self.problem_type = problem_type
        self.slug = slug
        self.difficulty = difficulty
        self.custom_input_format = custom_input_format
        self.company_tags = tags.get("company_tags", [])
        self.topic_tags = tags.get("topic_tags", [])
        self.problem_question = problem_question.replace("\r", "").replace("18px", "14px")
        self.url = gfg_endpoints["_questions_url"] + self.slug + str(self.problem_type)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.question_id}.{self.slug}>"

class ProblemURL(GFGClass):
    def __init__(self, slug: str, problem_type: int):
        self.slug = slug
        self.url = gfg_endpoints["_questions_url"] + self.slug + str(problem_type)
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.slug}>"
