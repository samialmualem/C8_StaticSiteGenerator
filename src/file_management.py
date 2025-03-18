import os
import shutil



def clean_public_folder():
    # Remove all files in the public folder
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")

def copy_folder_to_public(folder_name):
     # Copy the contents of the folder to inside the public folder
    destination = "public/"
    
    if not os.path.exists(destination):
        os.makedirs(destination)  # Ensure the public folder exists
    
    if os.path.exists(folder_name):
        for item in os.listdir(folder_name):
            source_item = os.path.join(folder_name, item)
            destination_item = os.path.join(destination, item)
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination_item)