# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 08:49:13 2021

@author: Abdolnoor
"""

#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

eye_velocity = np.array(pd.read_csv("eye_velocity.csv")).flatten()

plt.figure()
plt.plot(eye_velocity) # Plots the data
plt.xlabel('Samples')
plt.ylabel('Velocity (deg/s)')
plt.show()

#percent/number of NaN_values in dataset
a1 = np.sum(np.isnan(eye_velocity))
print("the number of NaN_values: ", a1)
percent_NaN_values = a1/len(eye_velocity)*100
print("the percentage of NaN_values in dataset: ", percent_NaN_values)

# Dataset of short eye_velocity
eye_velocity_short = eye_velocity [0:85694]
plt.plot(eye_velocity_short) 
plt.xlabel('Time (ms)')
plt.ylabel('Velocity (deg/s)')
plt.show()



#%% determine threshold

T = 30

#Function
def event_detector(eye_velocity,T):
    '''
    Input:
        eye_velocity (n * 1 array): eye velocities sampled at 1000 Hz
        T (int): threshold; values below are fixations
    Returns: 
        fixation_onset_idx (array): indexes where fixations start
        fixation_durations (array): durations of fixations
    '''

#  separating fixations from saccades and converting true/false to 1/0
    fixation_samples = (eye_velocity < T) * 1  
    fixation_samples_0 = np.hstack((0, fixation_samples, 0))  
    
    fix_onsets = np.where(np.diff(fixation_samples_0) == 1)
    fix_ofsets = np.where(np.diff(fixation_samples_0) == -1)
    fix_durations = np.subtract(fix_ofsets, fix_onsets)[0].astype('int64')  

    fix_durations0 = []                 
    for i in fix_durations:              
        if i > 20:
            fix_durations0.append(i)

    return fix_onsets, fix_durations0


# test the function by changing threshold below
fixation_onsets_and_durations = event_detector(eye_velocity, 30)
print(fixation_onsets_and_durations)                                                  

# number of fixations
fixation_amount = np.size(event_detector(eye_velocity, 30)[1])  
print('number of fixations:', fixation_amount)

#Sum of fixation durations
fixation_totallegth = np.sum(event_detector(eye_velocity, 30)[1])
print('total fixation duration:', fixation_totallegth)

#mean of fixation duration
fixation_mean = np.mean(event_detector(eye_velocity, 30)[1])
print('average fixation duration:', fixation_mean)

#percentage of fixation durations under 100 ms
fixations = (event_detector(eye_velocity, 30)[1])

n_fixations_under_100 = 0
for i in fixations:
    if i < 100:
        n_fixations_under_100 += 1
        
percentage_fixations_under_100 = n_fixations_under_100 * 100 / len(fixations)
print('percentage of fixations under 100:', percentage_fixations_under_100)
