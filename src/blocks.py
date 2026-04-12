import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"


def markdown_to_blocks(markdown):
    if markdown is None:
        return []
    blocks = []
    for block in markdown.split("\n\n"):
        block = block.strip()
        if len(block) == 0:
            continue
        blocks.append(block)
    return blocks


def block_to_block_type(block):
    if block is None:
        raise ValueError("block must be defined")

    lines = block.split("\n")
    if len(lines) == 0:
        raise ValueError("block must be non-empty")

    if block_is_heading(lines):
        return BlockType.HEADING
    if block_is_code(lines):
        return BlockType.CODE
    if block_is_quote(lines):
        return BlockType.QUOTE
    if block_is_unordered_list(lines):
        return BlockType.UNORDERED_LIST
    if block_is_ordered_list(lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def block_is_heading(lines):
    if len(lines) != 1:
        return False

    return re.match(r"^#{1,6}\s", lines[0])


def block_is_code(lines):
    if len(lines) < 2:
        return False

    return lines[0] == "```" and lines[-1] == "```"


def block_is_quote(lines):
    for line in lines:
        if len(line) == 0 or line[0] != ">":
            return False
    return True


def block_is_unordered_list(lines):
    for line in lines:
        if len(line) < 2 or line[:2] != "- ":
            return False
    return True


def block_is_ordered_list(lines):
    for i, line in enumerate(lines):
        if len(line) < 3 or line[:3] != f"{i + 1}. ":
            return False
    return True
