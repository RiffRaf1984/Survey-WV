from flask import render_template, redirect, request, session
from . import app
from .spreadsheet import *
from .forms import *
import time
time.asctime(time.localtime(time.time()))


def process_checklist(lst):
	s = str(lst)
	s = s.replace('"', '')
	s = s.replace("'", '')
	s = s.replace('[', '')
	s = s.replace(']', '')
	return s

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
        process_checklist(request.form.getlist('visit_accomodations')),
        request.form['nights_staying'],
        request.form['festivall_attendance'],
        request.form['num_events_to_attend'],
        request.form['money_spent'],
        request.form['age'],
        request.form['education'],
        request.form['income'],
        process_checklist(request.form.getlist('festivall_marketing')),
        request.form['festivall_fav'],
        request.form['festivall_suggestion'],
        request.form['email'],
        time.asctime(time.localtime(time.time())),
        session.get('volunteer')[0] + ' ' +  session.get('volunteer')[1]])
    return redirect('/submitted')
    
@app.route('/submitted')
def submitted():
    return "Survey submitted! <a href='/survey'>Submit another?</a>"

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/handle_registration', methods=["POST"])
def handle_registration():
    insert_volunteer(request.form['first_name'],
                     request.form['last_name'],
                     request.form['email'],
                     request.form['phone'],
                     request.form['password'])
    return redirect('/registered')

@app.route('/registered')
def registered():
	return "You have been registered. Please now <a href='/login'>login</a>"
	
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():
    load_user(request.form['email'], request.form['password'])
    return "Logged in! <a href='/survey'>Submit a survey?</a>"

@app.route('/logout')
def logout():
    session.pop('volunteer')
    return redirect('/')
