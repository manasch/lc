import json
import re

from urllib.parse import urlparse

from .lintcode_consts import lintcode_endpoints, lintcode_problem_level
from .lintcode_objects import Problem, ProblemURL

def parse_problem_url(url: str) -> ProblemURL:
    if not url.startswith(lintcode_endpoints["_problems_url"]):
        raise ValueError("This is not a correct URL")
    
    parsed_url = urlparse(url)
    problem_id = re.search("/problem/([0-9]+)", parsed_url.path).group(1)

    return ProblemURL(problem_id)

def parse_problem(data: dict) -> Problem:
    challenge = data.get("challenge")
    clarification = data.get("clarification")
    company_tags = data.get("company_tags")
    description = data.get("description")
    example = data.get("example")
    problem_id = str(data.get("id"))
    difficulty = lintcode_problem_level.get(str(data.get("level")))
    new_notice = data.get("new_notice")
    tags = data.get("tags")
    title = data.get("title")
    unique_name = data.get("unique_name")

    return Problem(challenge, clarification, company_tags, description, example,\
        problem_id, difficulty, new_notice, None, tags, title, unique_name)

def markdown_output(problem: Problem) -> str:
    new_notice = "\n".join(["> " + notice for notice in problem.new_notice.split("\n")]) if problem.new_notice else ""
    clarification = "\n### Clarification\n\n" + problem.clarification if problem.clarification else ""
    challenge = "\n### Challenge\n\n" + problem.challenge if problem.challenge else ""

    md = f"""\
[[{problem.problem_id}] - {problem.title}]({problem.url})

---

- {problem.difficulty}
- {", ".join(problem.tags)}
- {", ".join(problem.company_tags) if problem.company_tags else "[no companies listed]"}

---

## Problem Statement

### Description

{problem.description}

{new_notice}

### Example

{problem.example}

{clarification}

{challenge}

---

## Solution

```
```

---

## Notes

"""
    return md
