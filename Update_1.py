# -*- coding: utf-8 -*-
"""

@author: AAMOD
"""

from PIL import Image
import glob
from matplotlib import pyplot as plt
import pandas as pd
import cv2
import numpy as np

file_names = []
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A01Sample.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A02-tracks.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A03-tracks.csv')

#Using the original naming conventions
A01Sample= pd.read_csv(file_names[0],error_bad_lines=False)
A02tracks= pd.read_csv(file_names[1],error_bad_lines=False)
A03tracks= pd.read_csv(file_names[2],error_bad_lines=False)

#Appending the dataframes into list
files=[]
files.append(A01Sample)
files.append(A02tracks)
files.append(A03tracks)

#Adding new column naming, "Frame_No"
      
for i in range(len(files)):
    temp= files[i]['Slice n°'].div(3)
    if 'Frame_No' not in files[i]:
        files[i]['Frame_no'] = temp.astype(int)    
    files[i].to_csv(file_names[i])

#Plotting the images with seperating channels
#image1 = [cv2.imread(file) for file in glob.glob(r'D:\\Study\\Sem-3\\Research project\\Images\\**\*.tif', recursive=True)]

image = glob.glob(r'D:\Study\Sem-3\Research project\Images\**\*.tif', recursive=True)

#Plotting the images with seperating channels
for photo in image:
    figure, axs = plt.subplots(ncols=3, nrows=1)
    for i, subplot in zip(range(3), axs):
        img1=np.array(Image.open(photo))
        temp = np.zeros(img1.shape, dtype='uint8')
        temp[:,:,i] = img1[:,:,i]
        subplot.imshow(temp)
        subplot.set_axis_off()
        axs[0].set_title('Nuclei Marker')
        axs[1].set_title('Nuclei Marker')
        axs[2].set_title('Microsocpe image')
plt.show()

#Scatterplot
ax = plt.axes(projection ="3d")
i=0
for img in img1:
 ax.scatter(img.flat[i], img1.flat[i+1], img1.flat[i+2], c='r', marker='o')
 i+= 1
ax.set_xlabel('Channel 1')
ax.set_ylabel('Channel 2')
ax.set_zlabel('Channel 3')



 
    
