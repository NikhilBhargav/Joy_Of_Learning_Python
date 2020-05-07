###
# GPS tracker in Python
###

import csv
from gmplot import gmplot


#USe googlemaps API for GPS		
gmap=gmplot.GoogleMapPlotter(28.689169,77.324448,17)
gmap.coloricon="https://www.googlemapsmarkers.com/v1/%s/"

#Open route file and create iterator
with open('route.csv','r') as source:
	reader=csv.reader(source)
	count=0
	
	#Read each line and print lat /long
	for row in reader:
		lat=float(row[0])
		long=float(row[1])
		if(count==0):
			gmap.marker(lat,long,'yellow')
			#Move to next locationcount
			count=1
		else:
			gmap.marker(lat,long,'blue')

#Last Location is Red
gmap.marker(lat,long,'red')
#Draw the map
gmap.draw("mymap.html")