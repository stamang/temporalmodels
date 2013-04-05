#-------------------------------------------------------------------------------
# Name:        format_platelet
# Purpose:     format platelet data
#
# Author:      suzy
#
# Created:     20/12/2012
# Copyright:   (c) suzy 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------


fin =  open("C:\\Dropbox\\dissertation\\hepdata\\clustering\\plt_toformat.txt","r")
#FILENAME = "C:\\Dropbox\\dissertation\\diabetes\\data_formatted\\1000_1025\\ContiMeas_12_17_12.txt"
fout = open("C:\\Dropbox\\dissertation\\hepdata\\clustering\\plt_abstract_input.csv","w")

count =0
obsList = []

for line in fin:
    #print line
    if count ==0:
        count+=1
        continue
    temp = line.split("\t")
    if temp[2]=="\n":
        continue
    pid = int(temp[0].strip())
    date = temp[1].strip()
    state = temp[2].strip()
    state = float(state)
    state=state//1
    if state >= 350:
        state = "3"
    elif state <= 120:
        state = "1"
    elif state == "":
        continue
    else:
        state = "2"
    obsList.append([pid,date,state,temp[2].strip()])

#sort so the format won't throw errors in msm package
obsList.sort(key = lambda c: (c[0],c[1]))

for item in obsList:
    print >> fout,item[0],",",item[1],",",item[2],",",item[3]
#print pid,"\t",date,"\t",state, temp[2]

fout.close()
