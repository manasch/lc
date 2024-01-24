import requests
from urllib.error import HTTPError

from .codeninja_objects import Problem
from .codeninja_consts import codeninja_consts
from .codeninja_utils import parse_problem

class CodeNinjaAPI():
    def __repr__(self):
        return f"<{self.__class__.__name__}>"
    
    def __init__(self):
        self.session = requests.Session()
        self.headers = {}
    
    def call(self, url: str) -> dict:
        pass
    