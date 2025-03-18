import os
import shutil



def clean_public_folder():
    # Remove all files in the public folder
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")

def copy_folder_to_public(folder_name):
    # Copy the contents of the folder to inside the public folder
    if os.path.exists(folder_name):
        shutil.copytree(folder_name, "public/")