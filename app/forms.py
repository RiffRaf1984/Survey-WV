from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, DecimalField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length

event_list = [
    ("Art Fair", 'Art Fair'), 
    ("Air Play", 'Air Play'),
    ("Art Parade", 'Art Parade'),
    ("ArtWalk", 'ArtWalk'),
    ("Cabaret FestivAll", 'Cabaret FestivAll'),
    ("Carriage Trail", 'Carriage Trail'),
    ("Chili Cookoff", 'Chili Cookoff'),
    ("Civic Chorus", 'Civic Chorus'),
    ("CLOG", 'CLOG'),
    ("CYAC", 'CYAC'),
    ("Dance Gala", 'Dance Gala'),
    ("Drum Circle", 'Drum Circle'),
    ("Festiv-ALT", 'Festiv-ALT'),
    ("Go to Hale", 'Go to Hale'),
    ("Ice Cream Social", 'Ice Cream Social'),
    ("Juneteenth", 'Juneteenth'),
    ("Live on the Levee", 'Live on the Levee'),
    ("Mayor's Concert", "Mayor's Concert"),
    ("Mountain Stage", 'Mountain Stage'),
    ("Taste", 'Taste'),
    ("Wine & All That Jazz", 'Wine & All That Jazz'),
    ("Woofstock & Wieners", 'Woofstock & Wieners'),
    ("Other", 'Other')
]

marketing_sources_list = [
    ("WV Gazette Mail", 'WV Gazette Mail'),
    ("Charleston Radio", 'Charleston Radio'),
    ("WV Public Broadcasting", 'WV Public Broadcasting'),
    ("WSAZ", 'WSAZ'),
    ("State Journal", 'State Journal'),
    ("WTSQ Radio", 'WTSQ Radio'),
    ("WNKU Radio", 'WNKU Radio'),
    ("WOUB Radio", 'WOUB Radio'),
    ("WV State Visitor's Guide", "WV State Visitor's Guide"),
    ("Herald Tri-State Visitors Guide", 'Herald Tri-State Visitors Guide'),
    ("WV Living Magazine", 'WV Living Magazine'),
    ("South Hills Living Magazine", 'South Hills Living Magazine'),
    ("FestivALL Print Brochure/Schedule", 'FestivALL Print Brochure/Schedule'),
    ("FestivALL Website", 'FestivALL Website'),
    ("Facebook", 'Facebook'),
    ("Twitter", 'Twitter'),
    ("Instagram", 'Instagram'),
    ("Friends/Family", 'Friends/Family'),
    ("Other", 'Other')
]
    
accomodations_list = [
    ("I am staying with family or friends", 'I am staying with family or friends'),
    ("I am staying in paid lodging", 'I am staying in paid lodging')
]

education_list = [
    ("High School", 'High School'),
    ("Some College", 'Some College'),
    ("College Graduate", 'College Graduate'),
    ("Graduate Degree", 'Graduate Degree')
]

age_list = [
    ("Pre-teen / teen", 'Pre-teen / teen'),
    ("20-29", '20-29'),
    ("30-39", '30-39'),
    ("40-49", '40-49'),
    ("50-59", '50-59'),
    ("60-69", '60-69'),
    ("70+", '70+')
]

income_list = [
    ("less than $30,000", "less than $30,000"),
    ("$30,000 - $49,999", "$30,000 - $49,999"),
    ("$50,000 - $69,999", "$50,000 - $69,999"),
    ("$70,000 - $99,999", "$50,000 - $69,999"),
    ("more than $100,000", "$50,000 - $69,999")
]
		
class Survey(FlaskForm):
    event_name = RadioField('Name of Event', choices=event_list)
    home_zip = StringField("What is your home zip code?", validators=[Length(5)])
    visit_accomodations = RadioField("If you are visiting:", choices=accomodations_list)
    nights_staying =  IntegerField("How many nights are you staying?")
    festivall_attendance = BooleanField("Have you attended FestivALL in the past?")
    num_events_to_attend = IntegerField("How many events are you likely to attend this year?")
    money_spent = DecimalField("Not counting lodging, approximately how much will you spend here during FestivALL?")
    age = RadioField("What is your age?", choices=age_list)
    education = RadioField("What is your education level?", choices=education_list)
    income = RadioField("What is your household income level?", choices = income_list)
    festivall_marketing = SelectField("Where did you hear about FestivALL? (check all that apply)", choices=marketing_sources_list)
    festivall_fav = StringField("What do you like best about FestivALL?")
    festivall_suggestion = StringField("What would you like to see at FestivALL?")
    email = StringField("Enter your email address for a chance to win a FestivALL Fall ticket package")
