import os
import re
import subprocess
import concurrent.futures
from tqdm import tqdm

TIMEOUT = 60  # seconds

def upload_file(file_path):
    try:
        result = subprocess.run(['pyupload', file_path, '--host=catbox'], 
                                capture_output=True, text=True, timeout=TIMEOUT)
        if result.returncode == 0:
            link = result.stdout.strip().split('Your link : ')[-1]
            return link, None
        else:
            return None, result.stderr.strip()
    except subprocess.TimeoutExpired:
        return None, f"Upload timed out after {TIMEOUT} seconds"
    except Exception as e:
        return None, str(e)

def update_flash_gallery(directory, html_file):
    swf_files = [f for f in os.listdir(directory) if f.endswith('.swf')]
    js_array_entries = []
    failed_uploads = []
    
    with tqdm(total=len(swf_files), desc="Overall Progress") as pbar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_file = {executor.submit(upload_file, os.path.join(directory, swf_file)): swf_file for swf_file in swf_files}
            for future in concurrent.futures.as_completed(future_to_file):
                swf_file = future_to_file[future]
                try:
                    link, error = future.result()
                    if link:
                        name = os.path.splitext(swf_file)[0].replace('_', ' ').title()
                        js_array_entries.append(f'{{ name: "{name}", file: "{link}" }}')
                    else:
                        failed_uploads.append((swf_file, error))
                except Exception as exc:
                    failed_uploads.append((swf_file, str(exc)))
                pbar.update(1)
    
    js_array = '[\n        ' + ',\n        '.join(js_array_entries) + '\n    ]'
    
    with open(html_file, 'r') as file:
        content = file.read()
    
    pattern = r'const flashAnimations = \[[\s\S]*?\];'
    replacement = f'const flashAnimations = {js_array};'
    updated_content = re.sub(pattern, replacement, content)
    
    with open(html_file, 'w') as file:
        file.write(updated_content)
    
    print(f"\nUpdated {html_file} with {len(js_array_entries)} uploaded Flash animations.")
    
    if failed_uploads:
        print("\nFailed uploads:")
        for file, error in failed_uploads:
            print(f"- {file}: {error}")

# Usage
directory = '.'  # Current directory, change if your .swf files are elsewhere
html_file = 'index.html'  # Your main gallery HTML file

update_flash_gallery(directory, html_file)