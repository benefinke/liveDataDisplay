#####################################################
#  _   ______      ____    ________                 #
# |_| |   __  \   /    \  |__    __|TU Braunschweig #
#  _  |  |__|  | /  __  \    |  |                   #
# | | |  _____/ /  /__\  \   |  |    POSTPROCESSING #
# | | |  |     /  ______  \  |  |                   #
# |_| |__|    /__/      \__\ |__|         2017      #
#                                                   #
#####################################################

#################################################################################
#   Author: BeF 02-2017     Basic post-processing           Does it work? yes   #
#                                                                               #
#   Plots kinetic energy and courant number during simulation when started in   #
#   seperate terminal window  (Requires Input -> See Github-ReadMe for details) #
#################################################################################

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
import os
DEM_Timestep=1e-6 #OOOOOOO Needs adjusting

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = ax1.twinx()#fig.add_subplot(1,1,1)


pullData = open("../Results/Kinetic_energy.txt","r").read() #OOOOOOO Needs adjusting
#print "pullData: ",pullData
dataArray = pullData.split('\n')
#print "dataArray: ", dataArray
del dataArray[0]
#print "dataArray: ",dataArray
xar = []
yar = []
for eachLine in dataArray:
    if len(eachLine)>1:
        x,y = eachLine.split('\t')
        xar.append(float(x))
        yar.append(float(y))
ax1.clear()
ax1.plot(xar,yar, label='run')
ax1.set_xlabel('Timestep')
ax1.set_ylabel('Kinetic energy')
ax1.semilogy()
ax1.legend()
    #ax1.set_ylim([3.6751e-12,3.67815e-12])

case=os.path.relpath("..", "../..")
    #print case
ax1.set_title(case)
    #ax1.titlesize : large
    #ax1.set_yscale("log")
    
#==================================second line in graph ==================================
if os.path.isfile("../Results/Kinetic_energy_rec.txt")==True:          #OOOOOOO Needs adjusting
    pullData = open("../Results/Kinetic_energy_rec.txt","r").read()    #OOOOOOO Needs adjusting
    #print "pullData: ",pullData
    dataArray = pullData.split('\n')
    #print "dataArray: ", dataArray
    del dataArray[0]
    #print "dataArray: ",dataArray
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split('\t')
            xar.append(float(x))
            yar.append(float(y))
    #ax1.clear()
    ax1.plot(xar,yar,'r-', label='record')
    ax1.legend(loc=0)

#====================================Courant number plotting ================================

##### Definition of Diffusioncoefficient lists
Cmax=[]         # Maximum CourantNumber for given timestep
Cmean=[]        # Mean CourantNumber for given timestep
TimeInput=[]                   #Simulation time list
line2=str() # Buffer for fileinput (=line 1 loop ago)
line3=str() # Buffer for fileinput (=line 2 loops ago)

    #print "Starting CourantNumber Extraction from openfoam.log.............\n"

buffer=open("../openfoam.log", "r")   #OOOOOOO Needs adjusting
for line in buffer.readlines():
    if line.find("Courant") == 0 and line3.find("Time =") == 0: # Skips occurances of "Time= " where "Time= " is not the first word in line (comments etc.)
        TimeInput.append(float((line3.split())[2])/DEM_Timestep+1000)    # Saves 3rd word of list3 (=value) as float
        Cmean.append(float((line.split())[3]))
        Cmax.append(float((line.split())[5]))
    line3=line2
    line2=line

buffer.close()

TimeInput=np.array(map(float, TimeInput))       # convert lists into numpyarrays of type float
Cmean=np.array(map(float, Cmean))
Cmax=np.array(map(float, Cmax))

ax2.plot(TimeInput,Cmean,'g--', label='mean courant number')
ax2.plot(TimeInput,Cmax,'g-', label='max courant number')
#ax2.legend(loc=3)
ax2.set_ylabel('courant number')
#ax2.set_ylim([0,1.0])

#fig.legend(lines, labels)
#ani = animation.FuncAnimation(fig, animate, interval=1000)
#ani.title('Kinetic Energy')
#plt.show()
plt.savefig('../Results/liveData.png')      #OOOOOOO Needs adjusting
#plt.show('../Results/Kinetic_Energy.png')  #OOOOOOO Needs adjusting
plt.close()
