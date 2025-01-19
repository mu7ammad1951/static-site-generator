import re
from parentnode import ParentNode
from inline_text_functions import *

def markdown_to_blocks(text):
    return list(filter(lambda x: x!="", map(lambda x: x.strip(), text.split("\n\n"))))

def block_to_block_type(block):
    lines = list(filter(lambda x: x != "",list(block.split("\n"))))
    
    if check_heading(block):
        return "heading"
    if check_quotes(lines):
        return "quote"
    if check_code(block):
        return "code"
    if check_unordered_list(lines):
        return "unordered_list"
    if check_ordered_list(lines):
        return "ordered_list"

    return "paragraph"

# Heading
def check_heading(text):
    heading_matcher = re.compile(r"^\s*\#{1,6}\ .*")
    is_heading = True
    if heading_matcher.match(text) is None:
        is_heading = False

    return is_heading

def check_quotes(lines):
    quote_matcher = re.compile(r"^\s*>{1}\ .*")
    is_quote = True
    for line in lines:
        if line == "":
            continue
        if quote_matcher.match(line) is None:
            is_quote = False

    return is_quote

def check_code(text):
    code_matcher = re.match(r"^\s*```[\S\s]*```\s*$", text)
    return code_matcher is not None

def check_unordered_list(lines):
    ulist_matcher = re.compile(r"^\s*[*-]{1}\ .*")
    is_ulist = True
    for line in lines:
        if line == "":
            continue
        if ulist_matcher.match(line) is None:
            is_ulist = False

    return is_ulist

def check_ordered_list(lines):
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
        

    return True


def markdown_to_html_node(markdown_text):
    # Convert markdown to blocks
    # Convert blocks to appropriate values
    #   1. Determine the type of block (you already have a function for this)
    #   2. Based on the type of block, create a new HTMLNode with the proper data
    #   3. Assign the proper child HTMLNode objects to the block node. I created a shared 
    #      text_to_children(text) function that works for all block types. It takes a string of 
    #      text and returns a list of HTMLNodes that represent the inline markdown using 
    #      previously created functions (think TextNode -> HTMLNode).
    # Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

    blocks = markdown_to_blocks(markdown_text)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_node(block, block_type))
    
    return ParentNode("div", children)

def block_to_node(block, block_type):

    match(block_type):
        case("heading"):
            return heading_to_html(block)
        case("quote"):
            return quote_to_html(block)
        case("code"):
            return code_to_html(block)
        case("unordered_list"):
            return unordered_to_html(block)
        case("ordered_list"):
            return ordered_to_html(block)
        case("paragraph"):
            return paragraph_to_html(block)
        case _:
            raise Exception("Invalid Block Type")

def heading_to_html(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    tag = f'h{level}'
    if level+1 >= len(block):
        raise ValueError("Invalid Heading Level")
    text = block[level+1:]
    children = text_to_children(text)
    return ParentNode(tag, children)

def quote_to_html(block):
    tag = "blockquote"
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid Quote Block")
        line_text = line.lstrip(">").strip()
        new_lines.append(line_text)
    content = " ".join(new_lines)
    return ParentNode(tag, text_to_children(content))

def code_to_html(block):
    tag = "code"
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Invalid Code Block")
    code_text = block[4:-3]
    code_node = ParentNode(tag, text_to_children(code_text))
    return ParentNode("pre", [code_node])

def text_to_children(text):
    nodes = text_to_text_nodes(text)
    children = []
    for node in nodes:
        children.append(node.text_node_to_html_node())
    return children

def paragraph_to_html(block):
    lines = block.split("\n")
    content = " ".join(lines)
    children = text_to_children(content)
    return ParentNode("p", children)

def unordered_to_html(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        if not line.startswith("*") and not line.startswith("-"):
            raise ValueError("Invalid Unordered List Block")
        line_text = line[2:].strip()
        list_items.append(ParentNode("li", text_to_children(line_text)))
    return ParentNode("ul", list_items)

def ordered_to_html(block):
    lines = block.split("\n")
    list_items = []
    for line in lines:
        line_text = line[2:].strip()
        list_items.append(ParentNode("li", text_to_children(line_text)))
    return ParentNode("ol", list_items)