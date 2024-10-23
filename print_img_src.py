import subprocess
from pathlib import Path

import pyperclip
from PIL import Image


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
    path = Path("assets/photos").resolve()
    if not path.exists():
        print(f"path:{path} is wrong")
        return

    # Get the set of untracked files
    untracked_files = get_untracked_files()

    html_output = ""
    for filepath in sorted(
        path.glob("*"), key=lambda x: "_".join(str(x).split("_")[2:])
    ):
        name = str(filepath).split("Photo/")[1]
        # Check if the file is an image and is untracked by Git
        if (
            any(ext in str(filepath).lower() for ext in ["jpg", "jpeg", "png"])
            and name in untracked_files
        ):
            img = Image.open(filepath)
            html_line = f'<img src="{name}" width="{img.width}" height="{img.height}" loading="lazy" class="thumbnail" onclick="toggleScale(this)"/>'
            html_output += html_line + "\n"

    print(html_output)
    pyperclip.copy(html_output)


if __name__ == "__main__":
    print_img_src()
