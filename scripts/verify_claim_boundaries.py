#!/usr/bin/env python3
"""Keep the browser-only token and runtime-metric claims inside their evidence boundary."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = {
    "README.md": (
        "every interaction mints a DSSE-signed Khipu receipt",
        "All counts above are reproducible from `lutar-lean@main`",
    ),
    "index.html": (
        "you are receipt",
        "Signed receipts, minted across the mesh",
        "Your Khipu receipt was computed locally",
    ),
    "js/app.js": (
        "function chainIndex",
        "dataset.idx",
        "Khipu receipt for this visit",
    ),
    "js/receipts.js": (
        "Reed-Solomon parity protects the Khipu chain on disk",
        "signed Khipu receipts",
    ),
    "SECURITY.md": ("SZL release artifacts are signed with",),
}

REQUIRED = {
    "README.md": (
        "not signed, persisted, or appended to a Khipu receipt chain",
        "c7c0ba17c2eaec60ad38ea9172b4a0d9ca0b582f",
    ),
    "index.html": (
        "local visit token",
        "verify receipt signatures, append-only storage",
        "five public SZL Spaces",
        "chords are visual grouping only",
    ),
    "js/app.js": (
        "It is not a signature",
        "Ephemeral visit token",
    ),
    "js/receipts.js": (
        "service-reported counters",
        "signatures not verified here",
        "szl-constellation",
        "szl-frontier",
    ),
    "SECURITY.md": (
        "No signed release bundle is asserted",
        "An SBOM describes the scanned files",
    ),
}


def main() -> int:
    errors: list[str] = []
    for relative, phrases in FORBIDDEN.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase in text:
                errors.append(f"{relative}: forbidden overclaim remains: {phrase!r}")

    for relative, phrases in REQUIRED.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{relative}: required evidence boundary missing: {phrase!r}")

    if errors:
        print("claim-boundary verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("claim-boundary verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
