'''
Code to calculate clusters using a Dirichlet Process
Gaussian mixture model.

Requires scikit-learn:
  http://scikit-learn.org/stable/
'''

import numpy
from sklearn import mixture

#fin = "C:\\Dropbox\\dissertation\\hepdata\\tocluster_V2.csv"
fin = "C:\\Dropbox\\dissertation\\hepdata\\clustering\\feb_20\\5S\\logMatrix.csv"
fout = open("C:\\Dropbox\\dissertation\\hepdata\\clustering\\feb_20\\5S\\clusters\\run5.csv","w")

# Note: you'll have to remove the last "name" column in the file (or
# some other such thing), so that all the columns are numeric.
x = numpy.loadtxt(open(fin, "rb"), delimiter = ",", skiprows = 1)
#print x[1]

n = 100
a = .1

n_components = n
alpha = a

dpgmm = mixture.DPGMM(n_components = n, alpha = a)

dpgmm.fit(x)
clusters = dpgmm.predict(x)

##print >> fout, "components:","\t",n_components
##print >> fout, "alpha:","\t",alpha,"\n"

print "components:","\t",n_components
print "alpha:","\t",alpha,"\n"

numClusters = []
print >> fout, "cluster"
for item in clusters:
    if item not in numClusters:
        numClusters.append(item)
    print >> fout, item
##print>> fout, "\n","clusters:", len(numClusters)
print "clusters:", len(numClusters)
fout.close()
