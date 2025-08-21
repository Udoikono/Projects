from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return (render_template("Webpage.html", name=username, post_id=post_id),
            # "<p>Hello, This is Akaninyene Udoikono trial website<p>")

#
# @app.route("/blog")
# def hello_name():
#     return "<p>This blog is design for the enlightening the community on the importance of communal integration and general tolerance of one another</p>"
#
# @app.route("/blog/name")
# def blog_name():
#     return render_template("Webpage.html")


