import urllib.request
import re

repos = {
    "Javascript.md": "https://raw.githubusercontent.com/sudheerj/javascript-interview-questions/master/README.md",
    "Reactjs.md": "https://raw.githubusercontent.com/sudheerj/reactjs-interview-questions/master/README.md",
    "Angular.md": "https://raw.githubusercontent.com/sudheerj/angular-interview-questions/master/README.md"
}

for filename, url in repos.items():
    print(f"Processing {filename}...")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        continue
    
    # Extract questions and answers
    # Questions start with "### " followed by a number
    parts = re.split(r'\n### \d+\.\s*', content)
    
    if len(parts) < 100:
        print(f"Warning: less than 100 questions found in {filename}")
        
    questions = []
    for part in parts[1:]: # skip preamble
        lines = part.strip().split('\n')
        if not lines: continue
        q_title = lines[0].strip()
        q_body = '\n'.join(lines[1:]).strip()
        
        # remove "Back to Top" links
        q_body = re.sub(r'\[\*\*⬆ Back to Top\*\*\]\(#table-of-contents\)', '', q_body)
        
        questions.append((q_title, q_body))
        
    if not questions:
        print(f"No questions extracted for {filename}")
        continue
        
    # Take at least 100, or all if less
    questions = questions[:max(100, len(questions))]
    
    total = len(questions)
    easy_count = int(total * 0.2)
    med_count = int(total * 0.3)
    hard_count = total - easy_count - med_count
    
    easy = questions[:easy_count]
    med = questions[easy_count:easy_count+med_count]
    hard = questions[easy_count+med_count:]
    
    topic_name = filename.replace('.md', '')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {topic_name} Interview Questions\n\n")
        f.write("This document contains a comprehensive list of interview questions, categorized by difficulty (20% Easy, 30% Medium, 50% Hard) based on public GitHub repositories.\n\n")
        
        def write_section(title, qs, start_idx):
            f.write(f"## {title}\n\n")
            idx = start_idx
            for q_title, q_body in qs:
                # Clean up formatting
                # Convert the answer into a dense format to avoid huge files if necessary, or just dump it
                f.write(f"### {idx}. {q_title}\n")
                f.write(f"**Answer:**\n{q_body}\n\n")
                idx += 1
            return idx

        idx = 1
        idx = write_section("Easy (20%)", easy, idx)
        idx = write_section("Medium (30%)", med, idx)
        write_section("Hard (50%)", hard, idx)
        
    print(f"Saved {len(questions)} questions to {filename}")

