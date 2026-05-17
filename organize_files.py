import os
import shutil

# Directories to create
directories = ['frontend', 'backend', 'devops', 'other']
for d in directories:
    os.makedirs(d, exist_ok=True)

# File categories mapping
categories = {
    'Accessibility.md': 'frontend',
    'Angular.md': 'frontend',
    'BrowserCompatibility.md': 'frontend',
    'CSS3.md': 'frontend',
    'Core-javascript.md': 'frontend',
    'Cypress.md': 'frontend',
    'HTML.md': 'frontend',
    'Javascript.md': 'frontend',
    'Jest.md': 'frontend',
    'LESS.md': 'frontend',
    'Nextjs.md': 'frontend',
    'ReactArchiteture.md': 'frontend',
    'Reactjs.md': 'frontend',
    'Redux.md': 'frontend',
    'ResponsiveDesign.md': 'frontend',
    'SCSS.md': 'frontend',
    'TailwindCSS.md': 'frontend',
    'Typscript.md': 'frontend',
    'Vuejs.md': 'frontend',
    'WebPerformance.md': 'frontend',
    'Webpack.md': 'frontend',

    'Authentication.md': 'backend',
    'CSharp.md': 'backend',
    'DotNet.md': 'backend',
    'Hasura-GraphQL.md': 'backend',
    'MSSQL.md': 'backend',
    'MySQL.md': 'backend',
    'NodeJs.md': 'backend',
    'RestAPI.md': 'backend',

    'CICD.md': 'devops',
    'CloudPlatforms.md': 'devops',
    'Git.md': 'devops',

    'AgenticAI.md': 'other',
    'Agile.md': 'other',
    'Agent.md': 'other',
    'skills.md': 'other'
}

# Move files
for file in os.listdir('.'):
    if os.path.isfile(file):
        if file == 'README.md' or file == 'organize_files.py':
            continue
        
        # If it's a python script, put it in 'other'
        if file.endswith('.py'):
            dest = 'other'
        else:
            dest = categories.get(file, 'other')
            
        shutil.move(file, os.path.join(dest, file))
        print(f"Moved {file} to {dest}/")

# Update README.md
readme_path = 'README.md'
if os.path.exists(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update links in README.md based on new categories
    for filename, category in categories.items():
        old_link = f"(./{filename})"
        new_link = f"(./{category}/{filename})"
        content = content.replace(old_link, new_link)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Organization complete!")
