# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:45:40 2018

Melbourne Rent Map (Google Map)

@author: Silence
"""

#################### Get Data ####################
from googleplaces import GooglePlaces
from time import sleep

api_key = "**********" #add your own api_key
GGP=GooglePlaces(api_key)

def search_text(query=None, language=None, radius=13000, location=None, pagetoken=None):
    '''
    Search by text, post a request to Google API and get the results list
    :query: key words
    :language: in which language
    :radius: search radius, in meter
    :location: the center of your search, can be a place or a coordinate
    :pagetoken: this is used to get more data
    '''
    text_query_result=GGP.text_search(query=query, language=language, radius=radius, 
                                      location=location, pagetoken=pagetoken)
    query_result_list = [text_query_result]
    while text_query_result.has_next_page_token:
        sleep(2) #has to sleep for 2 seconds, or there will be an INVALID_REQUEST error
        text_query_result=GGP.text_search(pagetoken=text_query_result.next_page_token)
        query_result_list.append(text_query_result)
    
    return query_result_list


def extract_coord(res_list):
    '''
    Extract coordinates from the query_result_list
    '''
    res=[]
    for i in res_list:
        res.extend(i.raw_response['results'])
    coord=[]
    for j in range(len(res)):
        lat=res[j]['geometry']['location']['lat']
        lon=res[j]['geometry']['location']['lng']
        coord.append((float(lat), float(lon)))
    return coord
    
#################### Draw the Map ####################
from gmplot import gmplot
import os

os.chdir('G:/MapRent')

#Burnley=(-37.827675, 145.007736)
#Clayton=(-37.924437, 145.120116)

gmap = gmplot.GoogleMapPlotter(-37.827675, 145.007736, 13) #set the initial center and zoom size

def draw_sth(search=None, location='-37.924437, 145.120116', color='#000000'):
    lats, lons=zip(*extract_coord(search_text(search, location=location))) 
    gmap.scatter(lats, lons, color, size=200, marker=False, edge_alpha=0.50, face_alpha=0.20)
    gmap.scatter(lats, lons, color, size=500, marker=False, edge_alpha=0.45, face_alpha=0.15)
    gmap.scatter(lats, lons, color, size=1000, marker=False, edge_alpha=0.40, face_alpha=0.10)
    gmap.draw('./my_map_new.html')

#################### Let's do it! ####################    
if __name__ == '__main__':
    draw_sth('woolworths', color='#0055FF') #supermarket, blue
    draw_sth('coles', color='#0055FF') #supermarket, blue
    draw_sth('commonwealth bank', color='#222222') #bank, gray
    draw_sth('ANZ', color='#222222') #bank, gray
    draw_sth('GP', color='#FF0000') #GP, red





