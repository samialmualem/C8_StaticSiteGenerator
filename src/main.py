from textnode import *
from htmlnode import *

from file_management import *

from generate_page import *

def main():
    
    print("Cleaning public folder")
    clean_public_folder()

    print("\nCopying folders in static to public folder")
    copy_folder_to_public("static")

    print("\nGenerating pages")
    #generate_page("content/index.md", "./template.html", "public/index.html")
    generate_pages_recursive("content", "./template.html", "public")

main()