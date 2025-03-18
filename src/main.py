from textnode import *
from htmlnode import *

from filemanagement import *

def main():
    
    print("Cleaning public folder")
    clean_public_folder()

    print("\nCopying folders in static to public folder")
    copy_folder_to_public("static")



main()