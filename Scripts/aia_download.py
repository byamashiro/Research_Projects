from sunpy.net import Fido, attrs as a

import matplotlib.pyplot as plt
from matplotlib import patches
import astropy.units as u
from astropy.coordinates import SkyCoord

import sunpy.map
import sunpy.data.sample

hd_path = '/Volumes/Coursework/sunpy_files'

result = Fido.search(a.Time('2012/3/7 00:00:00', '2012/3/7 02:00:00'),a.Wavelength(193*u.angstrom), a.Instrument('aia')) # 191-195 Angstrom
print(result)

# downloaded_files = Fido.fetch(result, path=f'{hd_path}')
