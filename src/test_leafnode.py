import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Our website", props={"href": "http://localhost:8080/"})
        self.assertEqual(
            node.to_html(), '<a href="http://localhost:8080/">Our website</a>'
        )

    def test_leaf_to_html_text(self):
        node = LeafNode(None, "hooley dooley")
        self.assertEqual(node.to_html(), "hooley dooley")

    def test_leaf_to_html_empty(self):
        node = LeafNode("pre", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
