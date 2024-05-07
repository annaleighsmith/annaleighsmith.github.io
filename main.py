import os
import markdown


# Define HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>My Great Site</title>
</head>
<body>
{}
</body>
</html>
"""


def convert_file(md_file, output_dir="public"):
    with open(md_file, "r") as f:
        raw_md = f.read()

    html_content = markdown.markdown(raw_md, extensions=["extra", "smarty"])
    file_name = os.path.splitext(os.path.basename(md_file))[0] + ".html"
    output_file = os.path.join(output_dir, file_name)
    print(output_file)
    with open(output_file, "w") as f:
        f.write(HTML_TEMPLATE.format(html_content))

    return output_file


convert_file("index.md", "")
