from block import markdown_to_html_node
from htmlnode import *

import os

def extract_title(markdown): 
    lines = markdown.splitlines()  # Split the markdown into lines
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line.startswith("# "):  # Check if the line starts with a single '#'
            return line[2:].strip()  # Remove '# ' and strip any extra whitespace
    raise Exception("No H1 header found")  # Raise an exception if no H1 header is found

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path, "r") as file:
        markdown = file.read()
    
    # Read the template file at template_path and store the contents in a variable.
    with open(template_path, "r") as file:
        template = file.read()

    markdown_in_html = markdown_to_html_node(markdown).to_html()  # Convert the markdown to HTML
    
    title = extract_title(markdown)  # Extract the title from the markdown

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_in_html)

    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    with open(dest_path, "w") as file:
        file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Get a list of all files and directories in the content directory
    files = os.listdir(dir_path_content)
    # Iterate over each file or directory in the content directory
    for file in files:
        # Get the full path of the file or directory
        full_path = os.path.join(dir_path_content, file)
        # If the full path is a directory, call generate_pages_recursive with the directory
        if os.path.isdir(full_path):
            # Create the corresponding subdirectory in the destination directory
            sub_dest_dir = os.path.join(dest_dir_path, file)
            os.makedirs(sub_dest_dir, exist_ok=True)
            generate_pages_recursive(full_path, template_path, sub_dest_dir)
        # If the full path is a file, generate the page
        elif os.path.isfile(full_path):
            # Generate the page using the file as the markdown source and the file name as the destination
            generate_page(full_path, template_path, os.path.join(dest_dir_path, file.replace(".md", ".html")))