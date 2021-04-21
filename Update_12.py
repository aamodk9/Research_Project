

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:20:30 2021

@author: AAMOD
"""
'''Imports'''
from PIL import Image
import glob
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import imageio
from images2gif import writeGif
from PIL import Image
import itertools


file_names = []
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A01Sample.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A02-tracks.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A03-tracks.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/Book_A01.csv')

'''Using the original naming conventions'''
A01Sample= pd.read_csv(file_names[0],error_bad_lines=False)
A02tracks= pd.read_csv(file_names[1],error_bad_lines=False)
A03tracks= pd.read_csv(file_names[2],error_bad_lines=False)
Book_A01= pd.read_csv(file_names[3],error_bad_lines=False)


'''Appending the dataframes into list'''
files=[]
files.append(A01Sample)
files.append(A02tracks)
files.append(A03tracks)
files.append(Book_A01)

'''Adding new column naming, "Frame_No'''
      
for i in range(len(files)):
    temp= files[i]['Slice n°'].div(3)
    if 'Frame_No' not in files[i]:
        files[i]['Frame_no'] = temp.astype(int)    
    files[i].to_csv(file_names[i])

''' Importing one image to plot all the points while creating GIF'''
image = glob.glob(r'D:\Study\Sem-3\Research project/Images/A01_001.tif', recursive=True)




'''Animation going forward in time, Looping over chanel and frame number (GIF) (update)'''
figure, axs = plt.subplots(ncols=1, nrows=1)    
axs.set_title('Nuclei Marker')
img1=np.array(Image.open(image[0]))
temp = np.zeros(img1.shape, dtype='uint8')
image_list = [] 
max_frame_no = np.amax(A01Sample['Frame_no'].to_numpy())
iter_till_frame_no = 90 # 600 Slides = 200 Frames with 3 channels
iter_till_frame_no = iter_till_frame_no if iter_till_frame_no <= max_frame_no else max_frame_no
for frame_no in range(iter_till_frame_no):
   im = Image.open(f'D:/Study/Sem-3/Research project/Images/A01_{(frame_no+1):03}.tif')
   pix = im.load()
   sub_df = A01Sample[A01Sample['Frame_no']==frame_no]
   figure, axs = plt.subplots(ncols=1, nrows=1)    
   axs.set_title('Nuclei Marker')
   axs.imshow(temp)
   axs.set_axis_off() 
   for index, row in sub_df.iterrows():
       pixel= pix[row['X'], row['Y']]
       color = ['green' if pixel[0] < pixel[1] else 'red']
       sbplt = axs.scatter(row['X'], row['Y'], s=2, c=color ,alpha=0.9)
   figName = 'D:/Study/Sem-3/Research project/samp' + str(frame_no)+'.jpeg'
   sbplt.figure.savefig(figName, dpi=200)
   image_list.append(imageio.imread(figName))   
imageio.mimsave('D:\Study\Research_Project\Animation_01.gif',image_list)
plt.show()



