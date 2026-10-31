# QualityForge AI - Flaky Test Policy

## Objective
Identify, track, and investigate inconsistent test results.

## Definition
A flaky test passes and fails intermittently without relevant
changes to application or test code.

## Policy
1. Record every initial test failure.
2. Allow a maximum of one retry for diagnosis.
3. Never hide the initial failure when a retry passes.
4. Track flaky tests separately.
5. Investigate root causes such as timing, network instability,
   test data, and environment issues.
6. Fix or quarantine confirmed flaky tests with documented reasons.

## Reporting
Reports must distinguish:
- Passed tests
- Failed tests
- Retried tests
- Flaky tests

## Principle
A retry pass does not automatically mean the test is healthy.