"""App entry point."""

from flask import render_template
import markdown
from flask import Flask
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__,
            template_folder="src/eventum_website/templates",
            static_folder="src/eventum_website/static")

import_eventum = """
from eventum import talent, ai, consulting
""".strip()


@app.route("/")
def home():
    """Landing page route."""
    nav = [
        # dict(name='asdfasdfdsa', url='/')
    ]
    from_eventum = highlight(import_eventum, PythonLexer(), HtmlFormatter())

    with open('src/eventum_website/md/home.md', 'r') as markdown_file:
        text = markdown_file.read()
    html = markdown.markdown(text)
    html = html.replace(
        '{{ from_eventum }}', from_eventum,
    )
    # code = 'print "Hello World"'
    # print(from_eventum)

    return render_template(
        "home.jinja2",
        nav=nav,
        html=html,
        # from_eventum=from_eventum,
        style=HtmlFormatter().get_style_defs('.highlight')
        # description="Smarter page templates with Flask & Jinja.",
    )
