from textnode import *
from htmlnode import *

from file_management import *

from generate_page import *

import sys

def main():
     
    ##### CLEANING AND REGENERATING PUBLIC FOLDER #####
    print("Cleaning docs folder")
    clean_public_folder("docs")

    print("\nCopying folders in static to docs folder")
    copy_folder_to_public("static", "docs")


    ##### GENERATING PAGES #####
    print("\nGenerating pages")

    basepath = '/'
    if sys.argv[0] is not None:
        basepath = sys.argv[0]

    #generate_page("content/index.md", "./template.html", "public/index.html")
    #generate_pages_recursive("content", "./template.html", "public", basepath)
    generate_pages_recursive("content", "./template.html", "docs", basepath)

main()