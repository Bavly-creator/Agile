# Task A1 — Test Coverage

Run from the `lab6/` directory:

```bash
python -m pytest tests --cov=registration --cov-report=term-missing
```

Verified result from the submitted implementation:

| Name | Stmts | Miss | Cover |
|---|---:|---:|---:|
| registration.py | 20 | 0 | 100% |
| TOTAL | 20 | 0 | 100% |

**Does 100% coverage prove the code is correct?** No. It only means every executable line was run by the tests; it does not prove that the tests check the correct behaviour or cover every possible input.

**Screenshot evidence:** The original `coverage_100.png` screenshot is not currently in this repository. It is intentionally left pending at `docs/lab6/evidence/coverage_100.png`; add the genuine screenshot there when available. The text verification in `docs/lab6/evidence/pytest-coverage-verified.txt` is not a substitute for a screenshot.
