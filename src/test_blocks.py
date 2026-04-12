import unittest

from blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_3_newlines(self):
        md = """
This is the first line.


This is the second line.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["This is the first line.", "This is the second line."]
        )

    def test_markdown_to_blocks_4_newlines(self):
        md = """
This is the first line.



This is the second line.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks, ["This is the first line.", "This is the second line."]
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_empty(self):
        block_type = block_to_block_type("")
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph_1(self):
        block = """
Hello, world!
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph_3(self):
        block = """
Hello, world!
Lorem ipsum
Foo Bar Baz
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_heading_1(self):
        block = """
# Heading 1
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_6(self):
        block = """
###### Heading 6
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading_7(self):
        block = """
####### Heading 7
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_code_1(self):
        block = """
```
code block here
```
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_code_3(self):
        block = """
```
code block here
i += 1
print("ok")
```
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_code_no_opener(self):
        block = """
code block here
```
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_code_no_closer(self):
        block = """
```
code block here
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_code_indented(self):
        block = """
    ```
    code block here
    ```
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_code_trailing_text(self):
        block = """
```
code block here
```
trailing text
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_quote_space(self):
        block = """
> quote text
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_quote_no_space(self):
        block = """
>quote text
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_quote_multiple(self):
        block = """
> quote text
> another quote
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_quote_indented(self):
        block = """
    > quote text
    > another quote
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_quote_trailing_text(self):
        block = """
> quote text
> another quote
not a quote
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_1(self):
        block = """
- item 1
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_3(self):
        block = """
- item 1
- item 2
- item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_unordered_list_no_space(self):
        block = """
-item 1
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_indented(self):
        block = """
    - item 1
    - item 2
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_trailing_text(self):
        block = """
- item 1
trailing text
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_1(self):
        block = """
1. item 1
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_3(self):
        block = """
1. item 1
2. item 2
3. item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ordered_list_all_1(self):
        block = """
1. item 1
1. item 2
1. item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_skip_2(self):
        block = """
1. item 1
3. item 2
4. item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_zero_index(self):
        block = """
0. item 1
1. item 2
2. item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_indented(self):
        block = """
    1. item 1
    2. item 2
    3. item 3
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_trailing_text(self):
        block = """
1. item 1
2. item 2
3. item 3
trailing text
"""
        block_type = block_to_block_type(block.strip())
        self.assertEqual(block_type, BlockType.PARAGRAPH)
