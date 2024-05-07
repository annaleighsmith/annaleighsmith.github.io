import os
import markdown
import glob


def read_template(template_file):
    with open(template_file, "r") as f:
        return f.read()


def convert_file(md_file, output_dir):
    with open(md_file, "r") as f:
        raw_md = f.read()

    html_content = markdown.markdown(raw_md, extensions=["extra", "smarty"])
    file_name = os.path.splitext(os.path.basename(md_file))[0] + ".html"
    output_file = os.path.join(output_dir, file_name)
    print(output_file)
    with open(output_file, "w") as f:
        f.write(DEFAULT_TEMPLATE_FILE.format(html_content))

    return output_file


def create_index(index_dir):
    md_files = glob.glob(f"{index_dir}/*.md")
    index_content = "<h1>Index</h1>"
    for md_file in md_files:
        file_name = os.path.splitext(os.path.basename(md_file))[0]
        index_content += f'<a href="{file_name}.html">{file_name}</a><br>'

    with open(os.path.join(index_dir, "index.html"), "w") as f:
        f.write(DEFAULT_TEMPLATE_FILE.format(index_content))


if __name__ == "__main__":

    DEFAULT_TEMPLATE_FILE = read_template("templates/default.html")
    convert_file("public/index.md", "public")
    md_posts = glob.glob("public/posts/*.md")
    for f in md_posts:
        convert_file(f, "public/posts/")
    create_index("public/posts")
    create_index("public")
