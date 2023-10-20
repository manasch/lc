import json
import re

from urllib.parse import urlparse

from .gfg_consts import gfg_endpoints
from .gfg_objects import Problem, ProblemURL

def parse_problem_url(url: str) -> ProblemURL:
    if not url.startswith(gfg_endpoints["_questions_url"]):
        raise ValueError("This is not a correct URL")
    
    parsed_url = urlparse(url)
    pattern = re.compile("/problems/([a-zA-Z0-9\-]+)/(\d+)")
    slug = pattern.search(parsed_url.path).group(1)
    problem_type = pattern.search(parsed_url.path).group(2)

    return ProblemURL(slug, int(problem_type))

def parse_problem(data: dict) -> Problem:
    question_id = int(data.get("id"))
    problem_name = data.get("problem_name")
    problem_type = data.get("problem_type")
    slug = data.get("slug")
    difficulty = data.get("difficulty")
    custom_input_format = data.get("custom_input_format")
    tags = data.get("tags")
    problem_question = data.get("problem_question")

    return Problem(question_id, problem_name, problem_type, slug, difficulty, custom_input_format, tags, problem_question)

def markdown_output(problem: Problem) -> str:
    md = f"""\
[[{problem.question_id}] - {problem.problem_name}]({problem.url})

---

- {problem.difficulty}
- {", ".join(problem.topic_tags)}
- {", ".join(problem.company_tags)}

---

## Problem Statement

{problem.problem_question}

---

## Solution

```
```

---

## Notes

"""
    return md
