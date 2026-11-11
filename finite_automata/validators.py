from .dfa import DFA

def pin_dfa():
    states = frozenset('q0 q1 q2 q3 q4'.split())
    transitions = {(f'q{i}', d): f'q{i+1}' for i in range(4) for d in '0123456789'}
    return DFA(states, frozenset('0123456789'), transitions, 'q0', frozenset({'q4'}))

def password_valid(value):
    return len(value) >= 8 and any(c.isupper() for c in value) and any(c.islower() for c in value) and any(c.isdigit() for c in value) and any(not c.isalnum() and not c.isspace() for c in value)

def email_like_valid(value):
    if any(c.isspace() for c in value) or value.count('@') != 1:
        return False
    local, domain = value.split('@')
    labels = domain.split('.')
    return bool(local) and len(labels) >= 2 and all(labels) and all(all(c.isalnum() or c == '-' for c in label) for label in labels)

def validate(kind, value):
    if kind == 'pin': return pin_dfa().accepts(value)
    if kind == 'password': return password_valid(value)
    if kind == 'email': return email_like_valid(value)
    raise ValueError('kind must be pin, password, or email')
