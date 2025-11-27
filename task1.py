import argparse
from pathlib import Path
import shutil


def copy_and_sort(src_dir: Path, dst_dir: Path):
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                copy_and_sort(item, dst_dir)
            else:
                ext = item.suffix[1:] if item.suffix else "no_extension"
                ext_dir = dst_dir / ext
                ext_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, ext_dir / item.name)
    except PermissionError:
        print(f"Access denied to: {src_dir}")
    except Exception as e:
        print(f"Error occured while processing '{src_dir}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Recursive copying files by extension")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("destination", nargs="?", default="dist",
                        help="Destination directory (optional)")
    args = parser.parse_args()
    src_dir = Path(args.source)
    dst_dir = Path(args.destination)

    if not src_dir.is_dir():
        print(f"Source directory not found: {src_dir}")
        exit(1)

    dst_dir.mkdir(parents=True, exist_ok=True)
    copy_and_sort(src_dir, dst_dir)
    print(f"Files from '{src_dir}' are copied to '{dst_dir}'")


if __name__ == "__main__":
    main()
