import os

from .gfg import GFGAPI
from .gfg_utils import parse_problem_url, markdown_output

from ...utils import cd

class GFGCLI:
    def __init__(self):
        self._api = GFGAPI()
    
    def clone(self, url: str, *, path: str = ".") -> None:
        parsed_url = parse_problem_url(url)
        problem = self._api.fetch_problem_data(parsed_url.slug)

        with cd(path):
            fname = f"{problem.question_id}_{problem.slug}.md"

            with open(fname, "w") as f:
                f.write(markdown_output(problem))
