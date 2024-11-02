#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pylab as plt
from netCDF4 import Dataset, num2date
import pandas as pd
#from mpl_toolkits.basemap import Basemap
import numpy as np
#import seaborn as sns; sns.set()
import networkx as nx
import csv


temp1 =  '/home/ruby/Desktop/Data/air.sig995.1979.nc'
temp2 =  '/home/ruby/Desktop/Data/air.sig995.1980.nc'
temp3 =  '/home/ruby/Desktop/Data/air.sig995.1981.nc'
temp4 =  '/home/ruby/Desktop/Data/air.sig995.1982.nc'
temp5 =  '/home/ruby/Desktop/Data/air.sig995.1983.nc'
temp6 =  '/home/ruby/Desktop/Data/air.sig995.1984.nc'
temp7 = '/home/ruby/Desktop/Data/air.sig995.1985.nc'
temp8 = '/home/ruby/Desktop/Data/air.sig995.1986.nc'
temp9 = '/home/ruby/Desktop/Data/air.sig995.1987.nc'
temp10 = '/home/ruby/Desktop/Data/air.sig995.1988.nc'
temp11 = '/home/ruby/Desktop/Data/air.sig995.1989.nc'

temp12 =  '/home/ruby/Desktop/Data/air.sig995.1990.nc'
temp13 =  '/home/ruby/Desktop/Data/air.sig995.1991.nc'
temp14 =  '/home/ruby/Desktop/Data/air.sig995.1992.nc'
temp15 =  '/home/ruby/Desktop/Data/air.sig995.1993.nc'
temp16 =   '/home/ruby/Desktop/Data/air.sig995.1994.nc'
temp17 =  '/home/ruby/Desktop/Data/air.sig995.1995.nc'
temp18 =  '/home/ruby/Desktop/Data/air.sig995.1996.nc'
temp19 =  '/home/ruby/Desktop/Data/air.sig995.1997.nc'
temp20 =  '/home/ruby/Desktop/Data/air.sig995.1998.nc'
temp21 = '/home/ruby/Desktop/Data/air.sig995.1999.nc'

temp22 = '/home/ruby/Desktop/Data/air.sig995.2000.nc'
temp23 = '/home/ruby/Desktop/Data/air.sig995.2001.nc'
temp24 = '/home/ruby/Desktop/Data/air.sig995.2002.nc'
temp25 = '/home/ruby/Desktop/Data/air.sig995.2003.nc'
temp26 = '/home/ruby/Desktop/Data/air.sig995.2004.nc'
temp27 = '/home/ruby/Desktop/Data/air.sig995.2005.nc'
temp28 = '/home/ruby/Desktop/Data/air.sig995.2006.nc'
temp29 = '/home/ruby/Desktop/Data/air.sig995.2007.nc'
temp30 = '/home/ruby/Desktop/Data/air.sig995.2008.nc'
temp31 = '/home/ruby/Desktop/Data/air.sig995.2009.nc'

temp32 = '/home/ruby/Desktop/Data/air.sig995.2010.nc'
temp33 = '/home/ruby/Desktop/Data/air.sig995.2011.nc'
temp34 = '/home/ruby/Desktop/Data/air.sig995.2012.nc'
temp35 = '/home/ruby/Desktop/Data/air.sig995.2013.nc'
temp36 = '/home/ruby/Desktop/Data/air.sig995.2014.nc'
temp37 = '/home/ruby/Desktop/Data/air.sig995.2015.nc'
temp38 = '/home/ruby/Desktop/Data/air.sig995.2016.nc'
temp39 = '/home/ruby/Desktop/Data/air.sig995.2017.nc'
temp40 = '/home/ruby/Desktop/Data/air.sig995.2018.nc'
temp41 = '/home/ruby/Desktop/Data/air.sig995.2019.nc'


fh1 = Dataset(temp1, mode = 'r')
fh2 = Dataset(temp2, mode = 'r')
fh3 = Dataset(temp3, mode = 'r')
fh4 = Dataset(temp4, mode = 'r')
fh5 = Dataset(temp5, mode = 'r')
fh6 = Dataset(temp6, mode = 'r')
fh7 = Dataset(temp7, mode = 'r')
fh8 = Dataset(temp8, mode = 'r')
fh9 = Dataset(temp9, mode = 'r')

fh10 = Dataset(temp10, mode = 'r')
fh11 = Dataset(temp11, mode = 'r')
fh12 = Dataset(temp12, mode = 'r')
fh13 = Dataset(temp13, mode = 'r')
fh14 = Dataset(temp14, mode = 'r')
fh15 = Dataset(temp15, mode = 'r')
fh16 = Dataset(temp16, mode = 'r')
fh17 = Dataset(temp17, mode = 'r')
fh18 = Dataset(temp18, mode = 'r')
fh19 = Dataset(temp19, mode = 'r')

