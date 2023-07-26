import os

from .lintcode import LintcodeAPI
from .lintcode_utils import parse_problem_url, markdown_output

from ...utils import cd

class LintcodeCLI:
    def __init__(self):
        self._api = LintcodeAPI()
    
    def clone(self, url: str, *, path: str = ".") -> None:
        parsed_url = parse_problem_url(url)
        problem = self._api.fetch_problem_data(parsed_url.id)

        with cd(path):
            fname = f"{problem.problem_id}_{problem.unique_name}.md"

            with open(fname, "w") as f:
                f.write(markdown_output(problem))
