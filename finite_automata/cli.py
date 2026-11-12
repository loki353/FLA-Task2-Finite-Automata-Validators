import sys
from .validators import validate


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] == "all":
        examples = [
            ("mobile", "9123456780"),
            ("mobile", "5123456789"),
            ("username", "lokesh25"),
            ("username", "25lokesh"),
            ("time", "14:35"),
            ("time", "25:10")
        ]
        for kind, value in examples:
            result = "ACCEPTED" if validate(kind, value) else "REJECTED"
            print(f"{kind}: {value!r} -> {result}")
        return 0
    if len(args) != 2 or args[0] not in {"mobile", "username", "time"}:
        print("Usage: python -m finite_automata.cli [all|mobile VALUE|username VALUE|time VALUE]")
        return 2
    print("ACCEPTED" if validate(args[0], args[1]) else "REJECTED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
