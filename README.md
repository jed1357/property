# Property 233 GIS

#### Setting Up Note
- After setting up all necessary components, install postgis using the following commands <br/>
```
    sudo apt install postgresql-10-postgis-2.4
    sudo apt install postgresql-10-postgis-scripts
    
```
- After that, run ```CREATE EXTENSION postgis```.

Installation guide for postgis is https://postgis.net/install/

- Ensure GDAL is installed (https://gist.github.com/mojodna/2f596ca2fca48f08438e)[help here]

- Install Conda to deal with GDAL issues on EC 2 Use this link to install Conda: https://www.anaconda.com/rpm-and-debian-repositories-for-miniconda/
