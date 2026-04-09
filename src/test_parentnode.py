import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_text_child(self):
        child_node = LeafNode(None, "hello world!")
        node = ParentNode("body", [child_node])
        self.assertEqual(node.to_html(), "<body>hello world!</body>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "hello world!")
        node = ParentNode("div", [child_node], props={"class": "flex"})
        self.assertEqual(
            node.to_html(), '<div class="flex"><span>hello world!</span></div>'
        )

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "hello world!")
        node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_empty_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_child_error(self):
        child_node = LeafNode("span", None)
        node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
