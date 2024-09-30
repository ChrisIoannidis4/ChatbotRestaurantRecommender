import random
import csv
import pandas as pd
import os
from keyword_mapping import extract_preferences

def update_restaurant_info(added_features_dict, restaurant_info_path):
    df = pd.read_csv(restaurant_info_path)
    for feature in added_features_dict.keys():
        df[feature] = df.apply(lambda x: random.choice(added_features_dict[feature]), axis=1)
    # update_name_split = restaurant_info_path.split('/')
        
    directory = os.path.dirname(restaurant_info_path)
    df.to_csv(directory + '/updated_restaurant_info.csv', index=False)


added_features = {
    "quality" : ["bad food", "good food"],
    "crowdedness": ["busy", "not busy"],
    "length_of_stay": ["short stay", "long stay"]
}

# update_restaurant_info(added_features, 'data/restaurant_info.csv')

additional_preferences = {
 'romantic' : ['romantic'],
 'assigned seats' : ['assigned seats'],
 'children' : ['children'],
 'touristic' : ['touristic']
}

selected_added_pref = extract_preferences('i would like a romantic restaurant but touristic too', additional_preferences)
print(selected_added_pref)


def inference_rules(add_preferences):
#pricerange,area,food,quality,crowdedness,length_of_stay
    filters_true={}
    filters_false={}
    if add_preferences["touristic"]:
        filters_true['quality'] = 'good food'
        filters_true['pricerange']= 'cheap'
        filters_false['food'] = 'romanian'
    if add_preferences['assigned seats']:
        filters_true['crowdedness']='busy'
    if add_preferences['children']:
        filters_true['length_of_stay'] = 'short stay'
    if add_preferences['romantic']:
        filters_true['length_of_stay'] = 'long stay'
        filters_false['crowdedness'] = 'busy'
    
    return filters_true, filters_false

# filters_true, filters_false= 
print(inference_rules(selected_added_pref))



# query_restaurant(preferences, , output = 'list', version ='eq'):
#