import subprocess
from pathlib import Path

import pyperclip
from PIL import Image

# Usage: python assets/python/print_html.py


def get_untracked_files():
    # Get the list of untracked files using git
    result = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard"],
        capture_output=True,
        text=True,
    )
    # Split the output by lines to get each untracked file
    untracked_files = result.stdout.splitlines()
    return set(untracked_files)


def print_img_src():
    # Get the set of untracked files
    untracked_files = get_untracked_files()

    html_output = ""
    path = Path("assets/photos").resolve()
    for filepath in sorted(
        path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])
    ):
        img_path = str(filepath).split("Photo/")[1]
        # Check if the file is an image and is untracked by Git
        if (
            any(
                ext in str(filepath).lower()
                for ext in ["jpg", "jpeg", "png", "tiff", "heic"]
            )
            # and img_path in untracked_files
        ):
            img_name = img_path.split("/")[-1].split(".")[-2]
            for low_filepath in Path("assets/photos/low").resolve().glob("*"):
                if img_name in str(low_filepath):
                    low_img_path = str(low_filepath).split("Photo/")[1]
            img = Image.open(filepath)
            html_line = f'<img src="{low_img_path}" data-fullres="{img_path}" width="{img.width}" height="{img.height}" class="thumbnail" onclick="toggleScale(this)"/>'

            html_output += html_line + "\n"

    print(html_output)
    pyperclip.copy(html_output)


if __name__ == "__main__":
    print_img_src()
