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
    df = df.append(pd.read_csv('hekla3and4_without_geochemistry.csv'),
                   ignore_index=True)

    # Add unique IDs for sites with no geochemistry
    df.loc[df['site'].isnull(), 'site'] = df.loc[
        df['site'].isnull()].index.tolist()

    # Classify composition
    df['composition'] = [classify_composition(x) for x in df['SiO2']]

    # Write summary csv file
    grouped = df.groupby(
        ['tephra_name', 'site', 'composition'])['longitude', 'latitude']
    grouped.mean().to_csv(
        'summary_sites_and_compositions.csv', header=True, index=True,
        float_format='%.2f')

    for tephra in ['Hekla 4 Tephra', 'Hekla 3 Tephra']:
        for composition in ['Rhyolite', 'Dacite', 'Andesite',
                            'Basaltic andesite']:

            # Get coordinates
            coords = get_coordinates(df, tephra, composition)
            (lon_found, lat_found, lon_absent, lat_absent,
             lon_no_geochem, lat_no_geochem) = coords

            # Create figure
            print("Plotting {} {}".format(tephra, composition))
            plt.figure(figsize=(7, 7))
            m = prepare_basemap()

            # Plot sample locations
            m.scatter(lon_found, lat_found, latlon=True,
                      color='red', s=60, zorder=4,
                      label='{}'.format(composition))
            m.scatter(lon_absent, lat_absent, latlon=True,
                      color='orange', s=35, zorder=3,
                      label='Other compositions'.format(composition))
            m.scatter(lon_no_geochem, lat_no_geochem, latlon=True,
                      color='0.2', s=15, zorder=2,
                      label='No geochemistry data'.format(composition))

            # Add decoration
            plt.legend(loc='upper right', scatterpoints=1)
            fig_title = '{} {}'.format(tephra, composition)
            plt.title(fig_title)
            plt.savefig('{}.png'.format(fig_title),
                        bbox_inches='tight', dpi=100)
            plt.close()


def classify_composition(sio2):
    """
    Simple composition based on wt% SiO2.
    """
    if np.isnan(sio2):
        return 'No geochemistry data'

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


def get_coordinates(df, tephra, composition):
    """
    Prepare lists of latitude and longitude of places where tephra
    is present or absent.
    """
    my_tephra = df['tephra_name'] == tephra
    my_composition = df['composition'] == composition
    geochem_missing = df['composition'] == 'No geochemistry data'

    # Locations where composition is found
    found = np.logical_and(my_tephra, my_composition)
    lon_found = df.loc[found, 'longitude'].tolist()
    lat_found = df.loc[found, 'latitude'].tolist()

    # Locations where other composition is found
    absent = np.logical_and(
        my_tephra, np.logical_not(
            np.logical_or(my_composition, geochem_missing)))
    lon_absent = df.loc[absent, 'longitude'].tolist()
    lat_absent = df.loc[absent, 'latitude'].tolist()

    # Get locations with no geochemistry data
    no_geochem = np.logical_and(my_tephra, geochem_missing)
    lon_no_geochem = df.loc[no_geochem, 'longitude'].tolist()
    lat_no_geochem = df.loc[no_geochem, 'latitude'].tolist()

    coords = (lon_found, lat_found, lon_absent, lat_absent,
              lon_no_geochem, lat_no_geochem)

    return coords


def prepare_basemap():
    """
    Prepare matplotlib basemap.
    """
    # setup lambert conformal basemap.
    # lat_1 is first standard parallel.
    # lat_2 is second standard parallel (defaults to lat_1).
    # lon_0,lat_0 is central point.
    # rsphere=(6378137.00,6356752.3142) specifies WGS84 ellipsoid
    # area_thresh=300 means don't plot coastline features less
    # than 300 km^2 in area.
    m = Basemap(width=2.8e6, height=3.2e6, rsphere=(6378137.00, 6356752.3142),
                resolution='l', projection='lcc', area_thresh=300,
                lat_1=50, lat_2=66, lat_0=61.5, lon_0=0)
    m.drawcoastlines(linewidth=0.5, color='0.4')
    m.fillcontinents(color=[0.9, 0.9, 0.9], zorder=0)
    m.drawparallels(np.arange(-30, 81, 10.), labels=[1, 1, 0, 0])
    m.drawmeridians(np.arange(-50, 51, 10.), labels=[0, 0, 0, 1])

    return m


if __name__ == '__main__':
    main()
