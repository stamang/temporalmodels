#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-------------------------------------------------------------------------------
# Purpose:     format data for msm package
# Author:      suzy
# Created:     12/26/12
# Copyright:   (c) suzy 2012
#-------------------------------------------------------------------------------
path = "C:\\Dropbox\\dissertation\\hepdata\\"

fin =  open("plt_state_scale.csv","r")
#FILENAME = "C:\\Dropbox\\dissertation\\diabetes\\data_formatted\\1000_1025\\ContiMeas_12_17_12.txt"
fout = open("to_abstract_1_17.csv","w")

print>>fout,"pid",",","time",",","state"

count11=0.0
count12=0.0
count13=0.0
count14=0.0
count21=0.0
count22=0.0
count23=0.0
count24=0.0
count31=0.0
count32=0.0
count33=0.0
count34=0.0
count41=0.0
count42=0.0
count43=0.0
count44=0.0

curr=1

def getstate(value):

    if value >= 11:
        state = 4
    elif value >= 4:
        state = 3
    elif value >= 2:
        state = 2
    else:
        state = 1
    return state

for line in fin:
    prev=curr
    temp = line.split(",")
    pid = temp[0]
    time = temp[1]
    value = int(temp[2].strip())
    state = getstate(value)
    curr=state
    if prev==1 and curr ==1:
        count11+=1
    if prev==1 and curr ==2:
        count12+=1
    if prev==1 and curr ==3:
        count13+=1
    if prev==1 and curr ==4:
        count14+=1
    if prev==2 and curr ==1:
        count21+=1
    if prev==2 and curr ==2:
        count22+=1
    if prev==2 and curr ==3:
        count23+=1
    if prev==2 and curr ==4:
        count24+=1
    if prev==3 and curr ==1:
        count31+=1
    if prev==3 and curr ==2:
        count32+=1
    if prev==3 and curr ==3:
        count33+=1
    if prev==3 and curr ==4:
        count34+=1
    if prev==4 and curr ==1:
        count41+=1
    if prev==4 and curr ==2:
        count42+=1
    if prev==4 and curr ==3:
        count43+=1
    if prev==4 and curr ==4:
        count44+=1


#    print value, state
    print>>fout,pid,",",time,",",state

total1 = count11+count12+count13+count14
total2 = count21+count22+count23+count24
total3 = count31+count32+count33+count34
total4 = count41+count42+count43+count44

print count11/total1, count12/total1, count13/total1, count14/total1
print count21/total2, count22/total2, count23/total2, count24/total2
print count31/total3, count32/total3, count33/total3, count34/total3
print count41/total3, count42/total3, count43/total3, count44/total4

fout.close()
fin.close()







