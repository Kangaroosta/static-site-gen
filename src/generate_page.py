from pathlib import Path
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as f:
        md = f.read()
    with open(template_path) as f:
        temp_file = f.read()
    md_node = markdown_to_html_node(md)
    html_string = md_node.to_html()
    title = extract_title(md)
    temp_file = temp_file.replace("{{ Title }}", title)
    temp_file = temp_file.replace("{{ Content }}", html_string)
    temp_file = temp_file.replace('href="/', f'href="{basepath}')
    temp_file = temp_file.replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(temp_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    current_directory = os.listdir(dir_path_content)
    for item in current_directory:
        current_path = os.path.join(dir_path_content, item)
        current_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(current_path):
            path = Path(current_dest_path)
            fixed_path = path.with_suffix(".html")
            generate_page(current_path, template_path, fixed_path, basepath)
        else:
            generate_pages_recursive(current_path, template_path, current_dest_path, basepath)