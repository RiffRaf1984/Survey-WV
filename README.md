### WV FestivAll Survey Web App
This app is intended to be used by admin level volunteers to log in and collect surveys from FestivAll goers about their demographics and experience.

## VIEWS
* login - where volunteer will log in to begin collecting surveys
* survey - a form where users will input data and submit it to database
* admin surveys - page for admins to view and edit surveys
* analytics - page to visualize data

## DATABASE
  * id
  * email
  * age
  * sex
  * event_attended
  * 1st_time
  * event_attendence
  * recommendations
...

## SURVEY
* event_name
	* prompt = "Name of Event"
	* input = multiple choice
		* "Art Fair"
		* "Air Play"
		* "Art Parade"
		* "ArtWalk"
		* "Cabaret FestivAll"
		* "Carriage Trail"
		* "Chili Cookoff"
		* "Civic Chorus"
		* "CLOG"
		* "CYAC"
		* "Dance Gala"
		* "Drum Circle"
		* "Festiv-ALT"
		* "Go to Hale"
		* "Ice Cream Social"
		* "Juneteenth"
		* "Live on the Levee"
		* "Mayor's Concert"
		* "Mountain Stage"
		* "Taste"
		* "Wine & All That Jazz"
		* "Woofstock & Wieners"
		* "Other"
* home_zip
	* prompt = "What is your home zip code?"
	* input = valid zip code
* visit_accomodations
	* prompt = "If you are visiting:"
	* input = multiple choice
		* "I am staying with family or friends"
		* "I am staying in paid lodging"
* nights_staying
	* prompt = "How many nights are you staying?"
	* input = integer
* festivall_attendance
	prompt = "Have you attended FestivALL in the past?"
	input = multiple choice
		* "yes"
		* "no"
* num_events_to_attend
	* prompt = "How many events are you likely to attend this year?"
	* input = integer
* money_spent
	* prompt = "Not counting lodging, approximately how much will you spend here during FestivALL?"
	* input = USD currency
* age
	* prompt = "What is your age?"
	* input = multiple choice
		* "Pre-teen / teen"
		* "20-29"
		* "30-39"
		* "40-49"
		* "50-59"
		* "60-69"
		* "70+"
* education
	* prompt = "What is your education level?"
	* input = multiple choice
		* "High School"
		* "Some College"
		* "College Graduate"
		* "Graduate Degree"
* income
	* prompt = "What is your household income level?"
	* input = multiple choice
		* "less than $30,000"
		* "$30,000 - $49,999"
		* "$50,000 - $69,999"
		* "$70,000 - $99,999"
		* "more than $100,000"
* festivall_marketing
	* prompt = "Where did you hear about FestivALL? (check all that apply)"
	* input = multiple choice (check all that apply)
		* "WV Gazette Mail"
		* "Charleston Radio"
		* "WV Public Broadcasting"
		* "WSAZ"
		* "State Journal"
		* "WTSQ Radio"
		* "WNKU Radio"
		* "WOUB Radio"
		* "WV State Visitor's Guide"
		* "Herald Tri-State Visitors Guide"
		* "WV Living Magazine"
		* "South Hills Living Magazine"
		* "FestivALL Print Brochure/Schedule"
		* "FestivALL Website"
		* "Facebook"
		* "Twitter"
		* "Instagram"
		* "Friends/Family"
		* "Other: " (user input)
* festivall_fav
	* prompt = "What do you like best about FestivALL?"
	* input = essay
* festivall_suggestion
	* prompt = "What would you like to see at FestivALL?"
	* input = essay
* email
	* prompt = "Enter your email address for a chance to win a FestivALL Fall ticket package"
	* input = valid email address
