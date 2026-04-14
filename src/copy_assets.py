import os
import shutil


def copy_assets(source_dir, dest_dir):
    if os.path.isdir(dest_dir):
        clean_dir(dest_dir)
    else:
        print(f"mkdir: {dest_dir}")
        os.mkdir(dest_dir)
    copy_assets_in_dir(source_dir, dest_dir)


def clean_dir(dest_dir):
    for name in os.listdir(dest_dir):
        path = os.path.join(dest_dir, name)
        if os.path.isfile(path):
            print(f"unlink: {path}")
            os.unlink(path)
        else:
            print(f"rmtree: {path}")
            shutil.rmtree(path)


def copy_assets_in_dir(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        print(f"mkdir: {dest_dir}")
        os.mkdir(dest_dir)

    for name in os.listdir(source_dir):
        source_path = os.path.join(source_dir, name)
        dest_path = os.path.join(dest_dir, name)
        if os.path.isfile(source_path):
            print(f"copy: {source_path} -> {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            copy_assets_in_dir(source_path, dest_path)
