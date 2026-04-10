import unittest

from split import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplit(unittest.TestCase):
    def test_split_empty(self):
        new_nodes = split_nodes_delimiter([], "`", TextType.CODE)
        self.assertEqual(new_nodes, [])

    def test_split_none(self):
        node = TextNode("This is text with no special formatting", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [TextNode("This is text with no special formatting", TextType.PLAIN)],
        )

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ],
        )

    def test_split_code_multiple_in_single_node(self):
        node = TextNode("You can press `m`, `ctrl-M`, or `Esc`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("You can press ", TextType.PLAIN),
                TextNode("m", TextType.CODE),
                TextNode(", ", TextType.PLAIN),
                TextNode("ctrl-M", TextType.CODE),
                TextNode(", or ", TextType.PLAIN),
                TextNode("Esc", TextType.CODE),
            ],
        )

    def test_split_code_multiple_nodes(self):
        node1 = TextNode("You can press `m`, ", TextType.PLAIN)
        node2 = TextNode("`ctrl-M`, or `Esc`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("You can press ", TextType.PLAIN),
                TextNode("m", TextType.CODE),
                TextNode(", ", TextType.PLAIN),
                TextNode("ctrl-M", TextType.CODE),
                TextNode(", or ", TextType.PLAIN),
                TextNode("Esc", TextType.CODE),
            ],
        )

    def test_split_code_only(self):
        node = TextNode("`text_type`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [TextNode("text_type", TextType.CODE)],
        )

    def test_split_code_no_closer(self):
        node = TextNode("`text_type", TextType.PLAIN)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_code_no_closer_3(self):
        node = TextNode("`text_type`, `text", TextType.PLAIN)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.PLAIN),
            ],
        )

    def test_split_bold_consecutive(self):
        node = TextNode("This is text with a **bold****word**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
                TextNode("word", TextType.BOLD),
            ],
        )

    def test_split_multiple_types(self):
        node = TextNode(
            "This is text with `code block`, **bold**, and __italic__ words",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(", **bold**, and __italic__ words", TextType.PLAIN),
            ],
        )

if __name__ == "__main__":
    unittest.main()
