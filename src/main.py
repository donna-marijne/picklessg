import sys

from copy_assets import copy_assets
from generate_page import generate_page, generate_pages_recursive


def main():
    print("it's picklin' time!")

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"basepath={basepath}")

    copy_assets("./static", "./docs")
    generate_pages_recursive(
        "./content", "./template.html", "./docs", basepath=basepath
    )


if __name__ == "__main__":
    main()
