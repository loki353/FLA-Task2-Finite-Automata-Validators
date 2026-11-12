from pathlib import Path

output = Path(__file__).resolve().parents[1] / "docs" / "diagrams"
output.mkdir(parents=True, exist_ok=True)

diagrams = {
    "mobile_dfa.dot": """digraph MobileDFA {
    rankdir=LR;
    node [shape=circle];
    start [shape=point];
    start -> q0;
    q10 [shape=doublecircle];
    q0 -> q1 [label="6,7,8,9"];
    q1 -> q2 [label="digit"];
    q2 -> q3 [label="digit"];
    q3 -> q4 [label="digit"];
    q4 -> q5 [label="digit"];
    q5 -> q6 [label="digit"];
    q6 -> q7 [label="digit"];
    q7 -> q8 [label="digit"];
    q8 -> q9 [label="digit"];
    q9 -> q10 [label="digit"];
}""",
    "username_dfa.dot": """digraph UsernameDFA {
    rankdir=LR;
    node [shape=circle];
    start [shape=point];
    start -> start_state;
    valid [shape=doublecircle];
    start_state -> valid [label="letter"];
    valid -> valid [label="letter or digit"];
    valid -> underscore [label="underscore"];
    underscore -> valid [label="letter or digit"];
    underscore [shape=circle];
}""",
    "time_dfa.dot": """digraph TimeDFA {
    rankdir=LR;
    node [shape=circle];
    start [shape=point];
    start -> h1;
    accept [shape=doublecircle];
    h1 -> h2 [label="valid hour digit"];
    h2 -> colon [label="valid hour pair"];
    colon -> m1 [label=":"];
    m1 -> m2 [label="minute tens 0-5"];
    m2 -> accept [label="minute units 0-9"];
}"""
}

for filename, source in diagrams.items():
    (output / filename).write_text(source, encoding="utf-8")

print("Generated mobile_dfa.dot, username_dfa.dot, and time_dfa.dot")
