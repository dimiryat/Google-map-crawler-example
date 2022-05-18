# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:33:54 2022

@author: DennisLin
"""

import googlemaps
from pprint import pprint

API_KEY = 'AIzaSyBnIM9ngbSNrs6climnQ8B9HwjH6c4kh_4'

gmaps =  googlemaps.Client(key=API_KEY)
geocode_result = gmaps.geocode("台北市")
loc = geocode_result[0]['geometry']['location']
places = gmaps.places_nearby(keyword="拉麵", location = loc, radius=2500)['results']

print("台北市中心半徑 2500 公尺的拉麵店數量: "+str(len(places)))
print("第一筆資料")

p = gmaps.place(place_id=places[0]['place_id'], language='zh-TW')
pprint(p)