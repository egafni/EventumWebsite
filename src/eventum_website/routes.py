"""Route declaration."""
from flask import current_app as app
from flask import render_template
import markdown

@app.route("/")
def home():
    """Landing page route."""
    nav = [
    ]

    with open('src/eventum_website/md/home.md', 'r') as markdown_file:
        text = markdown_file.read()
    html = markdown.markdown(text)

    return render_template(
        "home.jinja2",
        nav=nav,
        html=html
        # description="Smarter page templates with Flask & Jinja.",
    )
