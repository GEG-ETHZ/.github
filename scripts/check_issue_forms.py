"""Check the default issue forms: every form sets an issue type, and Task is the default.

An issue without a type falls out of every board view that filters by type, so
every way of opening an issue in the web UI has to set one. Standard library
only, so CI needs nothing but Python.
"""

import re
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / ".github" / "ISSUE_TEMPLATE"
ISSUE_TYPES = {"Task", "Bug", "Feature", "Topic"}
DEFAULT_TYPE = "Task"
TYPE_LINE = re.compile(r"^type:\s*(\S+)\s*$", re.MULTILINE)
BLANK_ISSUES_OFF = re.compile(r"^blank_issues_enabled:\s*false\s*$", re.MULTILINE)


def forms() -> list[Path]:
    return sorted(path for path in TEMPLATES.glob("*.yml") if path.name != "config.yml")


def declared_type(path: Path) -> str | None:
    match = TYPE_LINE.search(path.read_text(encoding="utf-8"))
    return match.group(1).strip("\"'") if match else None


def problems() -> list[str]:
    found = forms()
    if not found:
        return [f"no issue forms in {TEMPLATES}"]
    errors = [
        f"{path.name} sets no known issue type" for path in found if declared_type(path) not in ISSUE_TYPES
    ]
    missing = ISSUE_TYPES - {declared_type(path) for path in found}
    if missing:
        errors.append(f"no form for: {', '.join(sorted(missing))}")
    if declared_type(found[0]) != DEFAULT_TYPE:
        errors.append(f"the first form offered must be {DEFAULT_TYPE}, not {found[0].name}")
    config = TEMPLATES / "config.yml"
    if not config.exists() or not BLANK_ISSUES_OFF.search(config.read_text(encoding="utf-8")):
        errors.append("config.yml must set blank_issues_enabled: false")
    return errors


def main() -> int:
    errors = problems()
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
