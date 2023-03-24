import xarray as xr 
import numpy as np                         
from matplotlib.dates import date2num, num2date                                         
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.rcParams["figure.figsize"] = (7,5)

def timesteps(input, Valuedpi):

    with xr.open_dataset(input) as file:
        
        minvar = file.analysed_sst.min()
        maxvar = file.analysed_sst.max()
        
        for t in range(file.time.shape[0]):    
            
            da = file.analysed_sst.isel(time=t)
            num = date2num(file.time[t])
            date = num2date(num)

            lat  = file.variables['lat'][:]
            lon  = file.variables['lon'][:]

            title = str(date)[0:10]
            plt.title(title, fontsize=10, weight='bold')

            plt.xlabel("Longitude", fontsize=10, labelpad=12)
            plt.ylabel("Latitude", fontsize=10, labelpad=12)

            m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
            urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
            resolution='f') 

            m.drawcoastlines()
            m.bluemarble()

            m.drawparallels(np.arange(-80., 81., 1.33), \
                            labels=[1,0,0,0], fontsize=6)
            
            m.drawmeridians(np.arange(-180., 181., 1.33), \
                            labels=[0,0,0,1], fontsize=6)

            x, y = m(*np.meshgrid(lon,lat))
            
            col = m.pcolormesh(x,y,da,shading='gouraud',cmap=plt.cm.jet, vmin=minvar, vmax=maxvar)
            cbar = plt.colorbar(col)
            cbar.ax.yaxis.set_ticks_position('right')

            for I in cbar.ax.yaxis.get_ticklabels():
                I.set_size(10)

            cbar.set_label("analysed_sst (Kelvin)", size = 10, weight='normal',labelpad=10)

            plt.savefig('PNG/{}.png'.format(t), dpi=Valuedpi)

            plt.close()

            