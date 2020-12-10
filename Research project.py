'''# -*- coding: utf-8 -*


@author: AAMOD
"""
'''


import os
from PIL import Image
from skimage import io
import glob
from matplotlib import pyplot as plt
import PIL
import pandas as pd
import matplotlib
import numpy as np



#Loading images
image=glob.glob(r'D:\Study\Sem-3\Research project\Images\**\*.tif', recursive=True)

#loading csv files (Added Frame_No column to each csv)

A01Sample= pd.read_csv("D:/Study/Sem-3/Research project/files/csv-2/A01Sample.csv")
A02tracks= pd.read_csv('D:/Study/Sem-3/Research project/files/csv-2/A02-tracks.csv')
A03tracks= pd.read_csv(r'D:/Study/Sem-3/Research project/files/csv-2/A03-tracks.csv')


#Plotting 3 sperate channels for each image
for photo in image:
    figure, plots = plt.subplots(ncols=3, nrows=1)
    for i, subplot in zip(range(3), plots):
        img1=np.array(Image.open(photo))
        temp = np.zeros(img1.shape, dtype='uint8')
        temp[:,:,i] = img1[:,:,i]
        subplot.imshow(temp)
        subplot.set_axis_off()
plt.show()

