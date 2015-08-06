import Dorade
import matplotlib.pyplot as plt 
import numpy.ma as ma 
import numpy as np 


swp='swp.1010123212512.TA43P3.540.-19.5_AIR_v58'
foo=Dorade.Dorade(swp)

nrays=foo.getNumRays()
ngates=foo.getNumGates()

dbz=[]
for i in range(nrays):
        dbz.append(foo.getReflectivity(i))

DBZ=ma.asarray(dbz)

rays=np.linspace(0,2*np.pi,nrays)
gates=np.linspace(0,45,ngates)
r,theta = np.meshgrid(gates,rays) #rectangular plot of polar data

r2x=r*np.sin(theta)
r2y=r*np.cos(theta)

# fig,ax=plt.subplots()
# ax.imshow(DBZ,interpolation='none')
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.pcolormesh(r2x, r2y, DBZ) #X,Y & data2D must all be same dimensions
plt.show()
