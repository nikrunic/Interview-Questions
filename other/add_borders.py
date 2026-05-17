import os

skip_files = ['README.md', 'Agent.md']

def add_borders():
    for filename in os.listdir('.'):
        if filename.endswith('.md') and filename not in skip_files:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
            
            new_lines = []
            for i, line in enumerate(lines):
                new_lines.append(line)
                if line.startswith('**Reference:**'):
                    # Check if there is already a border ahead
                    already_has_hr = False
                    for j in range(i + 1, min(i + 5, len(lines))):
                        if lines[j].strip() == '---':
                            already_has_hr = True
                            break
                        if lines[j].strip().startswith('###') or lines[j].strip().startswith('##'):
                            break
                            
                    if not already_has_hr:
                        # Append the space and border
                        new_lines.append('')
                        new_lines.append('---')
                        
            # Write back
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
                
if __name__ == '__main__':
    add_borders()
    print("Borders added to all Q&A files.")
