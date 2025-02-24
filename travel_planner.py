import numpy as np
import pandas as pd
from geopy import distance

capitals_df = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/features/travel/worldcapitals_light.csv')
capitals_df['tuple lat/lng']=list(zip(capitals_df.lat,capitals_df.lng))

print(capitals_df.head())

dic_distance = {}
length=len(capitals_df['city'])

for i in range(length):

    tuple_city_1 = capitals_df.iloc[i,3]
    name_city_1 = capitals_df.iloc[i,0]

    for j in range(i+1,length):

        tuple_city_2 = capitals_df.iloc[j,3]
        name_city_2 = capitals_df.iloc[j,0]
        
        geodesic_dist=distance.distance(tuple_city_1, tuple_city_2).km 
        dic_distance[f'{name_city_1} - {name_city_2}'] = geodesic_dist


max_aux = max(dic_distance.values())
print (list(dic_distance.keys())[list(dic_distance.values()).index(max_aux)])