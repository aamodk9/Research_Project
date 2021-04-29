

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 09:20:30 2021

@author: AAMOD
"""
'''Required imports'''
from PIL import Image
import glob
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import imageio
from images2gif import writeGif
from PIL import Image
import itertools

''' Adding 3 csv's to the list called "file_names'''
file_names = []
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A01Sample.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A02-tracks.csv')
file_names.append('D:/Study/Sem-3/Research project/files/csv-2/A03-tracks.csv')

'''Loading 3 csv files using pandas'''
A01Sample= pd.read_csv(file_names[0],error_bad_lines=False)
A02tracks= pd.read_csv(file_names[1],error_bad_lines=False)
A03tracks= pd.read_csv(file_names[2],error_bad_lines=False)


'''Appending the dataframes into list'''
files=[]
files.append(A01Sample)
files.append(A02tracks)
files.append(A03tracks)

'''Adding new column ,"Frame_No" to the list of dataframes by dividing "Slice n°" column by 3'''
      
for i in range(len(files)):
    new_column= files[i]['Slice n°'].div(3)
    if 'Frame_No' not in files[i]:
        files[i]['Frame_no'] = new_column.astype(int)    
    files[i].to_csv(file_names[i])

''' Loading one image to plot all the points while creating GIF'''
image_load= glob.glob(r'D:\Study\Sem-3\Research project/Images/A01_001.tif', recursive=True)

'''Plotting the images by seperating channels (axs.ravel flattens the 2d array)'''

for photo, z in zip(image_load, range(10)):
    figure, axs = plt.subplots(ncols=3, nrows=6)  #plotting the subplots
    axs[0,0].set_title('Nuclei Marker')
    axs[0,1].set_title('Nuclei Marker')
    axs[0,2].set_title('Microscope image')
    for i, subplot in zip(range(axs.shape[0]*axs.shape[1]), axs.ravel()):
        image_array=np.array(Image.open(photo))  #opening one photo and loading as array
        new_image_array = np.zeros(image_array.shape, dtype='uint8')
        new_image_array[:,:,i%3] = image_array[:,:,i%3]
        subplot.imshow(new_image_array)
        subplot.set_axis_off()        
        for index, row in A01Sample.iterrows(): #iterating over rows of A01Sample
            if (row['Track n°']==A01Sample['Track n°'].unique()[int(i/3)]):
             subplot.scatter(row['X'], row['Y'], c='w', s=1,alpha=0.8)
plt.savefig('D:/Study/Sem-3/Research project/sample.png', dpi=1200)   #saving the gif to the directory
plt.show()      




'''Animation going forward in time, Looping over chanel and frame number (GIF)'''
figure, axs = plt.subplots(ncols=1, nrows=1)    
axs.set_title('Nuclei Marker')
image_list = [] 
max_frame_no = np.amax(A01Sample['Frame_no'].to_numpy()) 
iter_till_frame_no = 90 # 600 Slides = 200 Frames with 3 channels
iter_till_frame_no = iter_till_frame_no if iter_till_frame_no <= max_frame_no else max_frame_no
for frame_no in range(iter_till_frame_no): #iterating over frame_no
   image = Image.open(f'D:/Study/Sem-3/Research project/Images/A01_{(frame_no+1):03}.tif') #image loading for pixel extraction
   pixel_load = image.load() #pixel extraction
   sub_df = A01Sample[A01Sample['Frame_no']==frame_no]
   figure, axs = plt.subplots(ncols=1, nrows=1) #plotting the subplots
   axs.set_title('Nuclei Marker')
   axs.imshow(new_image_array)
   axs.set_axis_off() 
   for index, row in sub_df.iterrows(): #iterating over sub_df rows
       pixel= pixel_load[row['X'], row['Y']]
       color = ['green' if pixel[0] < pixel[1] else 'red'] #Assigning pixel a color by checking the condition
       sbplt = axs.scatter(row['X'], row['Y'], s=2, c=color ,alpha=0.9)
   figure_name = ('D:/Study/Sem-3/Research project/samp') + str(frame_no)+'.jpeg'
   sbplt.figure.savefig(figure_name, dpi=200)
   image_list.append(imageio.imread(figure_name))   
imageio.mimsave('D:\Study\Research_Project\Animation_02.gif',image_list) #saving the gif to the directory
plt.show()



