import json
import re

from urllib.parse import urlparse

from .codeninja_consts import codeninja_consts
from .codeninja_objects import Problem, ProblemURL

def parse_problem_url(url: str) -> ProblemURL:
    if not url.startswith(codeninja_consts["problems_url"]):
        raise ValueError("This is not a correct URL")
    
    parsed_url = urlparse(url)
    pattern = re.compile("/studio/problems/([a-zA-Z0-9\-]+)")
    slug = pattern.search(parsed_url.path).group(1)

    return ProblemURL(slug)

def parse_problem(data: dict) -> Problem:
    pass

def markdown_output(problem: Problem) -> str:
    pass