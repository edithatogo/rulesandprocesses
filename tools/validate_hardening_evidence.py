"""Check the machine-readable hardening risk register and workflow invariants."""

from __future__ import annotations

import json
from pathlib import Path


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    register = json.loads((root / "security/RISK_REGISTER.json").read_text(encoding="utf-8"))
    seen: set[str] = set()
    for risk in register.get("risks", []):
        if risk.get("id") in seen:
            errors.append(f"duplicate risk: {risk.get('id')}")
        seen.add(risk.get("id"))
        for field in ("severity", "threat", "asset", "mitigation", "verification", "disposition"):
            if not risk.get(field):
                errors.append(f"risk {risk.get('id')} missing {field}")
    for workflow in sorted((root / ".github/workflows").glob("*.yml")):
        text = workflow.read_text(encoding="utf-8")
        if "uses:" in text:
            for line in text.splitlines():
                if "uses:" in line and "@" in line and "#" in line:
                    ref = line.split("@", 1)[1].split()[0]
                    if len(ref) != 40:
                        errors.append(f"workflow action is not immutable: {workflow}:{line.strip()}")
    return errors


def main() -> int:
    root = Path(".")
    errors = validate(root)
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("OK: hardening evidence and workflow pins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
