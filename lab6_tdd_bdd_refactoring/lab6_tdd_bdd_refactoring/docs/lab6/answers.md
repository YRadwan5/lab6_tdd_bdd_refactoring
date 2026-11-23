# Lab 6 — Written answers

## Task A1: Does 100% coverage prove the code is correct?

No. 100% coverage only means every measured statement or line was executed by the tests; it does not prove that the tests check every requirement or that the program has no defects.

## Task B1: Drop-course behaviour

The `Drop a registered course` scenario is in `features/registration.feature`. Its `@when` step is implemented in `features/steps/registration_steps.py`. The step calls `Student.drop` and captures a `RegistrationError` if the course is not registered.

## Task C1: Code smells

See `smells-and-refactoring.md` for the completed table with more than four smells and their locations and impacts.

## Task C2: Sibling discount

`SiblingPolicy` applies a 25% discount to the regular fee. For 6 credit hours, the result is 6 × 1200 × 0.75 = 5400 EGP. The policy is registered in `POLICIES`; `make_invoice` does not need a change.

## Part D: Team project

The three QR attendance scenarios are in `project-scenarios.feature`: valid QR success, invalid QR rejection, and duplicate-scan prevention.
