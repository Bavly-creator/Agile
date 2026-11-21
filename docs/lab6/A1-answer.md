# Task A1 — Coverage

Report (`python -m pytest --cov=registration --cov-report=term-missing`):

| Name | Stmts | Miss | Cover |
|---|---|---|---|
| registration.py | 20 | 0 | 100% |

Screenshot: `coverage_100.svg` (same folder).

**Does 100% coverage prove the code is correct?**
No. 100% only means every line was executed by some test. It does not prove that the tests check the right
behaviour or that every input is covered (for example, negative hours are never tested).
