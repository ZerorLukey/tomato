from flask import request
from flask import render_template
from flask import current_app as app
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')

    @app.route("/", methods=["GET", "POST"])
    def home_route():
        if request.method == "POST":
            video_url = request.form.get("video_url")
            app.logger.info(f"Received video URL: {video_url}")
        return render_template("home.html")

    return app