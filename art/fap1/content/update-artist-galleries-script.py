import os
import re
from bs4 import BeautifulSoup

def is_artist_gallery(soup):
    # Check if it's an artist gallery by looking for specific elements
    return soup.find('script', text=re.compile('SetArtDirectory')) is not None

def is_already_updated(soup):
    # Check if the file has already been updated
    return soup.find('meta', attrs={'name': 'viewport'}) is not None

def extract_artist_info(soup):
    # Extract title and header
    title = soup.title.string if soup.title else "Artist Gallery"
    header = soup.find('h1')
    header_text = header.string if header else title

    # Extract SetArtDirectory and AddArt calls
    script_content = soup.find('script', text=re.compile('SetArtDirectory'))
    script_text = script_content.string if script_content else ""

    return title, header_text, script_text

def update_artist_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(content, 'html.parser')

    # Check if it's an artist gallery and not already updated
    if not is_artist_gallery(soup):
        print(f"Skipping: {file_path} (not an artist gallery)")
        return
    if is_already_updated(soup):
        print(f"Skipping: {file_path} (already updated)")
        return

    # Extract artist information
    title, header_text, script_text = extract_artist_info(soup)

    # Create the new HTML structure
    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
    <script src="gallery.js"></script>
</head>
<body>
    <div class="container">
        <header>
            <h1>{header_text}</h1>
        </header>

        <div id="iconrow"></div>

        <div id="nav">
            <img id="prevButton" src="img/prevoff.png" alt="Previous" onclick="DoPrev()">
            <img id="zoomButton" src="img/full.png" alt="Full Size" onclick="openFullImage(ImgShown)">
            <img id="nextButton" src="img/next.png" alt="Next" onclick="DoNext()">
        </div>

        <div id="disp" role="main"></div>
    </div>

    <script>
        {script_text}

        // Initialize the gallery
        document.addEventListener("DOMContentLoaded", Init);
    </script>
</body>
</html>
"""

    # Write the new HTML back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_html)

    print(f"Updated: {file_path}")

def main():
    # Directory containing the HTML files
    directory = '.'  # Current directory, change if needed

    # Process all HTML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.html') and filename != 'index.html':
            file_path = os.path.join(directory, filename)
            update_artist_html(file_path)

if __name__ == "__main__":
    main()