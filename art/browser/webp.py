import os
import shutil
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def process_file(src_file, dest_file):
    # Check if the file is an image
    if src_file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Convert image to WebP
        try:
            with Image.open(src_file) as img:
                webp_file = os.path.splitext(dest_file)[0] + '.webp'
                img.save(webp_file, 'WEBP', quality=50, method=6)  # method=6 is the highest effort
        except Exception as e:
            print(f"Error converting {src_file}: {e}")
    else:
        # Copy non-image files
        shutil.copy2(src_file, dest_file)

def copy_and_convert(source_dir, dest_dir):
    tasks = []
    
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directory in destination
        relative_path = os.path.relpath(root, source_dir)
        dest_path = os.path.join(dest_dir, relative_path)
        os.makedirs(dest_path, exist_ok=True)
        
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)
            tasks.append((src_file, dest_file))
    
    # Use ThreadPoolExecutor with maximum number of threads
    max_workers = os.cpu_count()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_file = {executor.submit(process_file, src, dest): src for src, dest in tasks}
        
        # Create progress bar
        with tqdm(total=len(tasks), desc="Processing files") as pbar:
            for future in as_completed(future_to_file):
                pbar.update(1)

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a new directory for the copied and converted files
    new_dir = os.path.join(script_dir, "converted_files")
    os.makedirs(new_dir, exist_ok=True)
    
    print(f"Using {os.cpu_count()} CPU cores for processing.")
    
    # Run the copy and convert function
    copy_and_convert(script_dir, new_dir)
    
    print(f"Files have been copied and images converted to WebP in: {new_dir}")