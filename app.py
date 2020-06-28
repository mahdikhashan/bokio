from flask import Flask
from flask import render_template

from route.editor import editor


app = Flask(__name__)
app.register_blueprint(editor.router)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
