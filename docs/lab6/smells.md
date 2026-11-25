# Task C1 — Code smells in `legacy_invoice.py` (identified before refactoring)

| Code smell | Where it appears | Principle or issue |
|---|---|---|
| Long `if/elif` chain on `kind`, checked twice | Loop body and after the loop | OCP: adding a student type requires editing the function |
| Magic numbers: `1200`, `0.5`, `2000`, `5000` | Fee calculation chain | Readability: the meaning of each value is hidden |
| One function calculates fees, formats text, writes a file, and prints | Whole function | SRP: several independent reasons to change |
| File opened without a context manager and closed manually | `open(...)` and `f.close()` | Resource safety: the file may remain open if writing fails |
| Disk access and `print` are hard-wired into the function | Output section | DIP/testability: difficult to test without file I/O |
| Fee calculated per course even though only total hours matter | `for` loop | Unnecessary complexity and duplicated work |
| Unknown `kind` silently produces 0 EGP and still writes an invoice | Missing validation / `else` branch | Hidden bug: invalid input is not rejected |
