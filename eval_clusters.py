#-------------------------------------------------------------------------------
# Name: aggregate the runs, then find the labels
from sklearn import metrics
import sys, string, re,os, time, pickle
##sys.path.append("/m3/KBP/results/cunyqa-suzanne-marissa-daniel-juan/system/scripts/answers_rvt")

def listDirectory(directory, fileExt):
    fileList=[]
    for filename in os.listdir(directory):
        filename=os.path.normcase(filename)
        if os.path.splitext(filename)[1][1:] == fileExt:  # [1:] start from after the dot
            fileList.append(filename)
    return fileList

hep_path = "C:\\Dropbox\\dissertation\\hepdata\\"
#pt labels
hep_labels = open(hep_path+"\\pt_labels_hep.csv","r")
#model parameters
fin_params = open(hep_path+"clustering\\feb_21\\4S\\abs_4S_basematrix_all.csv","r")

#+++++model specific+++++++
#output results
fout = hep_path +"clustering\\feb_21\\4S\\results.txt"
#dir of files to process
path = hep_path +"clustering\\feb_21\\4S\\clusters\\"

#hold the label values for patients
labelDict = {}

header = 1
for line in hep_labels:
    if header == 1:
        header = 0
        continue
    else:
        temppt = line.split(",")
        last=len(temppt)-1
        temppt[last] = temppt[last].strip()
        key=temppt[0]
        value = temppt[1:4]
        labelDict[key] = value

#hold the patient model parameters
paramDict = {}

header = 1
#maintains an ordered pt list for pairing cluster results
ptList=[]
for line in fin_params:
    if header == 1:
        header = 0
        continue
    else:
        line=line.replace('"','')
        temppt = line.split(",")
        key=int(temppt.pop(0))
        ptList.append(key)
        value = [float(temppt[i]) for i in range(1,11)]
        paramDict[key] = value

#get the results to process
#filepath for traversal for pattern count and sentence extraction
fileExt="csv"
fileList=listDirectory(path,fileExt)

#index for patient list


for clusterfile in fileList:
    i=0
    true_label = []
    assign_label = []
    fullDocFileName=path+clusterfile
    fbFile = open(fullDocFileName, "r")
    data_list = fbFile.readlines()
    data_list.pop(0)
    print "processing ", clusterfile

    for item in data_list:
        cluster = item[0]
        key = str(ptList[i])
        i+=1
        if key in labelDict:
            labels = labelDict[key]
            assign_label.append(cluster)
            true_label.append(labels[1])
            #print key, labels
        #else:
            #print key, " not found"

    listlen = len(assign_label)

    print listlen
    assign_label = [int(assign_label[i]) for i in range(listlen)]
    true_label = [int(true_label[i]) for i in range(listlen)]
    x1=metrics.homogeneity_score(true_label, assign_label)
    print x1
    x2=metrics.completeness_score(true_label, assign_label)
    print x2
    x3=metrics.adjusted_mutual_info_score(true_label, assign_label)
    print x3







