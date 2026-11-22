# Lab 6 — Team Submission

This branch is the consolidated Lab 6 submission branch. The original contributor pull requests were merged into this branch so the team's work remains together and the original PR commits remain in its history.

## Included

- **Bavly — Part A and Part C:** TDD registration implementation and tests, invoice characterization tests, refactored `invoice.py` with `SiblingPolicy`, code-smells table, TDD run log and commit history.
- **Nicole — Task A1:** coverage explanation and coverage report contribution. The SVG is a recreated visual, not the genuine terminal screenshot.
- **David Albert — Task B1:** Behave registration feature with the drop scenario, step definitions and environment setup.
- **David Gerges — Part D:** three Gherkin scenarios for the team story in `team_story.feature`.

## Evidence status and canonical paths

All evidence paths below are relative to `docs/lab6/`:

1. **Coverage screenshot (pending):** add the genuine terminal screenshot at `evidence/coverage_100.png`. Do not treat `coverage_100.svg` as the original screenshot.
2. **Behave historical output:** `evidence/behave_after.txt` contains the supplied run output (7 scenarios / 28 steps). It is not a fresh rerun on the consolidated branch.
3. **Fresh Behave rerun (pending):** run `python -m behave` from `lab6/` and save the actual output as `docs/lab6/evidence/behave-rerun.txt`.

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
- `docs/lab6/`: assignment answers, team story, smells table, TDD log and submission evidence.
- `docs/lab6/evidence/`: test reports, run logs and the pending original screenshot.
