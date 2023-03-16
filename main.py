# Import libraries using import keyword
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import pandas as pd

excelFile = pd.read_excel(r'C:\Users\smosavarpour\Documents\Coding\Python\ProfileAssignment\Desc+ProfName-CODE.xlsx')
 
# Setting Plot and Axis variables as subplots()
# function returns tuple(fig, ax)
Plot, Axis = plt.subplots()
 
# Adjust the bottom size according to the
# requirement of the user
plt.subplots_adjust(bottom=0.25, left=0.35) #add left

# plot the x and y using plot function
l = plt.scatter(x=excelFile['ProfileName'], y=excelFile['Description'])
 
# Choose the Slider color
slider_color = 'White'
 

#this is a test to see how git works Rahhahahhahh
branchTest = 0
print('This is from the test branch', branchTest)




 
# Set the axis and slider position in the plot
desc_position = Plot.add_axes([0.1,0.25,0.0225,0.5])
slider_position_desc = Slider(
    ax = desc_position,
    label = 'Description',
    valmin = 0,
    valmax= 350,
    valinit = 0,
    orientation='vertical'
)

prof_position = Plot.add_axes([0.25,0.1,0.65,.05])
slider_position_prof = Slider(
    ax = prof_position,
    label = 'Profile Name',
    valmin = 0,
    valmax= 15,
    valinit = 0,
    orientation='horizontal'
) 
 

#!!!add feature that allows user to filter the profiles & descriptions shown.


# update() function to change the graph when the
# slider is in use
def update(val):
    descPos = slider_position_desc.val
    profPos = slider_position_prof.val
    Axis.axis([profPos-1, profPos + 30,descPos-1, descPos + 25])
    Plot.canvas.draw_idle()
 
# update function called using on_changed() function
slider_position_desc.on_changed(update)
slider_position_prof.on_changed(update)
Axis.tick_params(axis='y', pad = 1)
Axis.tick_params(axis='x', labelrotation = 45)

 
# Display the plot
plt.show()