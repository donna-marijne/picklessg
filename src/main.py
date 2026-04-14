from copy_assets import copy_assets
from generate_page import generate_page, generate_pages_recursive


def main():
    print("it's picklin' time!")
    copy_assets("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")


if __name__ == "__main__":
    main()
