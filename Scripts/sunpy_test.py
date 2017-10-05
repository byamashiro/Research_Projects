import matplotlib.pyplot as plt
from matplotlib import patches
import astropy.units as u
from astropy.coordinates import SkyCoord

import sunpy.map
import sunpy.data.sample


# Define a region of interest
length = 250 * u.arcsec
x0 = 900 * u.arcsec
y0 = -400 * u.arcsec
# x0 = -100 * u.arcsec
# y0 = -400 * u.arcsec

# Create a SunPy Map, and a second submap over the region of interest.
smap = sunpy.map.Map(sunpy.data.sample.AIA_193_IMAGE)
bottom_left = SkyCoord(x0 - length, y0 - length,
                       frame=smap.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length,
                     frame=smap.coordinate_frame)
submap = smap.submap(bottom_left, top_right)


# Create a new matplotlib figure, larger than default.
fig = plt.figure(figsize=(10,5)) # 5,12

# Add a first Axis, using the WCS from the map.
ax1 = fig.add_subplot(1,2,1, projection=smap) # 2,1,1

# Plot the Map on the axes with default settings.
smap.plot()

# Draw a box on the image
smap.draw_rectangle(bottom_left, length * 2, length * 2)

# Create a second axis on the plot.
ax2 = fig.add_subplot(1,2,2, projection=submap) # 2,1,2

submap.plot()

# Add a overlay grid.
submap.draw_grid(grid_spacing=10*u.deg)

# Change the title.
# ax2.set_title('Zoomed View')

plt.savefig('map_test/test_sunpy.png', format='png', dpi=900)
# plt.show()