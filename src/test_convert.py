import unittest

from convert import text_node_to_html_node
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_italic(self):
        node = TextNode("Hello, world!", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_code(self):
        node = TextNode("Hello, world!", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Hello, world!")

    def test_link(self):
        node = TextNode("Hello, world!", TextType.LINK, "http://localhost:8080/")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertDictEqual(html_node.props, {"href": "http://localhost:8080/"})
        self.assertEqual(html_node.value, "Hello, world!")

    def test_image(self):
        node = TextNode(
            "Our banner", TextType.IMAGE, "http://localhost:8080/banner.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertDictEqual(
            html_node.props,
            {"src": "http://localhost:8080/banner.png", "alt": "Our banner"},
        )
        self.assertIsNone(html_node.value)


if __name__ == "__main__":
    unittest.main()
