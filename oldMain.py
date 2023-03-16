import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from operator import *

excelFile = pd.read_excel('Desc+ProfName-CODE.xlsx')
desc = pd.Series(excelFile['Description'])
profName = pd.Series(excelFile['ProfileName'])

desc.drop_duplicates(keep='first',inplace=True)
profName.drop_duplicates(keep='first', inplace=True)

with pd.ExcelWriter(path='test1.xlsx') as writer:
    desc.to_excel(writer, sheet_name='Pandas Desc')

descList = desc.values.tolist()
profName = profName.values.tolist()



descLen = len(descList)
profLen = len(profName)
descNum = []

profDescDict = {}

print(descList)

#this worked the way i wanted it to
for x in profName:
    profDescDict[x] = []

count = 0
for x in excelFile['ProfileName']:
    profDescDict[x].append(excelFile.loc[count, 'Description'])
    count += 1


delete = []
print()

print('Length BEFORE: \n',len(excelFile))

#Getting rid of descriptions that appear for every profile
for x in descList:
    test = 0
    check = 0
    for y in profName:
        check += 1
        if countOf(profDescDict[y],x) >= 1:
            test += 1
        
    if test == 39:
        delete.append(x)
        

excelFile.replace(delete, None)
print('Length AFTER: \n',len(excelFile))


#BREAK POINT: check if the dictionary is right 
fig, ax = plt.subplot()
data = plt.scatter(x=excelFile['ProfileName'], y=excelFile['Description'],)
plt.subplots_adjust(bottom=.25)
axDesc = plt.add_axes([0.1,0.25,0.0225,.063])
descSlider = Slider(
    ax = axDesc,
    Label = 'Description',
    valmin = 0,
    valmax= 500,
    valinit = 0,
    orientation='Vertical'
)

slider_position = Slider(axDesc,'pos',0.1,90.0)

def update(val):
    pos = slider_position.val
    ax.axis([pos, pos+10, -1, 1])
    fig.canvas.draw_idle()

slider_position.on_changed(update)

#plt.figure(figsize = (19,35), dpi = 50)
#plt.scatter(excelFile['ProfileName'], excelFile['Description'])
plt.show()