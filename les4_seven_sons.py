#!/usr/bin/env python3

############
# You will be given a string of JSON, consisting of a family tree containing people's names, genders and children.
# Your task will be to find the seventh sons of seventh sons in the family tree, and return a set of their names.
# If there are none, return an empty set.
############

import json

json_data = {
    'name': 'A',
    'gender': 'male',
    'children': [
        {'name': 'B',
         'gender': 'male',
         'children': []},
        {'name': 'C',
         'gender': 'male',
         'children': []},
        {'name': 'D',
         'gender': 'male',
         'children': []},
        {'name': 'E',
         'gender': 'male',
         'children': []},
        {'name': 'F',
         'gender': 'male',
         'children': []},
        {'name': 'G',
         'gender': 'male',
         'children': []},
        {'name': 'H',
         'gender': 'male',
         'children':[
            {'name': 'I',
             'gender': 'male',
             'children': []},
            {'name': 'J',
             'gender': 'male',
             'children': []},
            {'name': 'K',
             'gender': 'male',
             'children': []},
            {'name': 'L',
             'gender': 'male',
             'children': []},
            {'name': 'M',
             'gender': 'male',
             'children': []},
            {'name': 'N',
             'gender': 'male',
             'children': []},
            {'name': 'O',
             'gender': 'male',
             'children': []}
         ]}
    ]
}

#load json file as dict (output dict)
obj = json.loads(json.dumps(json_data))
#get all children from dict (output list)
all_children = obj["children"]
# get 6 element of the list (output dict)
seven_sone = all_children[6]
#get exact field of the dict and compare
if seven_sone.get("gender", "none") == 'male':
    print("Wubba Lubba dub-dub")
    # iteration through elements of the list
    for childrens in seven_sone.get("children", "none"):
        if childrens.get("gender", "none") == 'male':
            print(childrens.get("name", "none"))
else:
    print("7 child isn't son")
