import unittest

from parse import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_empty(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, [TextNode("", TextType.PLAIN)])

    def test_text_to_text_nodes_plain(self):
        text = "Hello, world!"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, [TextNode("Hello, world!", TextType.PLAIN)])

    def test_text_to_text_nodes_bold(self):
        text = "Just some **bold text**"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("Just some ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
            ],
        )

    def test_text_to_text_nodes_bold_italic(self):
        text = "**Bold text** and some _italics_"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("Bold text", TextType.BOLD),
                TextNode(" and some ", TextType.PLAIN),
                TextNode("italics", TextType.ITALIC),
            ],
        )

    def test_text_to_text_nodes_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )
