# -*- coding: utf-8 -*-
"""

@author: AAMOD
"""

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

#Using the original naming conventions
A01Sample= pd.read_csv(file_names[0],error_bad_lines=False)
A02tracks= pd.read_csv(file_names[1],error_bad_lines=False)
A03tracks= pd.read_csv(file_names[2],error_bad_lines=False)
Book_A01= pd.read_csv(file_names[3],error_bad_lines=False)


#Appending the dataframes into list
files=[]
files.append(A01Sample)
files.append(A02tracks)
files.append(A03tracks)
files.append(Book_A01)
#Adding new column naming, "Frame_No"
      
for i in range(len(files)):
    temp= files[i]['Slice n°'].div(3)
    if 'Frame_No' not in files[i]:
        files[i]['Frame_no'] = temp.astype(int)    
    files[i].to_csv(file_names[i])

#Plotting the images with seperating channels
#image1 = [cv2.imread(file) for file in glob.glob(r'D:\\Study\\Sem-3\\Research project\\Images\\**\*.tif', recursive=True)]

image = glob.glob(r'D:\Study\Sem-3\Research project\Images1\A01_001.tif', recursive=True)



#Plotting the images with seperating channels

#axs.ravel flattens the 2d array
#axs.shape[0]*axs.shape[1] gives no. of rows and columns
for photo, z in zip(image, range(10)):
    figure, axs = plt.subplots(ncols=3, nrows=6)    
    axs[0,0].set_title('Nuclei Marker')
    axs[0,1].set_title('Nuclei Marker')
    axs[0,2].set_title('Microscope image')
    for i, subplot in zip(range(axs.shape[0]*axs.shape[1]), axs.ravel()):
        img1=np.array(Image.open(photo))
        temp = np.zeros(img1.shape, dtype='uint8')
        temp[:,:,i%3] = img1[:,:,i%3]
        subplot.imshow(temp)
        subplot.set_axis_off()        
        for index, row in A02tracks.iterrows():
            #print(row['X'], row['Y'])
            if (row['Track n°']==A02tracks['Track n°'].unique()[int(i/3)]):
             subplot.scatter(row['X'], row['Y'], c='w', s=1,alpha=0.8)
plt.savefig('D:/Study/Sem-3/Research project/sample6.png', dpi=1200)         
plt.show()

'''Using Slice No to figure out what channel the dataset corresponds to by checking if Slice No % 3 is 0, 1 or 2'''
figure, axs = plt.subplots(ncols=3, nrows=1)    
axs[0].set_title('Nuclei Marker')
axs[1].set_title('Nuclei Marker')
axs[2].set_title('Microscope image') 
#for i, subplot in zip(range(3), axs):
img1=np.array(Image.open(image[0]))
temp = np.zeros(img1.shape, dtype='uint8')
axs[0].imshow(temp)
axs[0].set_axis_off()
axs[1].imshow(temp)
axs[1].set_axis_off()
axs[2].imshow(temp)
axs[2].set_axis_off()
for index, row in A02tracks.iterrows():
            if (row['Slice n°']%3 == 1):
             axs[0].scatter(row['X'], row['Y'],s=0.1, c='r',alpha=0.9)
            if (row['Slice n°']%3 == 2):
             axs[1].scatter(row['X'], row['Y'],s=0.1, c='g',alpha=0.9) 
            if (row['Slice n°']%3 == 0):
              axs[2].scatter(row['X'], row['Y'],s=0.1, c='b',alpha=0.8)
plt.savefig('D:/Study/Sem-3/Research project/sample7.png', dpi=1200)  
plt.show()


'''Animation going forward in time, Looping over frame number (GIF)'''
figure, axs = plt.subplots(ncols=1, nrows=1)    
axs.set_title('Nuclei Marker')
img1=np.array(Image.open(image[0]))
temp = np.zeros(img1.shape, dtype='uint8')
axs.imshow(temp)
axs.set_axis_off() 
image_list = [] 
for index, row in A02tracks.iterrows():
 if (row['Frame_no'] == 1):
  color = ['green' if row['X'] < row['Y'] else 'red']
  sbplt = axs.scatter(row['X'], row['Y'], s=3, c=color ,alpha=1) 
  figName = 'D:/Study/Sem-3/Research project/sample' + str(row['X'])+'.jpeg'
  sbplt.figure.savefig(figName, dpi=600)
  image_list.append(imageio.imread(figName))     
imageio.mimsave('D:\Study\Research_Project\Images1.gif',image_list)
plt.show()


'''Animation going forward in time, Looping over chanel and frame number (GIF) (update)'''
im = Image.open(r'D:\Study\Sem-3\Research project\Images1\A01_001.tif')
pix = im.load()
figure, axs = plt.subplots(ncols=1, nrows=1)    
axs.set_title('Nuclei Marker')
img1=np.array(Image.open(image[0]))
temp = np.zeros(img1.shape, dtype='uint8')
axs.imshow(temp)
axs.set_axis_off() 
frame_no = 1
Max_frame_no = 90
for index, row in A02tracks.iterrows():
 if (row['Frame_no'] == frame_no and row['Frame_no']<= Max_frame_no ):
  pixel= pix[row['X'], row['Y']]
  color = ['green' if pixel[0] < pixel[1] else 'red']
  sbplt = axs.scatter(row['X'], row['Y'], s=2, c=color ,alpha=0.9) 
  figName = 'D:/Study/Sem-3/Research project/samp' + str(row['X'])+'.jpeg'
  sbplt.figure.savefig(figName, dpi=200)
  image_list.append(imageio.imread(figName))     
imageio.mimsave('D:\Study\Research_Project\Images4.gif',image_list)
plt.show()






 



