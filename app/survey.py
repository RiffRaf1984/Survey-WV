from lxml import etree as ET
from lxml.builder import E
class Survey_item(object):
    
    def __init__(self, prompt, input_type, choices=None):
        self.prompt = prompt
        self.input_type = input_type
        self.choices = choices

    def render_html(self):
        if self.input_type == '
        
class Survey(object):
    ''' '''
    def __init__(self, ):
        event_name
        home_zip
        visit_accomodations
        nights_staying
        festivall_attendance
        num_events_to_attend
        money_spent

columns = ['Event Name', 'Home Zipcode', 'Visit Accomodations', 'Nights Staying', 'Have Attended Festivall in the Past', 'Number of Events Expecting to Attend', 'Expected non-lodging Expenses', 'Age', 'Education', 'Income', 'Heard of Festival from', 'Favorite Part of Festivall', 'Seggestions for Festivall','Email']



# survey in dictionary
survey_dict = [
{'event_name' : {
 'prompt' : "Name of Event"
 'input' :
   {'type' : 'multiple choice',
    'options' : 
     ["Art Fair",
      "Air Play",
      "Art Parade",
      "ArtWalk",
      "Cabaret FestivAll",
      "Carriage Trail",
      "Chili Cookoff",
      "Civic Chorus",
      "CLOG",
      "CYAC",
      "Dance Gala",
      "Drum Circle",
      "Festiv-ALT",
      "Go to Hale",
      "Ice Cream Social",
      "Juneteenth",
      "Live on the Levee",
      "Mayor's Concert",
      "Mountain Stage",
      "Taste",
      "Wine & All That Jazz"
      "Woofstock & Wieners"
      "Other"
     ]
   },
 
{'home_zip' :
  {'prompt' : "What is your home zip code?",
   'input' :
    {'type' : 'text'}
  }
},
 
{'visit_accomodations' :
  'prompt' : "If you are visiting:"
  'input' :
    { 'type' : 'multiple choice',
          'choices' : [
  "I am staying with family or friends",
"I am staying in paid lodging"]

}},
 
{'nights_staying' :
  {'prompt' : "How many nights are you staying?",
   'input' { 'type' : 'integer'}
  }
}
 
{'festivall_attendance' : {'prompt' : "Have you attended FestivALL in the past?"}
 'input' : {'type' : 'multiple choice',  * "yes" * "no"}

{
num_events_to_attend
prompt = "How many events are you likely to attend this year?"
input = integer

money_spent
prompt = "Not counting lodging, approximately how much will you spend here during FestivALL?"
input = USD currency
age
prompt = "What is your age?"
input = multiple choice
"Pre-teen / teen"
"20-29"
"30-39"
"40-49"
"50-59"
"60-69"
"70+"
education
prompt = "What is your education level?"
input = multiple choice
"High School"
"Some College"
"College Graduate"
"Graduate Degree"
income
prompt = "What is your household income level?"
input = multiple choice
"less than $30,000"
"$30,000 - $49,999"
"$50,000 - $69,999"
"$70,000 - $99,999"
"more than $100,000"
festivall_marketing
prompt = "Where did you hear about FestivALL? (check all that apply)"
input = multiple choice (check all that apply)
"WV Gazette Mail"
"Charleston Radio"
"WV Public Broadcasting"
"WSAZ"
"State Journal"
"WTSQ Radio"
"WNKU Radio"
"WOUB Radio"
"WV State Visitor's Guide"
"Herald Tri-State Visitors Guide"
"WV Living Magazine"
"South Hills Living Magazine"
"FestivALL Print Brochure/Schedule"
"FestivALL Website"
"Facebook"
"Twitter"
"Instagram"
"Friends/Family"
"Other: " (user input)
festivall_fav
prompt = "What do you like best about FestivALL?"
input = essay
festivall_suggestion
prompt = "What would you like to see at FestivALL?"
input = essay
email
prompt = "Enter your email address for a chance to win a FestivALL Fall ticket package"
input = valid email address
