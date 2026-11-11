import sys
from .validators import validate

def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] == 'all':
        for kind, value in [('pin','1234'),('pin','12a4'),('password','Example@123'),('email','student@example.com')]:
            print(f'{kind}: {value!r} -> {validate(kind,value)}')
        return 0
    if len(args) != 2 or args[0] not in {'pin','password','email'}:
        print('Usage: python -m finite_automata.cli [all|pin VALUE|password VALUE|email VALUE]')
        return 2
    print('ACCEPT' if validate(args[0],args[1]) else 'REJECT')
    return 0

if __name__ == '__main__': raise SystemExit(main())
