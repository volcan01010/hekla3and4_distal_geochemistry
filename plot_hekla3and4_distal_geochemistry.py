# coding: utf-8

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd


def main():
    """
    Plot Hekla 3 and 4 geochemistry map
    """
    # Load data
    df = pd.read_csv('hekla3and4_distal_geochemistry.csv')
    df['classification'] = [classify_composition(x) for x in df['SiO2']]

    for tephra in ['Hekla 4 Tephra', 'Hekla 3 Tephra']:
        for classification in ['Rhyolite', 'Dacite', 'Andesite']:

            # Get coordinates
            (lon_found, lat_found,
             lon_absent, lat_absent) = get_coordinates(df, tephra,
                                                       classification)

            # Create figure
            print("Plotting {} {}".format(tephra, classification))
            plt.figure(figsize=(7, 7))
            m = prepare_basemap()

            # Plot sample locations
            m.scatter(lon_found, lat_found, latlon=True,
                      color='red', s=60, zorder=3,
                      label='{}'.format(classification))
            m.scatter(lon_absent, lat_absent, latlon=True,
                      color='orange', s=35, zorder=2,
                      label='Other compositions'.format(classification))

            # Add decoration
            plt.legend(loc='upper right', scatterpoints=1)
            fig_title = '{} {}'.format(tephra, classification)
            plt.title(fig_title)
            plt.savefig('{}.png'.format(fig_title),
                        bbox_inches='tight', dpi=100)
            plt.close()


def classify_composition(sio2):
    """
    Simple classification based on wt% SiO2.
    """
    if sio2 > 69:
        return 'Rhyolite'
    elif sio2 > 63:
        return 'Dacite'
    elif sio2 > 57:
        return 'Andesite'
    elif sio2 > 52:
        return 'Basaltic andesite'
    else:
        return 'Basalt'


def get_coordinates(df, tephra, classification):
    """
    Prepare lists of latitude and longitude of places where tephra
    is present or absent.
    """
    # Locations where composition is found
    found = ((df['tephra_name'] == tephra) &
             (df['classification'] == classification))
    lon_found = df.loc[found, 'longitude'].tolist()
    lat_found = df.loc[found, 'latitude'].tolist()

    # Get locations where composition is absent
    absent = ((df['tephra_name'] == tephra) &
              (df['classification'] != classification))
    lon_absent = df.loc[absent, 'longitude'].tolist()
    lat_absent = df.loc[absent, 'latitude'].tolist()

    return lon_found, lat_found, lon_absent, lat_absent


def prepare_basemap():
    """
    Prepare matplotlib basemap.
    """
    # setup lambert conformal basemap.
    # lat_1 is first standard parallel.
    # lat_2 is second standard parallel (defaults to lat_1).
    # lon_0,lat_0 is central point.
    # rsphere=(6378137.00,6356752.3142) specifies WGS84 ellipsoid
    # area_thresh=1000 means don't plot coastline features less
    # than 300 km^2 in area.
    m = Basemap(width=2.8e6, height=3.2e6, rsphere=(6378137.00, 6356752.3142),
                resolution='l', projection='lcc', area_thresh=300,
                lat_1=45, lat_2=65, lat_0=61, lon_0=0)
    m.drawcoastlines(linewidth=0.5, color='0.4')
    m.fillcontinents(color=[0.9, 0.9, 0.9], zorder=0)
    m.drawparallels(np.arange(-30, 81, 10.), labels=[1, 1, 0, 0])
    m.drawmeridians(np.arange(-50, 51, 10.), labels=[0, 0, 0, 1])
    
    return m


if __name__ == '__main__':
    main()
