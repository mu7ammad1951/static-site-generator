import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_ineq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_ineq_2(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_2(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node1, node2)

    def test_text_node_to_html_text(self):
        node = TextNode("Hello World", TextType.TEXT)
        expected = "Hello World"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_bold(self):
        node = TextNode("Hello World", TextType.BOLD)
        expected = "<b>Hello World</b>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_italic(self):
        node = TextNode("Hello World", TextType.ITALIC)
        expected = "<i>Hello World</i>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_code(self):
        node = TextNode("Hello World", TextType.CODE)
        expected = "<code>Hello World</code>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_link(self):
        node = TextNode("Hello World", TextType.LINK, "https://boot.dev")
        expected = "<a href=\"https://boot.dev\">Hello World</a>"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_image(self):
        node = TextNode("Image of a cat", TextType.IMAGE, "https://boot.dev")
        expected = "<img src=\"https://boot.dev\" alt=\"Image of a cat\">"
        self.assertEqual(node.text_node_to_html_node().to_html(), expected)

    def test_text_node_to_html_invalid(self):
        with self.assertRaises(ValueError):
            node = TextNode(None, "None", None)
            node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()


