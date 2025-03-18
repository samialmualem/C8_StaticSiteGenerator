import os
import shutil



def clean_public_folder(public_folder="public"):
    # Remove all files in the public folder
    if os.path.exists(public_folder):
        shutil.rmtree(public_folder)
    os.makedirs(public_folder)

def copy_folder_to_public(folder_name, public_folder="public"):
     # Copy the contents of the folder to inside the public folder
    destination = f"{public_folder}/"
    
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