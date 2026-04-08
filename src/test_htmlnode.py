import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("p", "hello, world")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_id(self):
        node = HTMLNode("p", "hello, world", props={"class": "p-1"})
        self.assertEqual(node.props_to_html(), ' class="p-1"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("p", "hello, world", props={"id": "main_1", "class": "p-1"})
        self.assertEqual(node.props_to_html(), ' id="main_1" class="p-1"')


if __name__ == "__main__":
    unittest.main()
