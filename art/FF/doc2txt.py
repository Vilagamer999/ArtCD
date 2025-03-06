import os
import subprocess
import docx2txt
from googletrans import Translator

def doc_to_txt(input_file, output_file, translate=False):
    _, file_extension = os.path.splitext(input_file)
    
    if file_extension.lower() == '.doc':
        # Use textutil for .doc files on macOS
        try:
            subprocess.run(['textutil', '-convert', 'txt', '-output', output_file, input_file], check=True)
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file}: {str(e)}")
            return
    elif file_extension.lower() == '.docx':
        # Use docx2txt for .docx files
        content = docx2txt.process(input_file)
    else:
        print(f"Unsupported file format for {input_file}. Please use .doc or .docx files.")
        return

    if translate:
        translator = Translator()
        try:
            translated = translator.translate(content, src='ja', dest='en')
            content = translated.text
        except Exception as e:
            print(f"Error translating {input_file}: {str(e)}")
            print("Saving original Japanese text without translation.")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Converted and {'translated ' if translate else ''}saved: {os.path.basename(output_file)}")

def batch_convert(input_folder, output_folder, translate=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.doc', '.docx')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
            doc_to_txt(input_path, output_path, translate)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = script_dir
    output_folder = os.path.join(script_dir, 'converted_txt_files')
    
    translate = input("Do you want to translate the text to English? (y/n): ").lower() == 'y'
    
    batch_convert(input_folder, output_folder, translate)