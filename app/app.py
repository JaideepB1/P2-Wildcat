from flask import Flask
from Website.Section1 import y2021_tri1_bp
from Website.Section2 import y2021_tri2_bp
from y2021.tri3.app import y2021_tri3_bp


app = Flask(__name__)
app.register_blueprint(y2021_tri1_bp, url_prefix='/Website/Section 1')
app.register_blueprint(y2021_tri2_bp, url_prefix='/Website/Section 2')
app.register_blueprint(y2021_tri3_bp, url_prefix='/Website/Section 3')


@app.route('/')
def index():
    return "Project"


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
