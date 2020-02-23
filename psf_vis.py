#!/usr/bin/env python3

""" PSF visualisation

Usefull links:
https://www.researchgate.net/post/How_are_you_deconvolving_your_confocal_LSM_stacks_for_dendritic_spine_morphological_analyses
https://svi.nl/NyquistCalculator
http://bigwww.epfl.ch/algorithms/psfgenerator/

https://photutils.readthedocs.io/en/stable/psf_matching.html

http://kmdouglass.github.io/posts/implementing-a-fast-gibson-lanni-psf-solver-in-python/


"""

import sys
import logging

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

from skimage import data
from skimage import exposure
from skimage import filters
from skimage.filters import scharr
from skimage.external import tifffile
from skimage import restoration

sys.path.append('modules')
import gila

psf_size =[128, 128, 128]
xy_slice = 40
slice_coord = int(psf_size[0] / 2)

psf = gila.demo(psf_size)
psf_xz = psf[:,slice_coord,:]
psf_xy = psf[xy_slice,:,:]



ax0 = plt.subplot(121)
slice_0 = ax0.imshow(psf_xy, cmap = 'inferno') 
divider_0 = make_axes_locatable(ax0)
cax = divider_0.append_axes("right", size="3%", pad=0.1)
plt.colorbar(slice_0, cax=cax)
ax0.set_title('X-Y')


ax1 = plt.subplot(122)
slice_1 = ax1.imshow(psf_xz, cmap = 'inferno')
ax1.plot([0, psf_size[0]-1], [xy_slice, xy_slice])

divider_1 = make_axes_locatable(ax1)
cax = divider_1.append_axes("right", size="3%", pad=0.1)
plt.colorbar(slice_1, cax=cax)
ax1.set_title('X-Z, middle')


plt.show()

