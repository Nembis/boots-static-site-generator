import os
import shutil

from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
from extractor import extract_title

SOURCE_DIR = "./static"
DEST_DIR = "public"

FROM_PATH = "./content/index.md"
TEMPALTE_PATH = "./template.html"
DEST_FILE =  os.path.join(DEST_DIR, "index.html")
TARGET_REPLACE_TITLE = "{{ Title }}"
TARGET_REPLACE_BODY = "{{ Content }}"

def copy_files_rec(static_dir: str, public_dir: str):
    files = os.listdir(static_dir)
    for file in files:
        full_dir = os.path.join(static_dir, file)
        full_dest = os.path.join(public_dir, file)
        if not os.path.isfile(full_dir):
            print(f"Creating new dir: {full_dest}")
            os.mkdir(full_dest)
            copy_files_rec(full_dir, full_dest)
        else:
            print(f"Copying file: {full_dir} => {full_dest}")
            shutil.copy(full_dir, full_dest)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_path_content = f.read()
    with open(template_path, "r") as f:
        template_path_content = f.read()
    title = extract_title(from_path_content)
    
    parent_node = markdown_to_html_node(from_path_content)
    generated_html = template_path_content.replace(TARGET_REPLACE_TITLE, title).replace(TARGET_REPLACE_BODY, parent_node.to_html())
    with open(dest_path, "w") as f:
        f.write(generated_html)




def main():
    print(f"Deleting {DEST_DIR}")
    shutil.rmtree(DEST_DIR)
    if not os.path.exists(DEST_DIR):
        print(f"Creating {DEST_DIR}")
        os.mkdir(DEST_DIR)
    copy_files_rec(SOURCE_DIR, DEST_DIR)
    print()

    generate_page(FROM_PATH, TEMPALTE_PATH, DEST_FILE)



if __name__ == "__main__":
    main()

