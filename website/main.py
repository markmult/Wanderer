from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")