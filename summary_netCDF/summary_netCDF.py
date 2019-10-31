#!/usr/bin/env python
# coding: utf-8

# In[10]:


from netCDF4 import Dataset
import datetime
import glob
import cftime


# In[40]:


def begin_log(name='summary_netCDF'):
    time_str = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    log_file = name+time_str +'.md'
    Lfile = open(log_file,'w')

    intro_str = "# Instruction \n"+                 "Welcome to the Toolbox4Tiros!\n"+                 "This tool helps summary the information and variables in "+                 "netCDF files in the current directory.\n" +                 "Please open this file with Typora for better performances.\n"
    Lfile.writelines(intro_str)
    return Lfile


# In[43]:


def read_netCDF(dataset,Lfile):
    Lfile.writelines('## General Information\n')
    Lfile.writelines('```C\n'+str(dataset)+'\n```\n')
    
    Lfile.writelines('## Dimensions\n')
    try:
        dim = dataset.dimensions.values()
    except Exception:
        Lfile.writelines('**Error**: Fail to read the dimension \n')
        Lfile.writelines('```C\n'+str(Exception)+'\n```\n')
        
    for each_dim in dim:
        Lfile.writelines('### '+each_dim.name+'\n')
        Lfile.writelines('```C\n'+str(each_dim)+'\n```\n')
        
    Lfile.writelines('## Variables\n')
    
        
    var_list = dataset.variables.keys()
    var = dataset.variables
    
    for ii, vv in enumerate(var_list):
        Lfile.writelines('### '+vv+'\n')
        Lfile.writelines('```C\n'+str(var[vv])+'\n```\n')
    
    

        # os.chdir("..")


# In[63]:


def all_netcdf(Lfile):
    filelist = glob.glob("*.*")
    for file in sorted(filelist, key=lambda s: s.lower()):
        if (len(file)>15 and file[0:15] == 'summary_netCDF.')  or (len(file)>3 and file[-3:]=='.md') or (len(file)>3 and file[-3:]=='.py') or (len(file)>6 and file[-6:]=='.ipynb') :
            continue
        Lfile.writelines('# '+file+'\n')
        try:
            dataset = Dataset(file)
        except Exception:
            Lfile.writelines('**ERROR**: Failed to read '+file+' as netCDF.\n')
            Lfile.writelines('- '+ str(Exception)+'\n')
            continue
        
        read_netCDF(dataset,Lfile)
        
    Lfile.close()
            
#         Lfile.writelines('\t page '+str(page1)+' - page '+str(page2)+'\n')
# except Exception:
#     traceback.print_exe(file=Lfile)


# In[65]:


Lfile = begin_log(name='summary_netCDF')
all_netcdf(Lfile)

