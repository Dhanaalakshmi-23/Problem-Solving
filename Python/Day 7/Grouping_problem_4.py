#3. Group cities by state and find the city with highest population in each state.
# sample input :
# [
#  ("Chennai", "Tamil Nadu", 7000000),
#  ("Coimbatore", "Tamil Nadu", 2000000),
#  ("Mumbai", "Maharashtra", 12000000),
#  ("Pune", "Maharashtra", 5000000),
#  ("Mysore", "Karnataka", 1200000)
# ]

# output :
# {
#  'Tamil Nadu': ['Chennai', 'Coimbatore'],
#  'Maharashtra': ['Mumbai', 'Pune'],
#  'Karnataka': ['Mysore']
# }

# highest population city in Tamil Nadu : Chennai
# highest population city in Maharashtra : Mumbai
# highest population city in Karnataka : Mysore

def cityDetails(data):
    groups = {}
    highest = {}
    
    for city, state, population in data:
        
        groups.setdefault(state, []).append(city)
        
        if state not in highest or population > highest[state][1]:
            highest[state] = (city, population)
    
    print(groups)
    
    for state in highest:
        print("highest population city in", state, ":", highest[state][0])


cities = [
    ("Chennai", "Tamil Nadu", 7000000),
    ("Coimbatore", "Tamil Nadu", 2000000),
    ("Mumbai", "Maharashtra", 12000000),
    ("Pune", "Maharashtra", 5000000),
    ("Mysore", "Karnataka", 1200000)
]

cityDetails(cities)