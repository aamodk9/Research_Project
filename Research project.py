# -*- coding: utf-8 -*-
"""

@author: AAMOD
"""

import os
from PIL import Image
import glob
from matplotlib import pyplot as plt
import PIL
import pandas as pd
%matplotlib inline

images=glob.glob(r'D:\\Study\\Sem-3\\Research project\\Images\\**\*.tif', recursive=True)

#Main 3 Csv's 
csv1= pd.read_csv('D:\Study\Sem-3\Research project\Research project\CSV files\A01Sample-1.csv')
csv2= pd.read_csv('D:\Study\Sem-3\Research project\Research project\CSV files\A02-tracks.csv',sep=";")
csv3= pd.read_csv(r'D:\Study\Sem-3\Research project\Research project\CSV files\A03-tracks.csv', sep=";")


#Plotting of images
rows=5
for i, x in enumerate(images):
    img = PIL.Image.open(x)
    plt.subplot(rows,3,i+1)
    plt.axis('off')
    plt.imshow(img)
    

#Conversion for csv1
csv1['Slice n°']=csv1['Slice n°'].div(3)
csv1['Slice n°'] = csv1['Slice n°'].astype(int)
display(csv1.dtypes) 
csv1.head()

#Conversion for csv2
csv2['Slice n°']=csv2['Slice n°'].div(3)
csv2['Slice n°'] = csv2['Slice n°'].astype(int)
display(csv2.dtypes) 
csv2.head()

#conversion for csv3
csv3['Slice n°']=csv3['Slice n°'].div(3)
csv3['Slice n°'] = csv3['Slice n°'].astype(int)
display(csv3.dtypes) 
csv3.head()
