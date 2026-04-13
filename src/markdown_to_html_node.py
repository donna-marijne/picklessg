import re

from blocks import BlockType, block_to_block_type, markdown_to_blocks
from parentnode import ParentNode
from parse import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_node = None
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_node = markdown_paragraph_to_html_node(block)
            case BlockType.HEADING:
                block_node = markdown_heading_to_html_node(block)
            case BlockType.CODE:
                block_node = markdown_code_to_html_node(block)
            case BlockType.QUOTE:
                block_node = markdown_quote_to_html_node(block)
            case BlockType.UNORDERED_LIST:
                block_node = markdown_unordered_list_to_html_node(block)
            case BlockType.ORDERED_LIST:
                block_node = markdown_ordered_list_to_html_node(block)

        block_nodes.append(block_node)

    return ParentNode("div", children=block_nodes)


def markdown_paragraph_to_html_node(markdown):
    p_text = " ".join(markdown.split("\n"))
    children = text_to_html_nodes(p_text)
    return ParentNode("p", children=children)


def markdown_heading_to_html_node(markdown):
    match = re.match(r"^(#{1,6})\s(.*)", markdown)
    assert match is not None
    level = len(match[1])
    children = text_to_html_nodes(match[2])
    return ParentNode(f"h{level}", children=children)


def markdown_code_to_html_node(markdown):
    lines = markdown.split("\n")
    code = "\n".join(lines[1:-1]) + "\n"
    code_node = text_node_to_html_node(TextNode(code, text_type=TextType.CODE))
    return ParentNode("pre", children=[code_node])


def markdown_quote_to_html_node(markdown):
    quote_text = ""
    lines = markdown.split("\n")
    for line in lines:
        quote_text += line[2:] + "\n"
    children = text_to_html_nodes(quote_text)
    return ParentNode("blockquote", children=children)


def markdown_unordered_list_to_html_node(markdown):
    children = []
    lines = markdown.split("\n")
    for line in lines:
        li_text = line.strip("- ")
        li_children = text_to_html_nodes(li_text)
        children.append(ParentNode("li", children=li_children))

    return ParentNode("ul", children=children)


def markdown_ordered_list_to_html_node(markdown):
    children = []
    lines = markdown.split("\n")
    for line in lines:
        match = re.match(r"\d+\.\s+(.*)", line)
        assert match is not None
        li_text = match[1]
        li_children = text_to_html_nodes(li_text)
        children.append(ParentNode("li", children=li_children))

    return ParentNode("ol", children=children)


def text_to_html_nodes(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes
