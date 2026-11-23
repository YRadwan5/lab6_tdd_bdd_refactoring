# Lab 6 — TDD, BDD & Refactoring

This project follows the uploaded Lab 6 handout. It contains the course-registration TDD kata, Gherkin/Behave scenarios, invoice characterization tests and SOLID refactoring, and three scenarios for a QR attendance project.

## Requirements

Python 3.10 or newer.

## Windows setup (PowerShell)

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest pytest-cov behave ruff
```

## Run the tests and tools

Run these commands from the `lab6` project root:

```powershell
python -m pytest -v
python -m pytest --cov=registration --cov-report=term-missing
python -m behave
python -m ruff check .
```

The handout's coverage target concerns `registration.py`. The fifth registration test covers dropping a course that was never registered. The additional invalid-hours test is extra defensive validation.

## Files

- `registration.py`: course registration model
- `tests/test_registration.py`: registration tests
- `features/registration.feature`: registration acceptance criteria, including drop
- `features/steps/registration_steps.py`: Behave step definitions
- `invoice.py`: refactored invoice policies and injected writer
- `tests/test_invoice_characterization.py`: legacy totals, fake writer, and sibling discount
- `docs/lab6/`: written answers, code-smell analysis, and QR attendance scenarios

## Important submission steps

The handout requires a real Git log with one commit per TDD Red–Green–Refactor cycle, plus a screenshot of the 100% coverage report and all-green Behave output. Those are generated from your own local workflow; they are not fabricated in this ZIP.

Suggested sequence while demonstrating the TDD process:
1. Commit the first registration test before implementing the behaviour.
2. Implement the smallest change that makes it pass; refactor and commit.
3. Repeat for the 18-hour limit, duplicate prevention, dropping a course, and dropping an unregistered course.
4. Run coverage and capture the terminal showing the report.
5. Run Behave and capture the all-green output.
6. Push the project, Git log, and screenshots to your repository under the requested `docs/lab6/` location.
