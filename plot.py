import Dorade
import matplotlib.pyplot as plt 
import numpy.ma as ma 
import numpy as np 


swp='swp.1010123212512.TA43P3.540.-19.5_AIR_v58'
foo=Dorade.Dorade(swp)

""" get dimensions """
nrays=foo.getNumRays()
ngates=foo.getNumGates()

""" create 2D array """
dbz=[]
for i in range(nrays):
        dbz.append(foo.getReflectivity(i))
DBZ=ma.asarray(dbz)
DBZm=ma.masked_values(DBZ,-32768.0)

""" grid for polar data """
rays=np.linspace(0,2*np.pi,nrays)
gates=np.linspace(0,45,ngates)
r,theta = np.meshgrid(gates,rays) 
r2x=r*np.sin(theta)*-1
r2y=r*np.cos(theta)*-1


fig = plt.figure()
ax = fig.add_subplot(111)
ax.pcolormesh(r2x, r2y, DBZm) #X,Y & data2D must all be same dimensions
plt.show()
