# FLA Task 2 — Finite Automata Validators

**Student:** Bakkola Lokesh  
**Register Number:** RA2411026050060  
**Course:** 21CSC301T — Formal Language and Automata  
**Institution:** SRM Institute of Science and Technology, Tiruchirappalli

## Aim

To implement deterministic finite automata (DFA)-based validators for mobile numbers, usernames, and 24-hour time values.

## Validation rules

1. **Mobile number:** exactly 10 ASCII digits; the first digit must be 6, 7, 8, or 9.
2. **Username:** must begin with an alphabetic character. Remaining characters may be letters, digits, or a single underscore between valid characters. Consecutive and trailing underscores are rejected.
3. **24-hour time:** must follow the exact `HH:MM` format. Hours range from 00 to 23 and minutes range from 00 to 59.

## Project structure

```text
finite_automata/
    validators.py
    dfa.py
    cli.py
tests/
    test_validators.py
validators.py
test_validators.py
docs/
    automata.md
tools/
    make_diagrams.py
```

## Run the program

Use Python 3.9 or later.

```bash
python validators.py
python -m finite_automata.cli all
python -m finite_automata.cli mobile 9123456780
python -m finite_automata.cli username lokesh25
python -m finite_automata.cli time 14:35
python -m unittest -v
```

## Sample test values

| Validator | Accepted | Rejected |
|---|---|---|
| Mobile | `9123456780` | `5123456789` |
| Username | `lokesh25` | `25lokesh` |
| Time | `14:35` | `25:10` |

The program prints ACCEPTED or REJECTED for each input. The test suite covers valid and invalid examples for all three validators.
