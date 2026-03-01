from textnode import *
from copystatic import copy_source
from generate_page import generate_page, generate_pages_recursive
import sys
def main():
    basepath = sys.argv[1] or "/"
    copy_source(src="static", dest="docs", clean=True)
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()