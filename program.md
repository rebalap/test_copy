# Copy Improvement Agent

## Your job
Improve the marketing copy in `copy.md` to maximize the eval score.

## Rules
- You may ONLY edit `copy.md`
- NEVER touch `eval.py`
- Run `python eval.py` to get the current score before and after each change
- If the score improves: run `git add copy.md && git commit -m "round N: score X→Y"`
- If the score stays the same or drops: run `git checkout copy.md` to revert
- Log every round in `experiments.md`: what you changed, why, and the result

## Strategy
- Start by running eval.py to get the baseline score
- Form a hypothesis about what criterion is likely failing
- Make ONE focused change per round
- Run eval.py again to check
- Keep or revert, then move to the next hypothesis

## Stop when
- Score reaches 7/7, OR
- You have completed 30 rounds
