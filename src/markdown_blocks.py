from enum import Enum
import re

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