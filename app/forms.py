from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, DecimalField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length


event_list = [
    ("Art Fair", ''), 
    ("Air Play", ''),
    ("Art Parade", ''),
    ("ArtWalk", ''),
    ("Cabaret FestivAll", ''),
    ("Carriage Trail", ''),
    ("Chili Cookoff", ''),
    ("Civic Chorus", ''),
    ("CLOG", ''),
    ("CYAC", ''),
    ("Dance Gala", ''),
    ("Drum Circle", ''),
    ("Festiv-ALT", ''),
    ("Go to Hale", ''),
    ("Ice Cream Social", ''),
    ("Juneteenth", ''),
    ("Live on the Levee", ''),
    ("Mayor's Concert", ''),
    ("Mountain Stage", ''),
    ("Taste", ''),
    ("Wine & All That Jazz", ''),
    ("Woofstock & Wieners", ''),
    ("Other", '')
]

marketing_sources_list = [
    ("WV Gazette Mail", ''),
    ("Charleston Radio", ''),
    ("WV Public Broadcasting", ''),
    ("WSAZ", ''),
    ("State Journal", ''),
    ("WTSQ Radio", ''),
    ("WNKU Radio", ''),
    ("WOUB Radio", ''),
    ("WV State Visitor's Guide", ''),
    ("Herald Tri-State Visitors Guide", ''),
    ("WV Living Magazine", ''),
    ("South Hills Living Magazine", ''),
    ("FestivALL Print Brochure/Schedule", ''),
    ("FestivALL Website", ''),
    ("Facebook", ''),
    ("Twitter", ''),
    ("Instagram", ''),
    ("Friends/Family", ''),
    ("Other", '')
]
    
accomodations_list = [
    ("I am staying with family or friends", ''),
    ("I am staying in paid lodging", '')
]

education_list = [
    ("High School", ''),
    ("Some College", ''),
    ("College Graduate", ''),
    ("Graduate Degree", '')
]

age_list = [
    ("Pre-teen / teen", ''),
    ("20-29", ''),
    ("30-39", ''),
    ("40-49", ''),
    ("50-59", ''),
    ("60-69", ''),
    ("70+", '')
]

class Survey(FlaskForm):
    #StringField('name', validators=[DataRequired()])
    event_name = RadioField('Name of Event', choices=event_list)
    home_zip = IntegerField("What is your home zip code?", validators=[Length(5)])
    visit_accomodations = RadioField("If you are visiting:", choices=accomodations_list)
    nights_staying =  IntegerField("How many nights are you staying?")
    festivall_attendance = BooleanField("Have you attended FestivALL in the past?")
    num_events_to_attend = IntegerField("How many events are you likely to attend this year?")
    money_spent = DecimalField("Not counting lodging, approximately how much will you spend here during FestivALL?")
    age = RadioField("What is your age?", choices=age_list)
    education = RadioField("What is your education level?", choices=education_list)
    festivall_marketing = SelectField("Where did you hear about FestivALL? (check all that apply)", choices=marketing_sources_list)
    festivall_fav = StringField("What do you like best about FestivALL?")
    festivall_suggestion = StringField("What would you like to see at FestivALL?")
    email = StringField("Enter your email address for a chance to win a FestivALL Fall ticket package")
