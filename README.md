# Hekla 3 and 4 distal geochemistry

>The [hekla3and4_distal_geochemistry](http://github.com/volcan01010/hekla3and4_distal_geochemistry.git) repository is for sharing data on the composition of glass shards from the Hekla 3 and Hekla 4 eruptions found outside Iceland.  Please contribute any that you may have.

I have been reconstructing the Hekla 3 and Hekla 4 eruptions based on their deposits in Iceland.  They are complicated, with multiple phases with different compositions, plume heights and dispersal directions.  Now I would like to relate these phases to their cryptotephra deposits outside Iceland.  This can be done based on their geochemistry.

Below are plots of the geochemical data that I have assembled so far (mainly from [Tephrabase](http://www.tephrabase.org)).  For Hekla 4, they show interesting features such as the narrow distribution of dacite and andesite composition material.  I can relate these to the deposits in Iceland.  For Hekla 3, there is unfortunately a real lack of data.


## Maps of distribution of Hekla 4 and Hekla 3 by geochemistry

The following maps show the results so far.

![Hekla 4 Rhyolite](Hekla 4 Tephra Rhyolite.png?raw=true)

![Hekla 4 Dacite](Hekla 4 Tephra Dacite.png?raw=true)

![Hekla 4 Andesite](Hekla 4 Tephra Andesite.png?raw=true)

![Hekla 3 Rhyolite](Hekla 3 Tephra Rhyolite.png?raw=true)

![Hekla 3 Dacite](Hekla 3 Tephra Dacite.png?raw=true)

![Hekla 3 Andesite](Hekla 3 Tephra Andesite.png?raw=true)


## A request for data

As these eruptions form such widespread tephrochronogical markers, lots more geochemical data must exist.  Much of it may only have been used to confirm that a layer was indeed H3 or H4 and nothing more.  It might be published as supplementary materials to papers, or just stored on hard drives.

I would really like to see these data.

The current dataset is stored in the spreadsheet [hekla3and4_distal_geochemistry.csv](hekla3and4_distal_geochemistry.csv).  It has columns for _longitude, latitude, site name, major oxide analyses (SiO2, TiO2 etc), total and reference_.  If you email a csv file in the same format to johnalexanderstevenson@gmail.com with your data, I will add it to the spreadsheet here and update the maps.  Of course, I will cite the reference provided in my paper on the eruption phases.

In particular, tephra glass analyses from Greenland, Faroes, Jan Mayen and the Baltic regions would be extremely valuable.


## Plotting the figures

This repository also contains the code for plotting the maps.  If you have
Python (including the Matplotlib, Pandas and Basemap packages) and Git
installed on your machine, you can recreate the plots as follows:

```
git clone http://github.com/volcan01010/hekla3and4_distal_geochemistry.git
cd hekla3and4_distal_geochemistry
python plot_hekla3and4_distal_geochemistry.py
```

