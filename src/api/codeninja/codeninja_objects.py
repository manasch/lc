import typing

from .codeninja_consts import codeninja_consts

class CodeNinja:
    def __repr__(self):
        return f"<{self.__class__.__name__}"

class Problem(CodeNinja):
    def __init__(
        offering_id: int,
        slug: str,
        _id: int,
        problem_name: str,
        problem_description: str,
        sample_tcs: str,
        difficulty: str,
        practice_topics: typing.List[str],
        company_list: typing.List[dict],

    ):
        self.offering_id = offering_id
        self.slug = slug
        self.problem_id = _id
        self.problem_name = problem_name
        self.problem_description = problem_description
        self.sample_tcs = sample_tcs
        self.difficulty = difficulty
        self.practice_topics = practice_topics
        self.company_list = company_list
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.problem_id}.{self.slug}>"

class ProblemURL(CodeNinja):
    def __init__(self, slug: str):
        self.slug = slug
        self.url = codeninja_consts["problems_url"] + slug
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.slug}>"