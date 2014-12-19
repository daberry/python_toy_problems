# Create a list comprehension that acts over a set of JSON blobs
# where each blob contains a definition of a person 
# ( firstName, lastName, address, phone number), and outputs in 
# sorted order by first name only the people who share a common 
# last name 

data = [ 
{ 
"firstName": "Davidson", 
"lastName": "Moran", 
"phone": "+1 (939) 481-3292", 
"address": "918 Bergen Place, Utting, Indiana, 3856" 
}, 
{ 
"firstName": "Keri", 
"lastName": "Cole", 
"phone": "+1 (883) 461-3165", 
"address": "916 Euclid Avenue, Brutus, Arizona, 197" 
}, 
{ 
"firstName": "Christina", 
"lastName": "Horn", 
"phone": "+1 (971) 499-3889", 
"address": "488 Dobbin Street, Gardners, Montana, 7980" 
}, 
{ 
"firstName": "Frye", 
"lastName": "Sanders", 
"phone": "+1 (985) 432-3063", 
"address": "194 Alabama Avenue, Hessville, South Dakota, 6050" 
}, 
{ 
"firstName": "Hyde", 
"lastName": "Cole", 
"phone": "+1 (827) 587-3720", 
"address": "734 Ridgewood Avenue, Saticoy, Maryland, 5789" 
}, 
{ 
"firstName": "Peck", 
"lastName": "Flowers", 
"phone": "+1 (914) 403-2851", 
"address": "712 Sutton Street, Joes, Utah, 4853" 
}, 
{ 
"firstName": "Cora", 
"lastName": "Cole", 
"phone": "+1 (822) 436-3401", 
"address": "600 Vandervoort Avenue, Suitland, Colorado, 3605" 
} 
] 

same_last_names = [person for person in data if count_last_names(person, data) > 1].sort()

def count_last_names(person, data):
    count = 0
    for item in data:
        if item["lastName"] == person["lastName"]:
            count += 1
    return count 
