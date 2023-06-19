from .leetcode_consts import leetcode_endpoints

class LeetcodeClass:
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

class Problem(LeetcodeClass):
    def __init__(
        self,
        question_id: str,
        question_frontend_id: str,
        title: str,
        slug: str,
        difficulty: str,
        similar_questions: list,
        tags: list,
        content: str,
        solution: str
    ):
        self.question_id = question_id
        self.question_frontend_id = question_frontend_id
        self.title = title
        self.slug = slug
        self.difficulty = difficulty
        self.similar_questions = similar_questions
        self.tags = tags
        self.content = content
        self.solution = solution
        self.url = leetcode_endpoints['_questions_url'] + self.slug
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.question_frontend_id}.{self.slug}>"

class ProblemURL(LeetcodeClass):
    def __init__(self, slug: str):
        self.slug = slug
        self.url = leetcode_endpoints["_questions_url"] + self.slug
    
    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.slug}>"
