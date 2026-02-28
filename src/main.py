from textnode import *
from copystatic import copy_source
from generate_page import generate_page

def main():
    copy_source()
    generate_page("content/index.md", "template.html", "public/index.html")

main()