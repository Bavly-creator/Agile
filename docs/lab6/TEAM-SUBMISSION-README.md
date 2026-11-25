# Lab 6 — Team Submission

This branch is the consolidated Lab 6 submission branch. The original contributor pull requests were merged into this branch so the team's work remains together and the original PR commits remain in its history.

## Included

- **Bavly — Part A and Part C:** TDD registration implementation and tests, invoice characterization tests, refactored `invoice.py` with `SiblingPolicy`, code-smells table, TDD run log and commit history.
- **Nicole — Task A1:** coverage explanation and coverage report contribution. The coverage screenshot is included separately as `evidence/coverage_100.png`.
- **David Albert — Task B1:** Behave registration feature with the drop scenario, step definitions and environment setup.
- **David Gerges — Part D:** three Gherkin scenarios for the team story in `team_story.feature`.

## Evidence status and canonical paths

All evidence paths below are relative to `docs/lab6/`:

1. **Coverage screenshot:** `evidence/coverage_100.png` is present in this branch.
2. **Behave historical output:** `evidence/behave_after.txt` contains the supplied earlier run output (7 scenarios / 28 steps).
3. **Fresh Behave rerun:** `evidence/behave-rerun.txt` contains the fresh run from the consolidated working copy: 1 feature, 7 scenarios and 28 steps passed, with 0 failures and 0 skipped.

Do not fabricate screenshots or test output. The evidence files above are committed to this branch.

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
- `docs/lab6/evidence/`: coverage screenshot, test reports and run logs.
