import os
import json
import re

# List of image file extensions to include
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')

def get_image_files(folder):
    """Get all image files in the given folder."""
    return [f for f in os.listdir(folder) if f.lower().endswith(IMAGE_EXTENSIONS)]

def update_html_file(folder_images):
    """Update the HTML file with the new folderImages object."""
    html_file = 'index.html'  # Assuming the HTML file is named index.html
    
    with open(html_file, 'r') as file:
        content = file.read()
    
    # Convert the folder_images dict to a JSON string
    folder_images_json = json.dumps(folder_images, indent=4)
    
    # Replace the existing folderImages object in the HTML file
    updated_content = re.sub(
        r'const folderImages = \{[^}]*\};',
        f'const folderImages = {folder_images_json};',
        content,
        flags=re.DOTALL
    )
    
    with open(html_file, 'w') as file:
        file.write(updated_content)

def main():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Initialize the folderImages object
    folder_images = {}
    
    # Iterate through all subdirectories
    for folder in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder)
        if os.path.isdir(folder_path):
            images = get_image_files(folder_path)
            if images:
                folder_images[folder] = images
    
    # Update the HTML file
    update_html_file(folder_images)
    
    print("HTML file updated successfully with current folder contents.")

if __name__ == "__main__":
    main()
