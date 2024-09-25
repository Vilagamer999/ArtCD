import os
import re
import chardet

def rename_htm_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.htm'):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, file[:-3] + 'html')
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    return chardet.detect(raw_data)['encoding']

def update_href_tags(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    encoding = detect_encoding(file_path)
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    
                    updated_content = re.sub(r'href=["\'](.+?)\.htm["\']', r'href="\1.html"', content)
                    
                    if content != updated_content:
                        with open(file_path, 'w', encoding=encoding) as f:
                            f.write(updated_content)
                        print(f"Updated href tags in: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")

def main():
    directory = input("Enter the directory path: ")
    
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return
    
    rename_htm_files(directory)
    update_href_tags(directory)
    print("Process completed.")

if __name__ == "__main__":
    main()