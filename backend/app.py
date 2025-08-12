from pathlib import Path
from flask import Flask, send_from_directory
from api.routes import api_bp


def create_app() -> Flask:
    base_dir = Path(__file__).resolve().parent
    frontend_dir = (base_dir.parent / "frontend").resolve()

    app = Flask(
        __name__,
        static_folder=str(frontend_dir),
        static_url_path="",
    )

    app.register_blueprint(api_bp)

    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


