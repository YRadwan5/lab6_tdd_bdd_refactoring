# Part C — Legacy invoice analysis and SOLID refactoring

## Task C1: Code smells before refactoring

| Code smell | Where it appears | Principle / impact |
|---|---|---|
| Long conditional chain | `if/elif` branches checking `kind` | **OCP:** adding a student type requires editing the calculation function |
| Magic numbers | `1200`, `2000`, `5000`, and `0.5` | Readability and maintainability: business rules have no meaningful names |
| Multiple responsibilities | `make_invoice` calculates, formats, writes a file, prints, and returns | **SRP:** several unrelated reasons can cause the function to change |
| Manual file closing | `open`, `write`, then `close` | Resource safety: an exception can prevent the file from being closed; use a context manager |
| Repeated per-course calculation | Loops over courses and adds each course fee | Simpler design: fee policies can use the student's total credit hours |
| Hard-coded output dependency | Function opens a disk file directly | **DIP:** calculation is coupled to concrete file I/O and is harder to test |

## Characterization results

For a student with 6 credit hours:
- Regular: 6 × 1200 = 7200 EGP
- Scholarship: 6 × 1200 × 0.5 = 3600 EGP
- International: 6 × 2000 + 5000 = 17000 EGP

The tests in `tests/test_invoice_characterization.py` pin down these existing totals before changes to the design.

## Refactoring decisions

- Named constants replace unexplained numeric literals.
- `RegularPolicy`, `ScholarshipPolicy`, `InternationalPolicy`, and `SiblingPolicy` each own one fee rule (**SRP**).
- `POLICIES` maps a kind to its policy, so adding a new type does not require changing `make_invoice` (**OCP**).
- `FileWriter` owns disk output, and `make_invoice` accepts a writer dependency (**DIP**).
- A context manager safely closes the output file.
- Printing is removed from the calculation function; the caller decides how to display the invoice.

## Task C2: SiblingPolicy

Sibling students receive a 25% discount on the regular fee. The test expects 5400 EGP for 6 hours. The implementation adds `SiblingPolicy` and one entry to `POLICIES`; `make_invoice` is unchanged.
