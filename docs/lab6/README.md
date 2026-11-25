# Lab 6 — TDD, BDD & Refactoring (Team 7 FocusPulse)

Run everything from the `lab6/` folder: `python -m pytest -q` · `python -m behave` · `ruff check .`

## Part A — TDD and coverage (Task A1)
Before: `registration.py` 95 %, line 26 missing (`evidence/coverage_before.txt`). New test
`test_cannot_drop_course_that_is_not_registered` covers the "not registered" error → **100 %**
(`evidence/coverage_after.txt`). The coverage screenshot is included at
`evidence/coverage_100.png`.

**Does 100 % coverage prove the code is correct?** No. It only shows every line was executed by some
test; it does not prove the assertions check the right things or that all rules and inputs are
covered (for example, negative or zero hours are never tested).

## Part B — BDD (Task B1)
`lab6/features/registration.feature` contains 7 scenarios, including *Drop a registered course*,
and `lab6/features/steps/registration_steps.py` contains the corresponding drop step.
The fresh run is saved as `evidence/behave-rerun.txt`: **1 feature, 7 scenarios and 28 steps passed;
0 failed and 0 skipped**. The supplied historical output remains available as `evidence/behave_after.txt`.

## Part C — Refactoring legacy_invoice.py
### Task C1 — Smells found before touching the code (full table in `smells.md`)
| Smell | Where | Principle it breaks |
|---|---|---|
| Long if/elif chain on `kind` (checked twice) | loop body + after the loop | OCP: a new student type means editing this function |
| Magic numbers 1200, 0.5, 2000, 5000 | inside the chain | Readability: the meaning of each number is hidden |
| One function calculates the fee, formats the text, writes a file and prints | whole function | SRP: four reasons to change |
| File opened without `with` and closed by hand | `open(...)` / `f.close()` | Resource safety: the file stays open if `write` fails |
| Disk and `print` hard-wired inside the function | last lines | DIP: cannot test without writing files |
| Fee worked out per course though only total hours matter | the `for` loop | Needless complexity / duplication |
| Unknown `kind` silently gives 0 EGP and still writes an invoice | no `else` branch | Hidden bug: no validation |

### Characterization tests first
Run against the **unchanged** legacy code (`evidence/characterization_on_legacy.txt`): 8 passed
(regular 7200, scholarship 3600, international 17000 plus the registration tests).
Ruff complexity of `make_invoice` before: **6** (`evidence/complexity_before.txt`).

### Refactoring (invoice.py)
Named constants → one policy class per type (SRP) → `POLICIES` lookup (OCP) → injected writer (DIP).
Complexity after: **1** (`evidence/complexity_after.txt`). `print` was removed from the calculation.

### Task C2 — SiblingPolicy (test first)
1. Red: `test_sibling_discount_is_25_percent_off_regular` fails with `KeyError: 'sibling'` (`evidence/sibling_red.txt`).
2. Green: added `SiblingPolicy` (25 % off the regular fee, 6 h → 5400) and one `POLICIES` entry.
   `make_invoice` was **not changed**. 10 tests pass (`evidence/sibling_green.txt`).

## Part D — Gherkin scenarios for our team story
Story **S11 Create a study group (AP-16)**, owner David Gerges: `team_story.feature` (3 scenarios:
create a group and get a code, group name required, two groups never share a code).

## Evidence paths
All evidence files are stored in `docs/lab6/evidence/`:
- Coverage reports: `coverage_before.txt`, `coverage_after.txt`, `pytest-coverage-verified.txt`.
- Coverage screenshot: `coverage_100.png`.
- Behave historical output: `behave_after.txt`; fresh rerun: `behave-rerun.txt` (7 scenarios / 28 steps passed).
- Other evidence: `characterization_on_legacy.txt`, `complexity_before.txt`, `complexity_after.txt`, `sibling_red.txt`, `sibling_green.txt`.
- Root-level documentation: `git-log.txt`, `tdd-run-log.txt`, `smells.md`, `A1-answer.md`.

See `TEAM-SUBMISSION-README.md` and `evidence/README.md` for submission status.
