import sys
import shutil
from pathlib import Path


def copy_file(file_path, dest_root):
    """Copies a file to a folder based on its extension."""
    ext = file_path.suffix.lower().lstrip(".")  # Get the file extension
    # check if no extension
    if ext == "":
        ext = "no_extension"

    target_dir = dest_root / ext

    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, target_dir / file_path.name)
    except FileNotFoundError:
        print(f"File not found: {file_path}")


def process_directory(source, dest_root):
    """Recursively processes a directory"""
    try:
        for item in source.iterdir():
            if item.is_dir():
                process_directory(item, dest_root)
            elif item.is_file():
                copy_file(item, dest_root)
    except FileNotFoundError:
        print(f"Directory not found: {source}")


def main():
    if len(sys.argv) < 2:
        print("Use: python task_1.py <source_dir> [dest_dir]")
        return

    source_path = Path(sys.argv[1])  # source
    dest_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")  # output

    if not source_path.exists() or not source_path.is_dir():
        print("The source directory does not exist or is not a folder.")
        return

    # create output folder
    dest_path.mkdir(parents=True, exist_ok=True)

    process_directory(source_path, dest_path)


if __name__ == "__main__":
    main()
