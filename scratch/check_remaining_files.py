import os
import re

directories = ["frontend", "backend"]
markdown_files = []

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))

print(f"Found {len(markdown_files)} markdown files in frontend and backend.")

for filepath in sorted(markdown_files):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Check for basic/intermediate/expert or basic/medium/hard or similar headings
    headings = re.findall(r"^##\s+(.*)$", content, re.MULTILINE)
    
    # Let's count questions
    questions = re.findall(r"^###\s+\d+\.", content, re.MULTILINE)
    
    print(f"\nFile: {filepath} (Questions count: {len(questions)})")
    if headings:
        print("  Headings:")
        for h in headings[:10]:
            print(f"    - {h}")
        if len(headings) > 10:
            print(f"    ... and {len(headings) - 10} more headings")
    else:
        print("  No H2 headings found.")
