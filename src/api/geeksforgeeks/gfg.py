import requests
from urllib.error import HTTPError

from .gfg_objects import Problem
from .gfg_consts import gfg_endpoints
from .gfg_utils import parse_problem

class GFGAPI():
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __init__(self):
        self._session = requests.Session()
        self._headers = {}
        self.referer = self._headers.get("Referer")
    
    def call(self, url: str) -> dict:
        if not self.referer:
            self.set_referer()
        
        res = self._session.get(url, headers=self._headers)
        return res.json()
    
    def set_referer(self):
        self._headers.update({
            "Referer": gfg_endpoints["_base_url"]
        })
    
    def fetch_problem_data(self, slug: str) -> Problem:
        url = gfg_endpoints["_api_endpoint_problems"] + slug
        response = self.call(url)
        if response.get("results"):
            return parse_problem(response.get("results"))
        raise HTTPError(url, response.get("error").get("code"), response.get("error", {}).get("message", "No Message"), None, None)
