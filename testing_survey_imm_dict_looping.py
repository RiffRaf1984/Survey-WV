mutabledict = dict([('festivall_suggestion', 'asdf'),
                    ('nights_staying', '3'),
                    ('age', '30-39'),
                    ('email', 'patrickmckowen1@gmail.com'),
                    ('home_zip', '25314'),
                    ('festivall_fav', 'asdaf'),
                    ('festivall_marketing', 'WV Living Magazine'),
                    ('festivall_marketing', 'FestivALL Print Brochure/Schedule'),
                    ('festivall_marketing', 'Facebook'),
                    ('num_events_to_attend', '3'),
                    ('event_name', 'Art Fair'),
                    ('money_spent', '3.50'),
                    ('visit_accomodations', 'I am staying with family or friends'),
                    ('education', 'Some College'),
                    ('income', '$50,000 - $69,999'),
                    ('festivall_attendance', 'on')])
#print(mutabledict)

immutable = frozenset(mutabledict.items())

#print(immutable)

marketings = []

for i in immutable:
    if i[0] is 'festivall_marketing':
        marketings.append(i)
print(marketings)
