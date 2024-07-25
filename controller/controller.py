import flask

app = flask.Flask(__name__)

@app.get("/")
def pagina_inicial():
    return flask.render_template("index.html")