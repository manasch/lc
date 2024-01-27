import requests
from urllib.error import HTTPError

from .codeninja_objects import Problem
from .codeninja_consts import codeninja_endpoints
from .codeninja_utils import parse_problem

class CodeNinjaAPI():
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __init__(self):
        self.session = requests.Session()
        self.headers = {}
    
    def call(self, url: str) -> dict:
        res = self.session.get(url)
        return res.json()
    
    def fetch_problem_data(self, slug: str) -> Problem:
        url = codeninja_endpoints.get("api_endpoint") + \
            f"v3/public_section/problem_detail?slug={slug}"
        
        response = self.call(url)
        if response.get("data"):
            return parse_problem(response.get("data"))
        raise HTTPError(url, response.get("error").get("code"), response.get("error").get("message"))
    