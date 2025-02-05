import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plot_data(data, coordinates, category_index=0, band_index=0):
    """Plot 2D data on a map using Cartopy."""
    data_2d = data[:, :, category_index, band_index]
    
    _, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    
    lon = np.linspace(coordinates["west"], coordinates["east"], data_2d.shape[1])
    lat = np.linspace(coordinates["south"], coordinates["north"], data_2d.shape[0])
    lat = lat[::-1] # Reverse the latitude array
    lon, lat = np.meshgrid(lon, lat)
    
    c = ax.pcolormesh(lon, lat, data_2d, transform=ccrs.PlateCarree(), cmap='viridis')
    plt.colorbar(c, ax=ax, orientation='vertical', label='RCCM Count')
    ax.set_title(f'Category {category_index} - Band {band_index}')
    plt.tight_layout()
    plt.show()