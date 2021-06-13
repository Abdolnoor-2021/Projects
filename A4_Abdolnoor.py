# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 12:57:52 2021

@author: Abdolnoor
"""
import matplotlib.pyplot as plt
import numpy as np
import os    


background = {'size':np.array([1280, 1024]),'color':0.5} 
target = {'shape':'^', 'size':150, 'color':'r', 'bg_color':'r', 'number_of':1}
distractors = {'shape':'o', 'size':150, 'color':'g', 'number_of':12}

def create_stimulus(background, target, distractor, stimulus_path):
    
     ''' 
     creating a stimulus with a target and distractors 
          in a 1280*1024 arandomly spread in a 10*8 grid.
          
     Args: background(size: array, color: number between 0 and 1).
          target {shape, size, color}
          distractor {shape, size, color}
          stimulus_path (new folder)
         
     Returns : saves a figure
      
     '''
           
     grid_size = [10, 8]
     grid_size_pixels_x = background['size'][1] / grid_size[1]
     grid_size_pixels_y = background['size'][0] / grid_size[0]
     x_c = np.arange(grid_size_pixels_x / 1.0, background['size'][0], grid_size_pixels_x)
     y_c = np.arange(grid_size_pixels_y / 1.0, background['size'][1], grid_size_pixels_y)
      
     x_all, y_all = np.meshgrid(x_c, y_c)
     xy_all = np.vstack((x_all.flatten(), y_all.flatten())).T
    
      
     fig, ax = plt.subplots()
     fig.set_size_inches(background['size'][0]/100.0, background['size'][1]/100.0)
     ax.set_facecolor((background['color'], background['color'], background['color']))
     ax.set_xlim(0, background['size'][0]) # hiding lables
     ax.set_ylim(0, background['size'][1]) # hiding lables
     fig.subplots_adjust(left=0.0, right=1, top=1, bottom=0) 
    
      
     
     np.random.shuffle(xy_all)
     plt.scatter(xy_all[:distractors['number_of'], 0], 
                  xy_all[:distractors['number_of'], 1], 
                  s=distractors['size'], c=distractors['color'], 
                  marker=distractors['shape']) 

     np.random.shuffle(xy_all)
     stimuli = plt.scatter(xy_all[:target['number_of'], 0], xy_all[:target['number_of'], 1], 
                  s=target['size'], c=target['color'], marker=target['shape'])
    
      
     plt.axis([0, background['size'][0], 0, background['size'][1]])
     
     plt.show()
 
     fig.savefig(stimulus_path + 'stimulus.png', dpi = 100)
     return
    
stimulus_path = os.getcwd() + os.sep + 'Stimuli' + os.sep
if not os.path.exists(stimulus_path):
    os.makedirs(stimulus_path)
    
create_stimulus(background, target, distractors, stimulus_path)
    