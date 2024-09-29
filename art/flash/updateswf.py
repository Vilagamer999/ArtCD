import os
import re

def update_flash_gallery(directory, html_file):
    # Get all .swf files in the directory
    swf_files = [f for f in os.listdir(directory) if f.endswith('.swf')]
    
    # Create the JavaScript array entries
    js_array_entries = []
    for swf_file in swf_files:
        name = os.path.splitext(swf_file)[0].replace('_', ' ').title()
        js_array_entries.append(f'{{ name: "{name}", file: "{swf_file}" }}')
    
    # Join the entries into a JavaScript array
    js_array = '[\n        ' + ',\n        '.join(js_array_entries) + '\n    ]'
    
    # Read the HTML file
    with open(html_file, 'r') as file:
        content = file.read()
    
    # Replace the existing flashAnimations array
    pattern = r'const flashAnimations = \[[\s\S]*?\];'
    replacement = f'const flashAnimations = {js_array};'
    updated_content = re.sub(pattern, replacement, content)
    
    # Write the updated content back to the HTML file
    with open(html_file, 'w') as file:
        file.write(updated_content)
    
    print(f"Updated {html_file} with {len(swf_files)} Flash animations.")

# Usage
directory = '.'  # Current directory, change if your .swf files are elsewhere
html_file = 'index.html'  # Your main gallery HTML file

update_flash_gallery(directory, html_file)