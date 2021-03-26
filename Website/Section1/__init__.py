from flask import Blueprint, render_template

Website_Section1_bp = Blueprint('Website_Section1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@Website_Section1_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")

