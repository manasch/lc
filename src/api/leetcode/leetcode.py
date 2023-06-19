import requests

from .leetcode_classes import Problem
from .leetcode_consts import leetcode_endpoints
from .leetcode_graphql import get_schema
from .leetcode_utils import parse_problem

class LeetcodeAPI():
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __init__(self):
        self._session = requests.Session()
        self._headers = {}
        self.csrf = None
    
    def call(self, data: dict) -> dict:
        if not self.csrf:
            self.get_csrf()
        
        res = self._session.post(leetcode_endpoints['_api_endpoint'], json={"query": data["query"], "variables": data["variables"]}, headers = self._headers)
        return res.json()
    
    def get_csrf(self):
        res = self._session.get(leetcode_endpoints["_base_url"])
        self.csrf = res.cookies.get("csrftoken")
        self._headers.update({
            "Referer": leetcode_endpoints["_base_url"],
            "Content-Type": "application/json",
            'X-CSRFToken': self.csrf
        })
    
    def fetch_problem_data(self, slug: str) -> Problem:
        variables = {
            "titleSlug": slug
        }
        body = get_schema("questionData", variables)
        return parse_problem(self.call(body).get("data").get("question"))
