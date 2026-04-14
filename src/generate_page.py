import os

from extract import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_pages_recursive(
    dir_path_content, template_path, dest_dir_path, basepath="/"
):
    for name in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, name)
        if os.path.isfile(path):
            name_root, ext = os.path.splitext(name)
            if ext != ".md":
                print(f"non-markdown file ignored: {dir_path_content}/{name}")
                continue
            dest_path = os.path.join(dest_dir_path, name_root + ".html")
            generate_page(path, template_path, dest_path, basepath=basepath)
        else:
            dest_path = os.path.join(dest_dir_path, name)
            generate_pages_recursive(path, template_path, dest_path, basepath=basepath)


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = read_file_to_str(from_path)
    template = read_file_to_str(template_path)

    title = extract_title(markdown)
    html_content = markdown_to_html_node(markdown).to_html()

    page_content = (
        template.replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        print(f"makedirs: {dest_dir}")
        os.makedirs(dest_dir)

    print(f"write: {dest_path}")
    with open(dest_path, mode="w") as dest_file:
        dest_file.write(page_content)


def read_file_to_str(path):
    if not os.path.isfile(path):
        raise ValueError(f"{path} is not a file")

    with open(path) as file:
        return file.read()
