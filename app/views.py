from flask import render_template
from . import app
from .spreadsheet import *
from .forms import *

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/survey")
def survey():
    form = Survey()
    if form.validate_on_submit():
        return redirect('/submitted')
    return render_template('survey.html', form=form)

@app.route('/submitted')
def submit():
    return "Survey submitted! <a href='/survey'>Submit another?</a>"
