import json


# Opens json file for fire data to be read in the program.
in_file = open('US_fires_9_1.json','r')

# Opens out file for the exact data we want to pull from the file.  
out_file = open('readable_fire_data_9_1.json','w')

fire_data = json.load(in_file)

json.dump(fire_data,out_file,indent=4)

list_of_fires = fire_data[:]

print(type(list_of_fires))

print(len(list_of_fires))

# Create empty lists for the brightness level and coordinates of each location in the data file. 
brights,lons,lats,hover_texts = [],[],[],[]

# Runs through each location and appends the brightness factor and coordinates of each location that has a brightness factor greater
# than 450. 
for f in list_of_fires:
    bright = f['brightness']
    lon = f['longitude']
    lat = f['latitude']

    if bright > 450:
        brights.append(bright)
        lons.append(lon)
        lats.append(lat)

print('Brightness')
print(brights[:10])

print('Lons')
print(lons[:10])

print('Lats')
print(lats[:10])

# Import plotly to plot map of the locations appended. 
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Creates the map of the locations plotted. 
data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size':[bright / 40 for bright in brights],
        'color':brights,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]

my_layout = Layout(title='Global Wildfires')

fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='global_wildfires.html')