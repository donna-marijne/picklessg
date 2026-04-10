import unittest

from split import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
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


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image_none(self):
        text = "hello, world!"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_image([old_node])
        self.assertEqual(new_nodes, [old_node])

    def test_split_nodes_image_empty(self):
        text = ""
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_image([old_node])
        self.assertEqual(new_nodes, [old_node])

    def test_split_nodes_image_only(self):
        text = "![image](http://localhost:8080/hello.png)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_image([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello.png"
                ),
            ],
        )

    def test_split_nodes_image_and_text(self):
        text = "This is text with an ![image](http://localhost:8080/hello.png) and a [link](http://localhost:8080/world.html)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_image([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello.png"
                ),
                TextNode(
                    " and a [link](http://localhost:8080/world.html)", TextType.PLAIN
                ),
            ],
        )

    def test_split_nodes_image_multiple(self):
        text = "This is text with an ![image](http://localhost:8080/hello.png) and another ![image](http://localhost:8080/hello2.png)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_image([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello.png"
                ),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello2.png"
                ),
            ],
        )

    def test_split_nodes_image_multiple_nodes(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](http://localhost:8080/hello.png)",
                TextType.PLAIN,
            ),
            TextNode(
                "![image](http://localhost:8080/hello2.png) is another image",
                TextType.PLAIN,
            ),
        ]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello.png"
                ),
                TextNode(
                    "image", TextType.IMAGE, url="http://localhost:8080/hello2.png"
                ),
                TextNode(" is another image", TextType.PLAIN),
            ],
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_none(self):
        text = "hello, world!"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(new_nodes, [old_node])

    def test_split_nodes_link_empty(self):
        text = ""
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(new_nodes, [old_node])

    def test_split_nodes_link_only(self):
        text = "[our website](http://localhost:8080/)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("our website", TextType.LINK, url="http://localhost:8080/"),
            ],
        )

    def test_split_nodes_link_and_text(self):
        text = "This is text with an ![image](http://localhost:8080/hello.png) and a [link](http://localhost:8080/world.html)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode(
                    "This is text with an ![image](http://localhost:8080/hello.png) and a ",
                    TextType.PLAIN,
                ),
                TextNode("link", TextType.LINK, url="http://localhost:8080/world.html"),
            ],
        )

    def test_split_nodes_link_multiple(self):
        text = "This is text with a [link](http://localhost:8080/hello.html) and another [link](http://localhost:8080/world.html)"
        old_node = TextNode(text, TextType.PLAIN)
        new_nodes = split_nodes_link([old_node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, url="http://localhost:8080/hello.html"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, url="http://localhost:8080/world.html"),
            ],
        )

    def test_split_nodes_link_multiple_nodes(self):
        old_nodes = [
            TextNode(
                "This is text with a [link](http://localhost:8080/hello.html)",
                TextType.PLAIN,
            ),
            TextNode(
                "[This is](http://localhost:8080/world.html) another link",
                TextType.PLAIN,
            ),
        ]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, url="http://localhost:8080/hello.html"),
                TextNode(
                    "This is", TextType.LINK, url="http://localhost:8080/world.html"
                ),
                TextNode(" another link", TextType.PLAIN),
            ],
        )


if __name__ == "__main__":
    unittest.main()
