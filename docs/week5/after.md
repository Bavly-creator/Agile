# Week 5 — Before / After and pairing reflection

**Team 7 — FocusPulse**

## Before / after table

| Measure | Before (`legacy_fees.py`) | After (`fees.py`) |
|---------|---------------------------|-------------------|
| Ruff issues (total) | 17 (the handout says 16; newer Ruff adds PLR0917) | 0 (`ruff check . --exclude legacy_fees.py`: All checks passed!) |
| Highest cyclomatic complexity | 9 (`calc`) | 3 (`tuition_fee`, `fee_report`) |
| Arguments of the main function | 6 | 5 (`courses, student_type, summer, discount, extras`) |
| Pylint score (/10) | 4.86 | 10.00 |
| Tests passing | 0 (no tests) | 10 in `test_fees.py` (`pytest -v`); 20 with `test_grades.py` |

The characterization tests compare the old `calc` and the new `tuition_fee` on four inputs and all agree. The last test, `test_scholarship_student_is_not_skipped`, fails on the legacy logic and passes after step 7, which fixed the hidden bug.

## Refactoring steps (one commit each)

1. Delete unused imports, variable `tmp` and argument `y`.
2. Rename `calc` → `tuition_fee`, `d` → `courses`, `s` → `summer`, `ProcessAll` → `process_all`.
3. Replace magic numbers with constants and the type codes 1/2/3 with the `StudentType` Enum.
4. Replace the if/elif chain with a rate table (`RATE_SHARE`), use `if summer:` and a discount default of 0.
5. Immutable default `extras=()` and a `Course` dataclass instead of `{"h": ...}`.
6. Separate calculation from printing: `fee_report` returns text.
7. Fix the hidden bug: `process_all` gives every student a fee (scholarship students pay 0).

## Pairing reflection

Working as driver and navigator made us slow down and explain each change out loud, and the navigator spotted naming and boundary-case problems that the driver had not seen while typing. Writing the characterization tests before refactoring gave us confidence, because each small step was checked immediately by `pytest`, and Ruff and Pylint showed the smells as numbers instead of opinions. The linters found the patterns but not the hidden bug in `ProcessAll`; we only understood it by reading the code and the tests. Next time we would switch roles on a timer from the beginning and commit smaller steps.
