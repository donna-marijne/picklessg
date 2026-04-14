import re

RE_IMAGE = r"!\[(.*?)\]\((.*?)\)"
RE_LINK = r"(?<!\!)\[(.*?)\]\((.*?)\)"
RE_TITLE = r"^#\s+(.+)"


def extract_markdown_images(text):
    return re.findall(RE_IMAGE, text)


def extract_markdown_links(text):
    return re.findall(RE_LINK, text)


def extract_title(text):
    match = re.search(RE_TITLE, text, re.MULTILINE)
    if match is None:
        raise ValueError("no title found")

    return match[1]
