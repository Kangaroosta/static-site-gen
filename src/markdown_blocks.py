from enum import Enum
import re
from htmlnode import HTMLnode, ParentNode, LeafNode
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    result = []
    split = markdown.split("\n\n")
    for line in split:
        line = line.strip()
        if line != "":
            result.append(line)
    return result

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        lines = block.split("\n")
        quote = True
        for line in lines:
            if not line.startswith(">"):
                quote = False
                break
        if quote:
            return BlockType.QUOTE
    elif block.startswith("- "):
        lines = block.split("\n")
        unordered = True
        for line in lines:
            if not line.startswith("- "):
                unordered = False
                break
        if unordered:
            return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        split_block = block.split("\n")
        ordered = True
        for i, line in enumerate(split_block):
            if not line.startswith(f"{i+1}. "):
                ordered = False
                break
        if ordered:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_children.append(html_node)
    return html_children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            text = " ".join(line.strip() for line in lines)
            children = text_to_children(text)
            node = ParentNode("p", children)
        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            text = block[level + 1:]
            children = text_to_children(text)
            node = ParentNode(f'h{level}', children)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                if line.startswith("> "):
                    cleaned_lines.append(line[2:].strip())
                else:
                    cleaned_lines.append(line.strip())
            text = " ".join(cleaned_lines)
            children = text_to_children(text)
            node = ParentNode("blockquote", children)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                if line.startswith("- ") or line.startswith("* "):
                    text = line[2:].strip()
                else:
                    text= line.strip()
                children = text_to_children(text)
                list_nodes.append(ParentNode("li", children))
            node = ParentNode("ul", list_nodes)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_nodes = []
            for line in lines:
                text = line.split(". ", 1)[1]
                children = text_to_children(text)
                list_nodes.append(ParentNode("li", children))
            node = ParentNode("ol", list_nodes)
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            text = "\n".join(lines[1:-1]) + "\n"
            text_node = TextNode(text, TextType.TEXT)
            code_leaf = text_node_to_html_node(text_node)
            code_node = ParentNode("code", [code_leaf])
            node = ParentNode("pre", [code_node])
        else:
            children = text_to_children(block)
            node = ParentNode("p", children)
        block_nodes.append(node)
    return ParentNode("div", block_nodes)