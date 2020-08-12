#!/usr/bin/env python
# coding: utf-8

# 老呆狼杂记MyTiros
# https://www.youtube.com/channel/UCDhL5X5nzGG6xGRbTKMxd3Q/

# In[1]:


import glob
import os
import imageio
import sys
sys.setrecursionlimit(5000)


# In[2]:


gif_name = 'MyTiros.gif'
log_name = 'log.txt'

file_list = glob.glob('*') # Get all the pngs in the current directory
sorted_list = sorted(file_list)

duration = input('Please input a number as duration \n Press Enter to use the default value (0.1)\n')
if len(duration)==0:
    duration='0.1'  
try:
    duration = float(duration)
except ValueError:
    print("Please make sure your input is a number\n")
# duration = float(duration)

loop = input('Please input a number as loop \n Press Enter to loop forever\n')
if len(loop)==0:
    loop='0'
try:
    loop = float(loop)
except ValueError:
    print("Please make sure your input is a number\n")  
# loop = float(loop)

f = open(log_name,'w')

_=f.write('gif parameter:\n')
_=f.write('  Duration: '+str(duration)+'s\n')
if loop>0:
    _=f.write('  Loop: '+str(loop)+' times.\n\n')
else:
    _=f.write('  Loop: forever.\n\n')
_=f.write('File order:\n')
_=f.write('\n')


# In[3]:


images = []
for file in sorted_list:
    if not (file.endswith('.exe') | file.endswith('.txt') | file.endswith('.gif')):
            images.append(imageio.imread(file))
            _=f.write('  %s\n' % file)
imageio.mimwrite(gif_name,images,'GIF',duration=duration,loop=loop) # default 0.1, 0
    
f.close()

