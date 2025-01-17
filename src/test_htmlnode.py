import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "www.google.com", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })

        expected_result = " href=\"https://www.google.com\" target=\"_blank\""

        self.assertEqual(node.props_to_html(), expected_result)

    def test_repr_1(self):
        node = HTMLNode()
        self.assertEqual(f"Tag: {None} \n Value: {None} \n Children: {None} \n Props: {None}", str(node))
    
    def test_props_to_html_2(self):
        node = HTMLNode("a", "www.google.com", None, {
            "href": "https://www.google.com",
        })

        expected_result = " href=\"https://www.google.com\""

        self.assertEqual(node.props_to_html(), expected_result)

    def test_props_to_html_3(self):
        node = HTMLNode("a", "www.google.com", None, {
        })

        expected_result = ""

        self.assertEqual(node.props_to_html(), expected_result)

    def test_repr_2(self):
        node = HTMLNode("a", "www.google.com", [], {
        })
        self.assertEqual(f"Tag: a \n Value: www.google.com \n Children: {[]} \n Props: {{}}", str(node))

    def test_to_html_raises(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()