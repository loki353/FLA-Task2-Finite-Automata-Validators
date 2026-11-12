# DFA Design Notes — FLA Task 2

## 1. Mobile Number Validator

The DFA checks exactly ten ASCII digits. The first digit must be 6, 7, 8, or 9. The initial state moves to the first-digit state only for one of these four symbols. Each following digit advances the count. The state reached after the tenth digit is accepting. Any non-digit, invalid first digit, or extra digit is rejected.

## 2. Username Validator

The first input symbol must be an alphabetic character. After the first character, the automaton permits letters and digits. An underscore is permitted only when it is not repeated and is followed by another valid character. Therefore, leading, consecutive, and trailing underscores are rejected.

## 3. 24-Hour Time Validator

The input must contain exactly five characters in the form HH:MM. The third character must be a colon. The hour must be between 00 and 23, and the minute must be between 00 and 59. Inputs with missing digits, extra characters, or out-of-range values are rejected.

## DFA Suitability

Each validator needs only a finite amount of information about the input read so far, such as the digit position, previous username character category, or hour/minute range. These conditions can be represented by a finite number of states, so finite automata are suitable for the task.
