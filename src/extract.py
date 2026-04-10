import re

RE_IMAGE = r"!\[(.*?)\]\((.*?)\)"
RE_LINK = r"(?<!\!)\[(.*?)\]\((.*?)\)"


def extract_markdown_images(text):
    return re.findall(RE_IMAGE, text)


def extract_markdown_links(text):
    return re.findall(RE_LINK, text)