fh20 = Dataset(temp20, mode = 'r')
fh21 = Dataset(temp21, mode = 'r')
fh22 = Dataset(temp22, mode = 'r')
fh23 = Dataset(temp23, mode = 'r')
fh24 = Dataset(temp24, mode = 'r')
fh25 = Dataset(temp25, mode = 'r')
fh26 = Dataset(temp26, mode = 'r')
fh27 = Dataset(temp27, mode = 'r')
fh28 = Dataset(temp28, mode = 'r')
fh29 = Dataset(temp29, mode = 'r')

fh30 = Dataset(temp30, mode = 'r')
fh31 = Dataset(temp31, mode = 'r')
fh32 = Dataset(temp32, mode = 'r')
fh33 = Dataset(temp33, mode = 'r')
fh34 = Dataset(temp34, mode = 'r')
fh35 = Dataset(temp35, mode = 'r')
fh36 = Dataset(temp36, mode = 'r')
fh37 = Dataset(temp37, mode = 'r')
fh38 = Dataset(temp38, mode = 'r')
fh39 = Dataset(temp39, mode = 'r')

fh40 = Dataset(temp40, mode = 'r')
fh41 = Dataset(temp41, mode = 'r')

air1 = fh1.variables['air'][:365]
air2 = fh2.variables['air'][:365]
air3 = fh3.variables['air'][:365]
air4 = fh4.variables['air'][:365]
air5 = fh5.variables['air'][:365]
air6 = fh6.variables['air'][:365]
air7 = fh7.variables['air'][:365]
air8 = fh8.variables['air'][:365]
air9 = fh9.variables['air'][:365]
air10 = fh10.variables['air'][:365]
air11 = fh11.variables['air'][:365]
air12 = fh12.variables['air'][:365]
air13 = fh13.variables['air'][:365]
air14 = fh14.variables['air'][:365]
air15 = fh15.variables['air'][:365]
air16 = fh16.variables['air'][:365]
air17 = fh17.variables['air'][:365]
air18 = fh18.variables['air'][:365]
air19 = fh19.variables['air'][:365]
air20 = fh20.variables['air'][:365]
air21 = fh21.variables['air'][:365]
air22 = fh22.variables['air'][:365]
air23 = fh23.variables['air'][:365]
air24 = fh24.variables['air'][:365]
air25 = fh25.variables['air'][:365]
air26 = fh26.variables['air'][:365]
air27 = fh27.variables['air'][:365]
air28 = fh28.variables['air'][:365]
air29 = fh29.variables['air'][:365]
air30 = fh30.variables['air'][:365]
air31 = fh31.variables['air'][:365]
air32 = fh32.variables['air'][:365]
air33 = fh33.variables['air'][:365]
air34 = fh34.variables['air'][:365]
air35 = fh35.variables['air'][:365]
air36 = fh36.variables['air'][:365]
air37 = fh37.variables['air'][:365]
air38 = fh38.variables['air'][:365]
air39 = fh39.variables['air'][:365]
air40 = fh40.variables['air'][:365]
air41 = fh41.variables['air'][:365]

time = fh14.variables['time'][:]
lat = fh14.variables['lat'][::3]
lon = fh14.variables['lon'][::5]

s=np.std(np.array([air1,air2,air3,air4,air5,air6,air7,air8,air9,air10,air11,air12,air13,air14,air15,air16,
                   air17,air18,air19,air20,air21,air22,air23,air24,air25, air26, air27, air28,air29,air30,
                   air31,air32, air33, air34,air35,air36,air37,air38,air39,air40,air41]),axis = 0)

m=np.mean(np.array([air1,air2,air3,air4,air5,air6,air7,air8,air9,air10,air11,air12,air13,air14,air15,air16,
                    air17,air18,air19,air20,air21,air22,air23,air24,air25, air26, air27, air28,air29,air30,
                    air31,air32, air33, air34,air35,air36,air37,air38,air39,air40,air41]),axis = 0)

x_14 = np.subtract(air36, m)
T_14 = np.divide(x_14, s)

jan_14=[]

for i in range(len(lat)):
        for j in range(len(lon)):
            for m in range(len(lat)):
                for n in range(len(lon)): 
                    jan_14.append( np.corrcoef(T_14[0:31,i,j],T_14[0:31, m,n])[0,1])
df = pd.DataFrame(data = jan_14)

B = np.reshape(jan_14, (725, 725))
A = B - np.diag(np.diag(B))

ls = []
for row in range(len(A)):
    for col in range(len(A)):
        if A[row][col] >= 0.5:
                ls.append((A[row][col],row,col))
                
df = pd.DataFrame(data = ls) 
ls.sort(reverse=True)
df1= pd.DataFrame(data = ls)
df1.columns=['corr', 'X', 'Y']
g =  nx.from_pandas_edgelist(df, source='X', target='Y', edge_attr='corr')
print(nx.transitivity(g))

