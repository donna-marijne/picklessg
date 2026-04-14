from copy_assets import copy_assets
from generate_page import generate_page


def main():
    print("it's picklin' time!")
    copy_assets("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")


if __name__ == "__main__":
    main()
