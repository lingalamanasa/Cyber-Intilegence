import os
import glob

html_files = glob.glob('c:/Users/manu1/OneDrive/Desktop/Cyber Intiligence/*.html')

for file in html_files:
    if file.endswith('error.html'):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all remaining error.html hrefs with #
    new_content = content.replace('href="error.html"', 'href="#"')
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
