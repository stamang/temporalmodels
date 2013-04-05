'''
Code to calculate clusters using a Dirichlet Process
Gaussian mixture model.

Requires scikit-learn:
  http://scikit-learn.org/stable/
'''

import numpy
from sklearn import mixture

FILENAME = "C:\\Dropbox\\dissertation\\hepdata\\plt_low_values.csv"

# Note: you'll have to remove the last "name" column in the file (or
# some other such thing), so that all the columns are numeric.
x = numpy.loadtxt(open(FILENAME, "rb"), delimiter = ",", skiprows = 0)
print x[1]
dpgmm = mixture.DPGMM(n_components = 10, alpha = 1)

dpgmm.fit(x)
clusters = dpgmm.predict(x)


fout = open("C:\\Dropbox\\dissertation\\hepdata\\plt_low_scale.csv","w")
numClusters=[]

print"cluster list is ",len(clusters)," patients long"
for item in clusters:
    if item not in numClusters:
        numClusters.append(item)
print "clusters:", len(numClusters)

print >> fout, "cluster"
for item in clusters:
    print >> fout, item

fout.close()
