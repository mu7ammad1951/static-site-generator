import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_none_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_props(self):
        node = LeafNode("a", "Click me!", {})
        expected = "<a>Click me!</a>"

        self.assertEqual(node.to_html(), expected)

    def test_to_html_none_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"

        self.assertEqual(node.to_html(), expected)

    def test_to_html_none_tag(self):
        node = LeafNode(None, "Click me!", None)
        expected = "Click me!"

        self.assertEqual(node.to_html(), expected)

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "<a href=\"https://www.google.com\">Click me!</a>"

        self.assertEqual(node.to_html(), expected)

        