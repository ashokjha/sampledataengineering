import os
from urllib.parse import quote
from dotenv import load_dotenv

# Configuration
DOCUMENTS_DIR = "reports"
README_PATH = "src/poc/README.md"
START_MARKER = "<!-- PDF_LIST_START -->"
END_MARKER = "<!-- PDF_LIST_END -->"


def format_title(name):
    return os.path.splitext(name)[0].replace("_", " ").replace("-", " ").title()


def scan_directory_recursive(base_dir, current_dir, indent_level=0):
    """create hierarchical list।"""
    markdown_text = ""
    indent = "  " * indent_level

    try:
        items = sorted(os.listdir(current_dir))
    except FileNotFoundError:
        return ""

    # process Sub-directories]
    for item in items:
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            has_pdf = any(
                f.lower().endswith(".pdf")
                for _, _, files in os.walk(item_path)
                for f in files
            )

            if has_pdf:
                folder_title = format_title(item)
                markdown_text += f"{indent}* 📁 **{folder_title}**\n"
                markdown_text += scan_directory_recursive(
                    base_dir, item_path, indent_level + 1
                )

    for item in items:
        item_path = os.path.join(current_dir, item)
        if os.path.isfile(item_path) and item.lower().endswith(".pdf"):
            file_title = format_title(item)
            relative_url = os.path.relpath(
                item_path, os.path.dirname(README_PATH)
            ).replace("\\", "/")
            safe_url = quote(relative_url, safe="/")
            markdown_text += f"{indent}* 📄 [{file_title}]({safe_url})\n"

    return markdown_text


def update_readme():
    if not os.path.exists(DOCUMENTS_DIR):
        print(f"Error: Folder '{DOCUMENTS_DIR}' not found.")
        return

    pdf_list_md = scan_directory_recursive(DOCUMENTS_DIR, DOCUMENTS_DIR)

    if not pdf_list_md.strip():
        pdf_list_md = "* No PDF files found.\n"

    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = f"# Project Documents\n\n## 📂 File Hierarchy\n{START_MARKER}\n{END_MARKER}\n"

    if START_MARKER in content and END_MARKER in content:
        start_idx = content.find(START_MARKER) + len(START_MARKER)
        end_idx = content.find(END_MARKER)

        new_content = content[:start_idx] + "\n" + pdf_list_md + content[end_idx:]

        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md hierarchy successfully updated!")
    else:
        print(f"Error: Markers {START_MARKER} and {END_MARKER} not found in README.md")


if __name__ == "__main__":
    update_readme()
