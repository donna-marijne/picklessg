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
