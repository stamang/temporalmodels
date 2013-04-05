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


fin =  open("C:\\Dropbox\\dissertation\\hepdata\\plt_toformat.txt","r")
#FILENAME = "C:\\Dropbox\\dissertation\\diabetes\\data_formatted\\1000_1025\\ContiMeas_12_17_12.txt"
fout = open("C:\\Dropbox\\dissertation\\hepdata\\plt_cluster_input.txt","w")

count =0
for line in fin:
    #print line
    if count ==0:
        count+=1
        continue
    temp = line.split("\t")
    pid = temp[0].strip()
    date = temp[1].strip()
    state = temp[2].strip()
    state = int(state)
    if state >= 350:
        state = "H"
        print >> fout,pid,"\t",date,"\t",state
        print pid,"\t",date,"\t",state
    elif state <= 120:
        state = "L"
        print >> fout,pid,"\t",date,"\t",state
        print pid,"\t",date,"\t",state
    elif state == "":
        continue
    else:
        state = "N"
        print >> fout,pid,"\t",date,"\t",state
        print pid,"\t",date,"\t",state

