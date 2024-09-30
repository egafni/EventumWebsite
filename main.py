"""App entry point."""

if __name__ == "__main__":
    """Construct the core application."""
    from flask import Flask

    app = Flask(__name__,
                template_folder="src/eventum_website/templates",
                static_folder="src/eventum_website/static")

    with app.app_context():
        # return app
        from eventum_website import routes

        app.run(host="0.0.0.0", port=6415, debug=True)
