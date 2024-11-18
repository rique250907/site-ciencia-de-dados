from flask import Flask, render_template

app = Flask (__name__,template_forder ="sintenciencia/templates", static_folder = "sitencia/static")

@app.route("/")
def index():
    # return "<h1>Bom dia, professor.</h1>"
    return render_template("index.html")

