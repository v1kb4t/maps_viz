import osmnx as ox
import matplotlib.pyplot as plt 

# Download the data
place_name = "Shibuya, Tokyo, Japan"

# lat and lon of a specific point
home_lat, home_lon =  (35.65805566571281, 139.70163579706602)

G = ox.graph_from_place(place_name, network_type='drive', which_result=1)

# options to change widths of roads
street_widths = {'footway' : 0.5,
             'steps' : 0.5,
             'pedestrian' : 0.5,
             'path' : 0.5,
             'track' : 0.5,
             'service' : 0.5,
             'residential' : 0.5,
             'primary' : 0.6,
             'motorway' : 0.6}

# fig, ax = ox.plot_graph(G, node_size=0, street_widths=street_widths, edge_color = "dodgerblue",
#                         show = False, close = False, figsize=(15,15))
fig, ax = ox.plot_figure_ground(G, street_widths=street_widths, show=False, close=False, 
                                node_size=0, edge_color="fuchsia", figsize=(15,15))
plt.plot(home_lon, home_lat,marker = 'd', markerfacecolor = '#f28500', markeredgecolor = 'orange', markersize=10)
plt.savefig("map.png", dpi=1200, facecolor = 'black')
plt.show()