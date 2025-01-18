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
