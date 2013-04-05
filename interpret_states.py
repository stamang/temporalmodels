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


fin =  open("C:\\Dropbox\\dissertation\\hepdata\\plt_state_scale.csv","r")
#FILENAME = "C:\\Dropbox\\dissertation\\diabetes\\data_formatted\\1000_1025\\ContiMeas_12_17_12.txt"
fout = open("C:\\Dropbox\\dissertation\\hepdata\\clustering\\to_abstract_1_17.csv","w")

count =0
obsList = []

fline = 0

print >> fout, "clusters"
for line in fin:
    if fline == 0:
        fline=1
        continue
    #print line
    state = line.strip()
    state = float(state)
    if state >= 120:
        state = "1"
    elif (state<120 and state>=102):
        state = "3"
    elif (state<102 and state>=57):
        state = "2"
    elif (state<57):
        state = "4"
    elif state == "":
        continue
    print >> fout, state
#print pid,"\t",date,"\t",state, temp[2]

fout.close()
