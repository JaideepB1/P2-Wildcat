from flask import Blueprint, render_template

WebsiteSection2_bp = Blueprint('y2021_tri2', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@WebsiteSection2_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/cspcbproject")
