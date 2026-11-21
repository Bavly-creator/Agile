# Lab 6 — TDD, BDD & Refactoring (Team 7 FocusPulse)

Run everything from the `lab6/` folder: `python -m pytest -q` · `python -m behave` · `ruff check .`

## Part A — TDD and coverage (Task A1)
Before: `registration.py` 95 %, line 26 missing (`coverage_before.txt`). New test
`test_cannot_drop_course_that_is_not_registered` covers the "not registered" error → **100 %**
(`coverage_after.txt`, `coverage_100.png`).

**Does 100 % coverage prove the code is correct?** No. It only shows every line was executed by some
test; it does not prove the assertions check the right things or that all rules and inputs are
covered (for example, negative or zero hours are never tested).

## Part B — BDD (Task B1)
`lab6/features/registration.feature` now has 7 scenarios (the new one: *Drop a registered course*),
and `features/steps/registration_steps.py` has the new `@when('the student drops "{code}"')` step.
`behave_after.txt`: 1 feature passed, 7 scenarios passed, 28 steps passed.

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
Run against the **unchanged** legacy code (`characterization_on_legacy.txt`): 8 passed
(regular 7200, scholarship 3600, international 17000 plus the registration tests).
Ruff complexity of `make_invoice` before: **6** (`complexity_before.txt`).

### Refactoring (invoice.py)
Named constants → one policy class per type (SRP) → `POLICIES` lookup (OCP) → injected writer (DIP).
Complexity after: **1** (`complexity_after.txt`). `print` was removed from the calculation.

### Task C2 — SiblingPolicy (test first)
1. Red: `test_sibling_discount_is_25_percent_off_regular` fails with `KeyError: 'sibling'` (`sibling_red.txt`).
2. Green: added `SiblingPolicy` (25 % off the regular fee, 6 h → 5400) and one `POLICIES` entry.
   `make_invoice` was **not changed**. 10 tests pass (`sibling_green.txt`).

## Part D — Gherkin scenarios for our team story
Story **S11 Create a study group (AP-16)**, owner David Gerges: `team_story.feature` (3 scenarios:
create a group and get a code, group name required, two groups never share a code).

## Evidence in this folder
`coverage_100.png`, `behave_green.png`, `git-log.txt`, `tdd-run-log.txt` (real red/green output of every cycle) (one commit per TDD cycle), `smells.md` (Task C1),
`A1-answer.md`, `team_story.feature`.
