import subprocess
from pathlib import Path

import pyperclip
from PIL import Image

# Usage: python print_html.py


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
    untracked_files = get_untracked_files()
    html_output = ""
    path = Path("assets/photos/mog").resolve()

    for filepath in sorted(
        path.glob("*"),
        key=lambda x: (
            str(x).split("_")[1]
            if len(str(x).split("_")) > 1
            else "",  # Sort by location (e.g., 'busan', 'seoul')
            str(x).split("_")[2]
            if len(str(x).split("_")) > 2
            else "",  # Sort by the next part (e.g., '00018' or 'qingdao')
            int(str(x).split("_")[3].split(".")[0])
            if len(str(x).split("_")) > 3
            and str(x).split("_")[3].split(".")[0].isdigit()
            else float("inf"),
        ),
    ):
        img_path = str(filepath).split("portfolio/")[1]
        if (
            any(
                ext in filepath.suffix.lower()
                for ext in [".jpg", ".jpeg", ".png", ".tiff", ".heic"]
            )
            and img_path in untracked_files
        ):
            img = Image.open(filepath)
            html_output += f'<img src="{img_path}" width="{img.width}" height="{img.height}" class="thumbnail" onclick="toggleScale(this)" loading="lazy"/>\n'

    print(html_output)
    pyperclip.copy(html_output)


if __name__ == "__main__":
    print_img_src()
