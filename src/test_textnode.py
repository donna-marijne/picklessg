import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a link", TextType.LINK, "http://localhost:8080/")
        node2 = TextNode("This is a link", TextType.LINK, "http://localhost:8080/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is bold", TextType.BOLD)
        node2 = TextNode("This is BOLD", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is pod racing!", TextType.BOLD)
        node2 = TextNode("This is pod racing!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_link(self):
        node = TextNode("This is a link", TextType.LINK, "http://localhost:8080/")
        node2 = TextNode("This is a link", TextType.LINK, "http://localhost:8000/")
        self.assertNotEqual(node, node2)

    def test_not_eq_link_2(self):
        node = TextNode("This is a link", TextType.LINK, "http://localhost:8080/")
        node2 = TextNode("This is a link", TextType.LINK, None)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
