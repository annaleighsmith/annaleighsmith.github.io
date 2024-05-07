import os
import markdown
import glob


def read_template(template_file):
    with open(template_file, "r") as f:
        return f.read()


def convert_file(md_file):
    """Create a new HTML file from a markdown file"""
    with open(md_file, "r") as f:
        raw_md = f.read()
    html_content = markdown.markdown(raw_md, extensions=["extra", "smarty"])
    file_name = os.path.splitext(os.path.basename(md_file))[0] + ".html"
    output_file = os.path.join(os.path.dirname(md_file), file_name)
    with open(output_file, "w") as f:
        f.write(DEFAULT_TEMPLATE_FILE.format(html_content))
    return output_file


# def create_index(index_dir):
#     md_files = glob.glob(f"{index_dir}/*.md")
#     index_content = "<h1>Index</h1>"
#     for md_file in md_files:
#         file_name = os.path.splitext(os.path.basename(md_file))[0]
#         index_content += f'<a href="{file_name}.html">{file_name}</a><br>'
#
#     with open(os.path.join(index_dir, "index.html"), "w") as f:
#         f.write(DEFAULT_TEMPLATE_FILE.format(index_content))


def create_index(index_dir):
    files_and_dirs = glob.glob(f"{index_dir}/*")
    index_content = ""
    for item in files_and_dirs:
        if os.path.isfile(item) and item.endswith(".md"):
            file_name = os.path.splitext(os.path.basename(item))[0]
            index_content += f'<a href="{file_name}.html">{file_name}</a><br>'
        elif os.path.isdir(item):
            dir_name = os.path.basename(item)
            index_content += f'<a href="{dir_name}/index.html">{dir_name}</a><br>'

    with open(os.path.join(index_dir, "index.html"), "w") as f:
        f.write(DEFAULT_TEMPLATE_FILE.format(index_content))


if __name__ == "__main__":
    DEFAULT_TEMPLATE_FILE = read_template("templates/default.html")

    for filename in glob.iglob("public/**", recursive=True):
        if os.path.isfile(filename):
            if filename.endswith(".md"):
                convert_file(filename)
        if os.path.isdir(filename):
            create_index(filename)
            # get every directory or .md file
