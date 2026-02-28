from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
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
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(temp_file)




