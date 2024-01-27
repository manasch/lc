import os

from .codeninja import CodeNinjaAPI
from .codeninja_utils import parse_problem_url, markdown_output

from ...utils import cd

class CodeNinjaCLI:
    def __init__(self):
        self._api = CodeNinjaAPI()
    
    def clone(self, url: str, *, path: str = ".") -> None:
        parsed_url = parse_problem_url(url)
        problem = self._api.fetch_problem_data(parsed_url.slug)

        with cd(path):
            fname = f"{problem.problem_id}_{problem.slug}.md"

            with open(fname, "w", encoding="utf-8") as f:
                f.write(markdown_output(problem))