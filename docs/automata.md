# DFA design notes

## PIN
States q0 through q4 record how many digits have been read. Each digit advances one state; q4 alone is accepting. Extra digits have no transition and are rejected.

## Password
The finite-state representation tracks whether the length has reached eight and whether uppercase, lowercase, digit, and special-character classes have appeared. Acceptance requires every condition.

## Email-like identifier
The simplified rule checks exactly one at-sign, a non-empty local part, and a dotted domain with non-empty alphanumeric/hyphen labels. It is not a complete implementation of email standards.

## DFA suitability
All required information is finite and can be encoded in a finite state. DFA validators are therefore suitable for these examples.
