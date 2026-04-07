from textnode import TextNode, TextType


def main():
    text_node = TextNode("hello, world!", TextType.BOLD)
    print(text_node)
    text_node = TextNode("boot.dev", TextType.LINK, "https://boot.dev")
    print(text_node)


if __name__ == "__main__":
    main()
