# Task A1 — Test Coverage

Run from the `lab6/` directory:

```bash
python -m pytest tests --cov=registration --cov-report=term-missing
```

Verified result from the Bavly implementation:

| Name | Stmts | Miss | Cover |
|---|---:|---:|---:|
| registration.py | 20 | 0 | 100% |
| TOTAL | 20 | 0 | 100% |

**Does 100% coverage prove the code is correct?** No. It only means every executable line was run by the tests; it does not prove that the tests check the correct behaviour or cover every possible input.

**Screenshot evidence:** Save a genuine terminal screenshot showing the command and its 100% coverage result as `docs/lab6/coverage-100-percent.png`. Do not use the old recreated SVG as a terminal screenshot.
