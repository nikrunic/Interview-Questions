"""Expand backend interview Q&A files to at least 100 questions."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "backend"


def format_qna(num, title, concept, details, example, ref_url, ref_title="Documentation"):
    details_md = "\n".join(f"- {d}" for d in details)
    return f"""### {num}. {title}
**Answer:** 
**The Core Concept:**
{concept}

**Key Details:**
{details_md}

**Example:** 
`{example}`

**Reference:** [{ref_title}]({ref_url})

---
"""


def strip_tail(content):
    """Remove placeholder notes and broken Additional Depth sections."""
    content = re.sub(r"\n\*\(Questions 51-100[^*]*\)\*\n", "\n", content)
    content = re.sub(r"\\n## Additional Depth \(Architectural Focus\)\\n[\s\S]*$", "", content)
    content = re.sub(r"\n## Additional Depth \(Architectural Focus\)\n[\s\S]*$", "", content)
    return content.rstrip() + "\n"


def next_num(content):
    matches = re.findall(r"^### (\d+)\.", content, re.MULTILINE)
    return max(int(m) for m in matches) + 1 if matches else 1


def append_questions(path, questions, start=None):
    content = strip_tail(path.read_text(encoding="utf-8"))
    n = start or next_num(content)
    block = "".join(
        format_qna(n + i, *q) for i, q in enumerate(questions)
    )
    path.write_text(content + block, encoding="utf-8")
    return n + len(questions) - 1


def main():
    from qna_auth_data import AUTH_EXTRA
    from qna_auth_data2 import AUTH_EXTRA_2
    from qna_rest_data import REST_EXTRA
    from qna_node_data import NODE_EXTRA
    from qna_hasura_data import HASURA_EXTRA

    auth_path = BACKEND / "Authentication.md"
    auth_content = strip_tail(auth_path.read_text(encoding="utf-8"))
    # Fix intro and remove stub Additional Depth; keep Q1–4
    auth_content = auth_content.replace(
        "This document contains interview questions focused on web security",
        "This document contains 100 interview questions focused on web security",
    )
    auth_path.write_text(auth_content, encoding="utf-8")
    end = append_questions(auth_path, AUTH_EXTRA + AUTH_EXTRA_2)
    print(f"Authentication.md: {end} questions")

    for name, extra in [
        ("RestAPI.md", REST_EXTRA),
        ("NodeJs.md", NODE_EXTRA),
        ("Hasura-GraphQL.md", HASURA_EXTRA),
    ]:
        path = BACKEND / name
        content = strip_tail(path.read_text(encoding="utf-8"))
        # Remove placeholder line if still present
        content = re.sub(r"\n\*\(Questions 51-100[^*]*\)\*\n", "\n", content)
        path.write_text(content, encoding="utf-8")
        end = append_questions(path, extra)
        intro = "51" if end == 100 else str(end)
        print(f"{name}: {end} questions")


if __name__ == "__main__":
    main()
