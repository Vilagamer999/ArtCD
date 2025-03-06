import os
import json

def get_file_structure(directory):
    file_structure = {}
    ignored_files = {'.DS_Store', 'folder.webp', 'file.webp'}
    ignored_extensions = ('.py', '.html')
    
    for root, dirs, files in os.walk(directory):
        current_level = file_structure
        path_parts = os.path.relpath(root, directory).split(os.sep)
        for part in path_parts:
            if part == '.':
                continue
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
        
        # Sort directories case-insensitively
        dirs.sort(key=str.lower)
        
        # Add directories first
        for dir in dirs:
            current_level[dir] = {}
        
        # Sort files case-insensitively
        sorted_files = sorted(files, key=str.lower)
        
        # Add files
        for file in sorted_files:
            if file in ignored_files or file.endswith(ignored_extensions):
                continue
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory).replace('\\', '/')
            current_level[file] = relative_path
    
    return file_structure

def update_html_file(file_structure):
    with open('index.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Replace fileStructure
    start_index = html_content.find('const fileStructure = ')
    end_index = html_content.find('};', start_index) + 2
    updated_html = (
        html_content[:start_index] +
        f"const fileStructure = {json.dumps(file_structure, indent=4)};" +
        html_content[end_index:]
    )

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(updated_html)

if __name__ == "__main__":
    current_directory = os.getcwd()
    file_structure = get_file_structure(current_directory)
    update_html_file(file_structure)
    print("File explorer HTML has been updated with the current directory structure.")