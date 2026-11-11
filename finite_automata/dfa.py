from dataclasses import dataclass
from typing import FrozenSet, Mapping, Tuple

@dataclass(frozen=True)
class DFA:
    states: FrozenSet[str]
    alphabet: FrozenSet[str]
    transitions: Mapping[Tuple[str, str], str]
    start: str
    accepting: FrozenSet[str]

    def accepts(self, value: str) -> bool:
        state = self.start
        for symbol in value:
            if symbol not in self.alphabet:
                return False
            state = self.transitions.get((state, symbol))
            if state is None:
                return False
        return state in self.accepting
