from flask import Flask
from flask import render_template

from route.editor import editor
from route.home import home
from route.index import index


app = Flask(__name__)
app.register_blueprint(editor.router)
app.register_blueprint(home.router)
app.register_blueprint(index.router)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
