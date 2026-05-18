"""Merge JS and React interview files into unified guides."""
from pathlib import Path

FRONTEND = Path(__file__).resolve().parent.parent / "frontend"


def strip_title(content: str, skip_lines: int = 0) -> str:
    lines = content.splitlines()
    # Skip initial # title and blank lines after it
    i = 0
    if lines and lines[0].startswith("# "):
        i = 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    i += skip_lines
    return "\n".join(lines[i:]).strip()


def merge_javascript():
    prep = (FRONTEND / "Javascript-Interview-Prep.md").read_text(encoding="utf-8")
    main = (FRONTEND / "Javascript.md").read_text(encoding="utf-8")
    core = (FRONTEND / "Core-javascript.md").read_text(encoding="utf-8")

    doc = f"""# JavaScript — Complete Interview Guide

This file combines three JavaScript resources into one place:

| Part | Content | Former file |
|------|---------|-------------|
| **1** | Interview preparation (concepts, links, tables) | `Javascript-Interview-Prep.md` |
| **2** | 100 interview Q&A (Basic / Medium / Hard) | `Javascript.md` |
| **3** | Core language deep dive Q&A | `Core-javascript.md` |

**Also see:** [JS Practical](./js-practical.md) — runnable snippets with step-by-step outputs.

---

## Table of contents

- [Part 1 — Interview preparation](#part-1--interview-preparation)
- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)
- [Part 3 — Core JavaScript deep dive](#part-3--core-javascript-deep-dive)

---

# Part 1 — Interview preparation

{strip_title(prep)}

---

# Part 2 — Interview questions (100)

{strip_title(main)}

---

# Part 3 — Core JavaScript deep dive

{strip_title(core)}
"""
    out = FRONTEND / "Javascript.md"
    out.write_text(doc, encoding="utf-8")
    print(f"Wrote {out} ({len(doc.splitlines())} lines)")


def merge_react():
    prep = (FRONTEND / "React-Interview-Prep.md").read_text(encoding="utf-8")
    main = (FRONTEND / "Reactjs.md").read_text(encoding="utf-8")

    doc = f"""# React.js — Complete Interview Guide

This file combines two React resources into one place:

| Part | Content | Former file |
|------|---------|-------------|
| **1** | Interview preparation (concepts, links, tables) | `React-Interview-Prep.md` |
| **2** | 100 interview Q&A (Basic / Medium / Hard) | `Reactjs.md` |

**Related (kept separate):**

- [React Architecture](./ReactArchiteture.md) — patterns, scaling, structure (100 Q&A)
- [Redux & State Management](./Redux.md) — Redux-specific Q&A

---

## Table of contents

- [Part 1 — Interview preparation](#part-1--interview-preparation)
- [Part 2 — Interview questions (100)](#part-2--interview-questions-100)

---

# Part 1 — Interview preparation

{strip_title(prep)}

---

# Part 2 — Interview questions (100)

{strip_title(main)}
"""
    out = FRONTEND / "Reactjs.md"
    out.write_text(doc, encoding="utf-8")
    print(f"Wrote {out} ({len(doc.splitlines())} lines)")


if __name__ == "__main__":
    merge_javascript()
    merge_react()
