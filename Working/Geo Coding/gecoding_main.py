import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim


data = pd.read_json("../Data handelling/supermarkets.json")

nom = Nominatim(scheme = "http")

merge_data = zip(data["Address"], data["City"], data["State"])
# geopy_location_objects = list( map(lambda x:nom.geocode("{}, {}, {}".format(x[0], x[1], x[2])),merge_data))
# data["Coordainates"] = geopy_location_objects
combine_address = [address + ", " + city +", " +state for address,city,state in merge_data]

data["Coordainates"] = pd.Series(combine_address).apply(nom.geocode).apply(lambda x : (x.latitude,x.longitude) if x is not None else None)

print( data.head())



