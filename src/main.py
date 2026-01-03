import os
import sys
import shutil
from pathlib import Path

from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode
from extractor import extract_title

SOURCE_DIR = "./static"
DEST_DIR = "./public"

FROM_PATH = "./content/"
TEMPALTE_PATH = "./template.html"
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

def generate_page(from_path, template_path, dest_path, base_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_path_content = f.read()
    with open(template_path, "r") as f:
        template_path_content = f.read()
    title = extract_title(from_path_content)
    
    parent_node = markdown_to_html_node(from_path_content)
    generated_html = template_path_content.replace(TARGET_REPLACE_TITLE, title).replace(TARGET_REPLACE_BODY, parent_node.to_html())
    generated_html = generated_html.replace("href=\"/", f"href=\"{base_path}")
    generated_html = generated_html.replace("src=\"/", f"src=\"{base_path}")

    dest_folder_path = os.path.dirname(dest_path)
    path = Path(dest_folder_path)
    path.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(generated_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path: str):
    files = os.listdir(dir_path_content)
    for file in files:
        full_source_path = os.path.join(dir_path_content, file)
        full_dest_path = os.path.join(dest_dir_path, file)
        if not os.path.isfile(full_source_path):
            generate_pages_recursive(full_source_path, template_path, full_dest_path, base_path)
        else:
            full_dest_path = full_dest_path.replace(".md", ".html")
            generate_page(full_source_path, template_path, full_dest_path, base_path)


def main():
    root_path = sys.argv[1]
    if not root_path:
        root_path = "/"
    print("ROOT PATH: ", root_path)

    print(f"Deleting {DEST_DIR}")
    if os.path.exists(DEST_DIR):
        shutil.rmtree(DEST_DIR)
    if not os.path.exists(DEST_DIR):
        print(f"Creating {DEST_DIR}")
        os.mkdir(DEST_DIR)
    copy_files_rec(SOURCE_DIR, DEST_DIR)
    print()

    generate_pages_recursive(FROM_PATH, TEMPALTE_PATH, DEST_DIR, root_path)



if __name__ == "__main__":
    main()

