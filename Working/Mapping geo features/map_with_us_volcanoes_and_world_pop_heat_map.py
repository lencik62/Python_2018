import folium
import pandas as pd

def main():
    foli_map = folium.Map(
        location = [
            43.1799011,
            -114.3509979],
        zoom_start = 6,
        tiles = "Mapbox Bright")

    fg_volcanoes = folium.FeatureGroup(name = "Volcanoes in the US")
    fg_pop = folium.FeatureGroup(name = "Simple Poplutaion Heat Map")

    map_data = pd.read_csv('../Data Handelling/Volcanoes_USA.csv')
    # data = map_data[['NAME', 'LOCATION', 'STATUS', 'ELEV', 'TYPE', 'TIMEFRAME', 'LAT', 'LON']].copy()
    data = map_data.loc[:, 'NAME':"LON"]

    for i, row in data.iterrows():
        add_volcanoes(fg_volcanoes, row)

    add_polygons_with_pop_color(fg_pop)

    add_feature_group_to_map(foli_map, fg_pop, fg_volcanoes)

    foli_map.add_child(folium.LayerControl())
    foli_map.save('map.html')

def add_feature_group_to_map(map, fg_pop, fg_volcanoes):
    map.add_child(fg_pop)
    map.add_child(fg_volcanoes)

def add_polygons_with_pop_color(feature_group):
    feature_group.add_child(
        folium.GeoJson(
            data = open(
                        '../Data Handelling/world Map data.json',
                        'r',
                        encoding = 'utf-8-sig'
                    ).read(),
                    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

def add_volcanoes(feature_group, row):
    feature_group.add_child(
     folium.CircleMarker(
         location = [row['LAT'], row['LON']],
         radius = 6,
         popup = str(
             "Name:{} \\n At:{} \\n Status:{} \\n Elevation:{}m \\n Type:{}".format(
                 row['NAME'].replace("'", 'ʹ').upper(),
                 row['LOCATION'],
                 row['STATUS'],
                 row['ELEV'],
                 row['TYPE'])),
         fill_color = color_producer(row['ELEV']),
         fill = True,
         color = 'grey',
         fill_opacity = 0.7))

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
if __name__ == '__main__':
    main()
