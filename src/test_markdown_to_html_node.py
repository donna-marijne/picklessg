import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_lists(self):
        md = """
Here are some lists:

- red
- orange
- _yellow_ and _pink_

1. Lorem ipsum
2. Sit dolor

1. Here's a [link](http://localhost:8080/index.html)
2. and here's an image ![logo](http://localhost:8080/logo.png)

Happy Hacking
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Here are some lists:</p><ul><li>red</li><li>orange</li><li><i>yellow</i> and <i>pink</i></li></ul><ol><li>Lorem ipsum</li><li>Sit dolor</li></ol><ol><li>Here\'s a <a href="http://localhost:8080/index.html">link</a></li><li>and here\'s an image <img src="http://localhost:8080/logo.png" alt="logo" /></li></ol><p>Happy Hacking</p></div>',
        )

    def test_headings(self):
        md = """
# Heading 1

Content 1

## Heading 2

Content 2

### Heading 3 _(with some italics)_

Content 3

#### [Heading 4 with a link](http://localhost:8080/index.html)

Content 4

##### Heading 5

Content 5

###### Heading 6

Content 6
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading 1</h1><p>Content 1</p><h2>Heading 2</h2><p>Content 2</p><h3>Heading 3 <i>(with some italics)</i></h3><p>Content 3</p><h4><a href="http://localhost:8080/index.html">Heading 4 with a link</a></h4><p>Content 4</p><h5>Heading 5</h5><p>Content 5</p><h6>Heading 6</h6><p>Content 6</p></div>',
        )
