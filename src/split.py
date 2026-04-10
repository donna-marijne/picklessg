import re

import extract
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        in_node = False
        text_fragments = old_node.text.split(delimiter)

        # probably not needed but in case it has other properties
        if len(text_fragments) == 1:
            new_nodes.append(old_node)
            continue

        if len(text_fragments) % 2 == 0:
            raise ValueError(f"mismatched {delimiter} in '{old_node.text}'")

        for text_fragment in text_fragments:
            if len(text_fragment) == 0:
                in_node = not in_node
                continue
            node_type = text_type if in_node else TextType.PLAIN
            new_node = TextNode(text_fragment, node_type)
            new_nodes.append(new_node)
            in_node = not in_node

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        fragments = re.split(extract.RE_IMAGE, old_node.text)

        if len(fragments) <= 1:
            new_nodes.append(old_node)
            continue

        alt_text = ""
        for i, fragment in enumerate(fragments):
            match i % 3:
                case 0:
                    # prefix plain text
                    if len(fragment) > 0:
                        new_nodes.append(TextNode(fragment, TextType.PLAIN))
                case 1:
                    # alt text match
                    alt_text = fragment
                case 2:
                    # url match
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=fragment))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        fragments = re.split(extract.RE_LINK, old_node.text)

        if len(fragments) <= 1:
            new_nodes.append(old_node)
            continue

        link_text = ""
        for i, fragment in enumerate(fragments):
            match i % 3:
                case 0:
                    # prefix plain text
                    if len(fragment) > 0:
                        new_nodes.append(TextNode(fragment, TextType.PLAIN))
                case 1:
                    # link text match
                    link_text = fragment
                case 2:
                    # url match
                    new_nodes.append(TextNode(link_text, TextType.LINK, url=fragment))

    return new_nodes
