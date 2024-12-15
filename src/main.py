from textnode import TextNode,TextType
from htmlnode import HTMLNode,LeafNode,ParentNode
from inline_markdown import text_to_textnodes
from gencontent import generate_pages_recursive
import os,shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory contents...")
    clean_directory(dir_path_public)
    print("Copying static files to public directory...")
    move_files_to_public_directory(dir_path_static,dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

def clean_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)

def move_files_to_public_directory(source_directory, destination_directory):
    for item in os.listdir(source_directory):
        s = os.path.join(source_directory, item)
        d = os.path.join(destination_directory, item)
        
        if os.path.isdir(s):
            # If the directory already exists at the destination, remove it
            if os.path.exists(d):
                shutil.rmtree(d)
            # Recursively copy the entire directory tree
            shutil.copytree(s, d)
        else:
            # Copy a single file, preserving metadata
            shutil.copy2(s, d)

if __name__ == "__main__":
    main()