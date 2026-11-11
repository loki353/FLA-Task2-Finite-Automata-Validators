from pathlib import Path
out = Path(__file__).resolve().parents[1] / 'docs' / 'diagrams'
out.mkdir(parents=True, exist_ok=True)
dot = '''digraph PIN_DFA {
 rankdir=LR; node [shape=circle]; start [shape=point]; start -> q0;
 q4 [shape=doublecircle]; q0 -> q1 [label="digit"];
 q1 -> q2 [label="digit"]; q2 -> q3 [label="digit"]; q3 -> q4 [label="digit"];
}'''
(out / 'pin_dfa.dot').write_text(dot, encoding='utf-8')
print('Wrote docs/diagrams/pin_dfa.dot')
