import json
import re

from urllib.parse import urlparse

from .codeninja_consts import codeninja_endpoints
from .codeninja_objects import Problem, ProblemURL

def parse_problem_url(url: str) -> ProblemURL:
    if not url.startswith(codeninja_endpoints["problems_url"]):
        raise ValueError("This is not a correct URL")
    
    parsed_url = urlparse(url)
    pattern = re.compile("/studio/problems/([a-zA-Z0-9\-_]+)")
    slug = pattern.search(parsed_url.path).group(1)

    return ProblemURL(slug)

def parse_problem(data: dict) -> Problem:
    offering_id = data.get("offering").get("id")
    slug = data.get("offering").get("slug")
    _id = data.get("offerable").get("problem").get("id")
    problem_name = data.get("offerable").get("problem").get("name")
    problem_description = data.get("offerable").get("problem").get("description")
    sample_tcs = data.get("offerable").get("problem").get("sample_testcase")
    difficulty = data.get("offerable").get("problem").get("difficulty")
    practice_topics = data.get("offerable").get("problem").get("practice_topics")
    company_list = data.get("offerable").get("problem").get("company_list")

    return Problem(offering_id, slug, _id, problem_name, problem_description, sample_tcs, difficulty, practice_topics, company_list)

def markdown_output(problem: Problem) -> str:
    md = f"""\
[[{problem.problem_id}] - {problem.problem_name}]({problem.url})

---

- {problem.difficulty}
- {", ".join(problem.practice_topics)}
- {", ".join([company.get("name") for company in problem.company_list])}

---

## Problem Statement

{problem.problem_description}

{problem.sample_tcs}

---

## Solution

```
```

---

## Notes

"""
    md = re.sub('(<h5 id="input-format">.*)', '<details><summary> Detailed explanation (Input/output format, Notes, Images) </summary>\n\\1', md)
    md = re.sub('\n(<h5 id="constraints">.*)', '</details>\n\n\\1', md)
    return md
