import os
import re

# Supported image file extensions
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

def get_image_files(directory):
    """Get all image files in the given directory."""
    return [f for f in os.listdir(directory) if f.lower().endswith(IMAGE_EXTENSIONS)]

def update_folder_images(html_file):
    # Read the HTML file
    with open(html_file, 'r') as file:
        content = file.read()

    # Find the folderImages object in the HTML
    folder_images_match = re.search(r'const folderImages = \{([^}]*)\};', content, re.DOTALL)
    if not folder_images_match:
        print("Couldn't find folderImages object in the HTML file.")
        return

    # Get the current directory (where the HTML file is located)
    base_dir = os.path.dirname(os.path.abspath(html_file))

    # Create a new folderImages object
    new_folder_images = {}

    # Traverse the directory structure
    for root, dirs, files in os.walk(base_dir):
        rel_path = os.path.relpath(root, base_dir)
        if rel_path == '.':
            rel_path = ''
        
        # Get image files in the current directory
        image_files = get_image_files(root)
        
        if image_files:
            folder_key = rel_path.replace('\\', '/')
            new_folder_images[folder_key] = image_files

    # Convert the new_folder_images dictionary to a string representation
    new_folder_images_str = "const folderImages = {\n"
    for folder, images in new_folder_images.items():
        new_folder_images_str += f'    "{folder}": {images},\n'
    new_folder_images_str += "};"

    # Replace the old folderImages object with the new one
    updated_content = re.sub(
        r'const folderImages = \{[^}]*\};',
        new_folder_images_str,
        content,
        flags=re.DOTALL
    )

    # Write the updated content back to the HTML file
    with open(html_file, 'w') as file:
        file.write(updated_content)

    print("HTML file updated successfully with new folderImages object.")

# Usage
html_file_path = 'index.html'  # Replace with your HTML file name
update_folder_images(html_file_path)