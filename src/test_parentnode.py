import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_tag_children_no_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        actual = node.to_html()
        self.assertEqual(actual, expected)

    def test_to_html_no_tag_children_no_props(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing Tag")

    
    def test_to_html_tag_no_children_no_props(self):
        node = ParentNode(
            "p", None,
        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing Children")

    def test_to_html_tag_children_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {
                "class":"paragraph important",
            }
        )

        expected = "<p class=\"paragraph important\"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    
    def test_to_html_tag_parent_node_children_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode("ul", 
                           [
                               LeafNode("li", "Fruits", {"class":"first-item"}),
                               LeafNode("li", "Mango"),
                               LeafNode("li", "Orange")

                           ])
            ],
            {
                "class":"paragraph important",
            }
        )

        expected = "<div class=\"paragraph important\"><b>Bold text</b>Normal text<i>italic text</i>Normal text<ul><li class=\"first-item\">Fruits</li><li>Mango</li><li>Orange</li></ul></div>"
        self.assertEqual(node.to_html(), expected)
