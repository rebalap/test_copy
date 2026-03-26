import anthropic
import re

CRITERIA = [
    "Does the headline mention a specific time benefit (e.g. minutes, hours)?",
    "Does the headline avoid buzzwords like 'streamline', 'leverage', 'synergy'?",
    "Is the headline under 10 words?",
    "Does the subheadline address a specific pain point?",
    "Does the CTA use action-first language (verb at the start)?",
    "Is the copy free of passive voice?",
    "Would a non-technical person understand it immediately?",
]

def score_copy():
    with open("copy.md", "r") as f:
        copy = f.read()

    client = anthropic.Anthropic()
    score = 0

    for criterion in CRITERIA:
        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=10,
            messages=[{
                "role": "user",
                "content": f"""Copy:
{copy}

Criterion: {criterion}
Answer only YES or NO."""
            }]
        )
        answer = response.content[0].text.strip().upper()
        if answer == "YES":
            score += 1

    print(f"SCORE: {score}/{len(CRITERIA)}")
    return score

if __name__ == "__main__":
    score_copy()
