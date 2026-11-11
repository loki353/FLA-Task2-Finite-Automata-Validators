# Task 2 — Finite Automata Validators

**Author:** Lokesh Bakkola

## Overview
This project demonstrates DFA-based validation for PIN codes, passwords, and simplified email-like identifiers.

## Structure
```text
finite_automata/ (DFA interpreter, validators, CLI)
tests/ (pytest cases)
docs/ (DFA design notes and diagrams)
tools/ (diagram source generator)
```

## DFA model
A deterministic finite automaton is a 5-tuple (Q, Σ, δ, q0, F). It reads one symbol at a time, changes state through δ, and accepts if the final state belongs to F.

## Case studies
1. **PIN:** exactly four decimal digits.
2. **Password:** at least eight characters, with uppercase, lowercase, digit, and special character.
3. **Email-like identifier:** one `@`, non-empty local part, and a dotted domain with non-empty alphanumeric/hyphen labels. This is an educational simplified rule, not a full email-standard implementation.

## Run
```bash
python -m finite_automata.cli all
python -m finite_automata.cli pin 1234
python -m finite_automata.cli password Example@123
python -m finite_automata.cli email student@example.com
python -m pytest -q
python tools/make_diagrams.py
```

Python 3.9+; runtime code uses only the standard library. Pytest is needed for tests. The tool writes Graphviz DOT source.

## Why DFA?
Each validator needs only finite information about the prefix read so far (digit count or whether character classes have appeared). This information can be represented by finite states, so a DFA is sufficient.
