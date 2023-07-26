import requests
from urllib.error import HTTPError

from .lintcode_objects import Problem
from .lintcode_consts import lintcode_endpoints
from .lintcode_utils import parse_problem

class LintcodeAPI():
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __init__(self):
        self._session = requests.Session()
        self._headers = {}
        self.cookie = None
    
    def call(self, url: str) -> dict:
        if not self.cookie:
            self.set_cookie()
        
        res = self._session.get(url, headers=self._headers)
        return res.json()
    
    def set_cookie(self):
        res = self._session.get(lintcode_endpoints["_base_url"])
        self.cookie = res.cookies.get("uuid")
        self._headers.update({
            "Referer": lintcode_endpoints["_base_url"],
            "Cookie": f"uuid={self.cookie}"
        })

    def fetch_problem_data(self, problem_id: str) -> Problem:
        url = lintcode_endpoints["_api_problems_url"] + problem_id
        response = self.call(url)
        if response.get("code") == 200:
            return parse_problem(response.get("data"))
        raise HTTPError(url, response.get("code"), response.get("detail"), None, None)
