import typing
from abc import ABC
from .lintcode_consts import lintcode_endpoints

class LintcodeClass(ABC):
    def __init__(self):
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__}"

class ProblemURL(LintcodeClass):
    def __init__(self, problem_id: int):
        self.id = problem_id
        self.url = lintcode_endpoints["_problems_url"] + self.id
    
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

class Problem(LintcodeClass):
    def __init__(
        self,
        challenge: str,
        clarification: str,
        company_tags: typing.List[str],
        description: str,
        example: str,
        problem_id: str,
        difficulty: str,
        new_notice: str,
        notice: str,
        tags: typing.List[str],
        title: str,
        unique_name: str
    ):
        self.challenge = challenge
        self.clarification = clarification
        self.company_tags = [x.get("unique_name") for x in company_tags]
        self.description = description
        self.example = example
        self.problem_id = problem_id
        self.difficulty = difficulty
        self.new_notice = new_notice
        self.notice = notice
        self.tags = [x.get("unique_name") for x in tags]
        self.title = title
        self.unique_name = unique_name
        self.url = lintcode_endpoints["_problems_url"] + self.problem_id
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.problem_id_id}.{self.unique_name}>"
