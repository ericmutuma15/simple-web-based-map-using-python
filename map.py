# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 14:03:03 2021

@author: mutuma
"""

from map.folium import folium

m= folium.map(location= [-1.292066, 36.821945], zoom_start = 6)
m.save()
