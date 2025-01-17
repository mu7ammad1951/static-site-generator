import unittest
from inline_text_functions import *
from textnode import TextNode, TextType

class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]'
        self.assertEqual("".join(str(new_nodes)), expected)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.BOLD), TextNode(" word", TextType.TEXT)]'
        self.assertEqual("".join(str(new_nodes)), expected)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a *code block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)

        expected = '[TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.ITALIC), TextNode(" word", TextType.TEXT)]'
        self.assertEqual("".join(str(new_nodes)), expected)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = "[('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]"

        self.assertEqual(str(extract_markdown_images(text)), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = "[('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]"

        self.assertEqual(str(extract_markdown_links(text)), expected)


    def test_split_nodes_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )   
        new_nodes = split_nodes_links([node])
        expected = '[TextNode("This is text with a link ", TextType.TEXT), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), TextNode(" and ", TextType.TEXT), TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")]'

        self.assertEqual(str(new_nodes), expected)


    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an image ![cute bear](https://pics.com/bear) and some text after",
            TextType.TEXT,
        )   
        new_nodes = split_nodes_images([node])
        expected = '[TextNode("This is text with an image ", TextType.TEXT), TextNode("cute bear", TextType.IMAGE, "https://pics.com/bear"), TextNode(" and some text after", TextType.TEXT)]'

        self.assertEqual(str(new_nodes), expected)


    def test_text_to_text_nodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected = '[TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.TEXT), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.LINK, "https://boot.dev")]'
        
        processed = text_to_text_nodes(text)

        self.assertEqual(str(processed), expected)