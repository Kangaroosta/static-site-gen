from textnode import *
from copystatic import copy_source
from generate_page import generate_page, generate_pages_recursive

def main():
    copy_source()
    generate_pages_recursive("content", "template.html", "public")

main()