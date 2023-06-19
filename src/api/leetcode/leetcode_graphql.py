import json

query = {
    "questionTitle": """\
    query questionTitle($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            isPaidOnly
            difficulty
            likes
            dislikes
        }
    }
    """,
    "SimilarQuestions": """\
    query SimilarQuestions($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            similarQuestionList {
            difficulty
            titleSlug
            title
            translatedTitle
            isPaidOnly
            }
        }
    }    
    """,
    "singleQuestionTopicTags": """\
    query singleQuestionTopicTags($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags {
            name
            slug
            }
        }
    }
    """,
    "questionContent": """\
    query questionContent($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
            mysqlSchemas
        }
    }
    """,
    "questionOfToday": """\
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                paidOnly: isPaidOnly
                status
                title
                titleSlug
                hasVideoSolution
                hasSolution
                topicTags {
                    name
                    id
                    slug
                }
            }
        }
    }
    """,
    "hasOfficialSolution": """\
    query hasOfficialSolution($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            solution {
            id
            }
        }
    }
    """,
    "questionData": """\
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
            likes
            dislikes
            similarQuestionList {
                title
                titleSlug
                difficulty
            }
            topicTags {
                name
                slug
            }
            content
            solution {
                id
            }
        }
    }
    """
}

def get_schema(type: str, vars: dict) -> dict:
    schema = query.get(type)

    if not schema:
        raise ValueError(f"Schema with name {type} not found.")
    
    obj = {
        "query": schema,
        "variables": vars
    }

    return obj
