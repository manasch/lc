import json
import re

# import markdownify
from urllib.parse import urlparse

from .leetcode_classes import Problem, ProblemURL
from .leetcode_consts import leetcode_endpoints

def parse_problem_url(url: str) -> ProblemURL:
    if not url.startswith(leetcode_endpoints["_questions_url"]):
        raise ValueError("This is not a correct URL")
    
    parsed_url = urlparse(url)
    slug = re.search("/problems/([a-zA-Z0-9\-]+)", parsed_url.path).group(1)

    return ProblemURL(slug)

def parse_problem(data: dict) -> Problem:
    question_id = int(data.get("questionId"))
    question_frontend_id = int(data.get("questionFrontendId"))
    title = data.get("title")
    slug = data.get("titleSlug")
    difficulty = data.get("difficulty")
    similar_questions = data.get("similarQuestionList")
    tags = [x["slug"] for x in data.get("topicTags")]
    # content = markdownify.markdownify(data.get("content").strip().replace("<p>", "").replace("&nsbp;", "").replace("</p>", ""))
    content = data.get("content")
    solution = data.get("solution").get("id")

    return Problem(question_id, question_frontend_id, title, slug, difficulty, similar_questions, tags, content, solution)

def markdown_output(problem: Problem) -> str:
    md = f"""\
[[{problem.question_frontend_id}] - {problem.title}]({problem.url})

---

- {problem.difficulty}
- [Submission]()
- {", ".join(problem.tags)}

## Problem Statement

{problem.content}

## Solution

```
```

---

## Notes

"""
    return md
