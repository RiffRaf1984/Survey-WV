from flask import render_template, redirect, request
from . import app
from .spreadsheet import *
from .forms import *

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/survey")
def survey():
    form = Survey()
    return render_template('survey.html', form=form)

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    insert_survey([request.form['event_name'],
        request.form['home_zip'],
        request.form['visit_accomodations'],
        request.form['nights_staying'],
        request.form['festivall_attendance'],
        request.form['num_events_to_attend'],
        request.form['money_spent'],
        request.form['age'],
        request.form['education'],
        request.form['income'],
        request.form['festivall_marketing'],
        request.form['festivall_fav'],
        request.form['festivall_suggestion'],
        request.form['email']])
    return redirect('/submitted')
    
@app.route('/submitted')
def submitted():
    return "Survey submitted! <a href='/survey'>Submit another?</a>"
