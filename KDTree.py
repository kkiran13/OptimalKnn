from scipy import spatial
import numpy as np
import datetime
"""
class GeographicalInfo :
    # Simple class that stores geographic data of a given place ID
    def __init__(self, lattitude, longitude, category, storeName) :
        self.lat = lattitude
        self.long = longitude
        self.category = category
        self.storeName = storeName
"""
        
def main():
    # parse command line options
    file = '/home/karthik/Documents/CSE603/data/Locate_sample.txt'
    data = []
    geoDict = {}
    start = datetime.datetime.now()
    #with open(file) as f:
    for line in open(file):
            geoDataArray = line.rstrip('\n').split(';')  #removes the newline character from each input line
            placeID = geoDataArray[0].rstrip('*')  #gets place ID from input file
            locData = geoDataArray[1].lstrip('*(').rstrip(')*').split(',') #splits the values in the tuple of input
            locTuple = (float(locData[0].strip()), float(locData[1].strip()))  #makes a tuple of latitude and longitude
                # Open the text file and load the latitude and longitude of place into data
            data.append(locTuple)  #load latitude and longitude into the data LIST
            # Load a dictionary with key as place ID and location info as value    
            geoDict[placeID] = locData #Populate the dictionary with Place ID as key and tuple (lat,longitude) as value
    #Create the KD Tree
    tree = spatial.KDTree(data)
    f = open('/home/karthik/Documents/CSE603/data/Sampleout.txt', 'r+')
    for item in geoDict:
        sourceLatitude = float(geoDict[item][0].strip())
        sourceLongitude = float(geoDict[item][1].strip())
        #f.write('****************')
        f.write('Source:'+ str(sourceLatitude) + str(sourceLongitude))
        #Find all points within distance r of point(s) x.
        f.write( str([data[i] for i in tree.query_ball_point([sourceLatitude, sourceLongitude], 0.01)])+'\n') 
        #f.write('****************')
    f.close()
    end = datetime.datetime.now()
    print '\n'
    print start
    print end
    print end-start
        
if __name__ == "__main__":
    main()