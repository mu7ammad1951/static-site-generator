from textnode import TextNode, TextType
import re

def split_nodes_delimiter(oldnodes, delimiter, text_type):
    def split_delimiter(node, delimiter, text_type):
        node_text = node.text
        node_type = node.text_type
        if node.text_type != TextType.TEXT:
            return [node]
        
        result = []
        split_node_text = node_text.split(delimiter)
        if len(split_node_text) % 2 == 0:
            raise Exception("Invalid Markdown Syntax: Missing closing delimiter")
        for i in range(len(split_node_text)):
            result.append(TextNode(split_node_text[i], text_type) if i % 2 != 0 else TextNode(split_node_text[i], node_type))
        
        return result
    
    result = []
    for node in oldnodes:
        result.extend(split_delimiter(node, delimiter, text_type))

    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_images(oldnodes):
    def split_images(node):
        node_text = node.text
        node_type = node.text_type
        if node.text_type != TextType.TEXT:
            return [node]
    
        result = []
        
        to_be_processed = node_text
        processed = ""

        extracted_image_tuples = extract_markdown_images(node_text)
        for image in extracted_image_tuples:
            alt_text, image_link = image
            processed, to_be_processed = to_be_processed.split(f"![{alt_text}]({image_link})", 1)
            result.append(TextNode(processed, TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, image_link))

        if to_be_processed:
            result.append(TextNode(to_be_processed, TextType.TEXT))

        return result
    
    result = []
    for node in oldnodes:
        result.extend(split_images(node))
    
    return result

def split_nodes_links(oldnodes):
    def split_links(node):
        node_text = node.text
        node_type = node.text_type
        if node.text_type != TextType.TEXT:
            return [node]
    
        result = []
        
        to_be_processed = node_text
        processed = ""

        extracted_links_tuples = extract_markdown_links(node_text)
        for link in extracted_links_tuples:
            text, href_link = link
            processed, to_be_processed = to_be_processed.split(f"[{text}]({href_link})", 1)
            result.append(TextNode(processed, TextType.TEXT))
            result.append(TextNode(text, TextType.LINK, href_link))

        if to_be_processed:
            result.append(TextNode(to_be_processed, TextType.TEXT))

        return result
    
    result = []
    for node in oldnodes:
        result.extend(split_links(node))
    
    return result


def text_to_text_nodes(text):
    original_text = TextNode(text, TextType.TEXT)

    bold_processed_nodes = split_nodes_delimiter([original_text], "**", TextType.BOLD)
    italic_processed_nodes = split_nodes_delimiter(bold_processed_nodes, "*", TextType.ITALIC)
    code_processed_nodes = split_nodes_delimiter(italic_processed_nodes, "`", TextType.CODE)
    link_processed_nodes = split_nodes_links(code_processed_nodes)
    image_processed_nodes = split_nodes_images(link_processed_nodes)
    return image_processed_nodes
