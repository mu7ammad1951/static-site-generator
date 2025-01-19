import unittest
from block_text_functions import *

class TestBlockTextFunctions(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        actual = markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item")
        expected = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(actual, expected)

    def test_markdown_to_blocks_multiple_newlines(self):
        md = """
First block

Second block



Third block
"""

        blocks = markdown_to_blocks(md)
        expected = ["First block", "Second block", "Third block"]

        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_trailing_newlines(self):  
        md = """
   
# Heading
Paragraph

"""

        blocks = markdown_to_blocks(md)
        expected = ["# Heading\nParagraph"]

        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_trailining_no_emptyline(self):  
        md = """
# Heading
Paragraph
"""

        blocks = markdown_to_blocks(md)
        expected = ["# Heading\nParagraph"]

        self.assertEqual(blocks, expected)

    def test_markdown_to_blocks_trailing_newlines_and_internal(self):  
        md = """
   
# Heading

Paragraph

"""

        blocks = markdown_to_blocks(md)
        expected = ["# Heading", "Paragraph"]

        self.assertEqual(blocks, expected)



    def test_block_to_block_type_heading_1(self):
        md = """
# This is a heading
"""
        expected = "heading"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_heading_6(self):
        md = """
###### This is a heading 6
"""
        expected = "heading"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_heading_3(self):
        md = """
### This is a heading
"""
        expected = "heading"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_code(self):
        md = """
```
This is a code block 
This contains lines of code
```
"""
        expected = "code"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_quote(self):
        md = """
> This is a quote
> This is a quote too
> This is a continuation of the previous quote
"""
        expected = "quote"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_unordered_list(self):
        md = """
* This is an unordered list
* Line
* Line
* Line 
"""
        expected = "unordered_list"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_ordered_list(self):
        md = """
1. This is an unordered list
2. Line
3. Line
4. Line 
"""
        expected = "ordered_list"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_paragraph(self):
        md = """
This is just a normal paragraph with nothing 
special in it.
"""
        expected = "paragraph"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)


    def test_block_to_block_type_ordered_feint_paragraph(self):
        md = """
1. This is an paragraph list
4. Line 
"""
        expected = "paragraph"
        actual = block_to_block_type(md)

        self.assertEqual(expected, actual)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


    def test_extract_title(self):
        md = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)
"""
        expected_title = "Tolkien Fan Club"
        actual_title = extract_title(md)
        self.assertEqual(expected_title, actual_title)


    def test_extract_title_different_levels(self):
        md = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

## Reasons I like Tolkien
"""
        expected_title = "Tolkien Fan Club"
        actual_title = extract_title(md)
        self.assertEqual(expected_title, actual_title)


    def test_extract_title_no_heading(self):
        md = """
**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

## Reasons I like Tolkien
"""
        with self.assertRaises(ValueError) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "Missing Heading 1")