# Lab 6 — Team Submission

This branch is the consolidated Lab 6 submission branch. The original contributor pull requests were merged into this branch so the team's work remains together and the original PR commits remain in its history.

## Included

- **Bavly — Part A and Part C:** TDD registration implementation and tests, invoice characterization tests, refactored `invoice.py` with `SiblingPolicy`, code-smells table, TDD run log and commit history.
- **Nicole — Task A1:** coverage explanation and coverage report contribution. The old SVG was recreated, not a genuine terminal screenshot; add a real screenshot before submission.
- **David Albert — Task B1:** Behave registration feature with the drop scenario, step definitions and environment setup. These files are included in the consolidated code.
- **David Gerges — Part D:** three Gherkin scenarios for the team story in `team_story.feature`.

## Final evidence to add

1. Save the real 100% coverage terminal screenshot as `docs/lab6/coverage-100-percent.png`.
2. Run `python -m behave` from `lab6/` and save the actual all-green output as `docs/lab6/behave-output.txt`.

Do not submit fabricated screenshots or output. Re-run the commands on this branch before the LMS upload.

## Verification commands

From the repository root:

```bash
cd lab6
python -m pytest tests --cov=registration --cov-report=term-missing
python -m behave
python -m ruff check .
```

## Contents

- `lab6/`: source code, unit tests and Behave features/steps.
- `docs/lab6/`: assignment answers, team story, smells table, TDD log and submission notes.
