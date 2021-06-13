# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:33:16 2021

@author: Abdolnoor 
"""
#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image


# Question 1

eye_velocity = np.array(pd.read_csv("eye_velocity.csv")).flatten()

# Plotting figure 1

x = np.arange(1000)
y1 = eye_velocity [0:1000]
y2 = [np.mean(y1)] * 1000

plt.plot (x, y1, c = 'r', lw = 2)
plt.plot (x, y2, linestyle = 'dashed' , c = 'g', lw = 1)

plt.legend()
plt.xlabel('Time (ms)' , fontsize = 14)
plt.ylabel('Velocity ${}^{\circ}/s$' , fontsize = 14)


x_text, y_text = 720, 200
plt.text(x_text, y_text, 'average velocity')
plt.annotate('average velocity', xy=(600, 46), xytext=(720,200), 
             arrowprops=dict(facecolor='black', arrowstyle="->"))
plt.show()

# Question 2
# histogram of eye_velocity
eye_velocity_samples = 85765
plt.figure()
plt.hist(eye_velocity, bins = 100, edgecolor = 'black', rwidth = 0.95, log = True) 
plt.xlabel('time (ms)')
plt.ylabel('number of samples')
plt.title('A histogram of the eye_velocity')
plt.show()

# Question openning and plotting images
plt.show()

#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


im1 = Image.open('1.png')
im2 = Image.open('2.png')
im3 = Image.open('3.png')
im4 = Image.open('4.png')

im1 = np.rot90(im1.resize((250, 255), Image.ANTIALIAS),3,)
im2 = im2.resize((255, 250), Image.ANTIALIAS)
im3 = im3.resize((255, 250), Image.ANTIALIAS)
im4 = im4.resize((255, 250), Image.ANTIALIAS)

#  antialias: minimizing the distortion after resizing, to make it smoother.

top = np.concatenate((im1, im2), axis = 1)  
plt.imshow(top)

bottom = np.concatenate((im3, im4), axis = 1)  
plt.imshow(bottom)

combined = np.concatenate((top, bottom), axis = 0)  
plt.imshow(combined)
plt.savefig('baboon.pdf')



