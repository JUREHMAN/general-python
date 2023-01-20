#Unsupervised learning for more dimensions (easy) Classify dynamically clusters of data in three dimensions.
#Generate a 3D sample with clusters.
#Run the algorithm with dynamic clustering.
#Make appropriate graphs for the three dimensions.
#Plot the projections onto lanes with selected 2 dimensions.
#Importing the Libraries
import numpy as np              # numeric
import matplotlib.pyplot as plt # plotting
import statistics as st         # statistics

# show imported graphics
from IPython.display import display, Image

import os.path 

isdir = os.path.isdir('lib_nn') # check whether 'lib_nn' exists

if not isdir:
   !git clone https://github.com/bronwojtek/lib_nn.git # cloning the library from github

import sys                     
sys.path.append('./lib_nn') 

from neural import *            # importing my library package
#Defining four points in a 3D space
def pA():
    return [np.random.uniform(.75, .95), np.random.uniform(.7, .9),np.random.uniform(.8,.85)] 

def pB():
    return [np.random.uniform(.4, .6), np.random.uniform(.6, .75),np.random.uniform(.65,.70)] 

def pC():
    return [np.random.uniform(.1, .3), np.random.uniform(.4, .5),np.random.uniform(.45,.48)] 

def pD():
    return [np.random.uniform(.7, .9), np.random.uniform(0, .2),np.random.uniform(.4,.85)] 
#Generating data points
samA=np.array([pA() for _ in range(30)])
samB=np.array([pB() for _ in range(25)])
samC=np.array([pC() for _ in range(22)])
samD=np.array([pD() for _ in range(28)])
#Plotting the data points in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(samA[:,0],samA[:,1],samA[:,2])
ax.scatter(samB[:,0],samB[:,1],samB[:,2])
ax.scatter(samC[:,0],samC[:,1],samC[:,2])
ax.scatter(samD[:,0],samD[:,1],samD[:,2])
ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#Defining the mean of the data points generated
rA=[st.mean(samA[:,0]),st.mean(samA[:,1]),st.mean(samA[:,2])]
rB=[st.mean(samB[:,0]),st.mean(samB[:,1]),st.mean(samB[:,2])]
rC=[st.mean(samC[:,0]),st.mean(samC[:,1]),st.mean(samC[:,2])]
rD=[st.mean(samD[:,0]),st.mean(samD[:,1]),st.mean(samD[:,2])]
#Defining colors
col=['red','blue','green','magenta']
#PLotting data points along with the mean
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(samA[:,0],samA[:,1],samA[:,2])
ax.scatter(samB[:,0],samB[:,1],samB[:,2])
ax.scatter(samC[:,0],samC[:,1],samC[:,2])
ax.scatter(samD[:,0],samD[:,1],samD[:,2])
ax.scatter(rA[0],rA[1],rA[2],c=col[0], s=90, alpha=0.5)
ax.scatter(rB[0],rB[1],rB[2],c=col[1], s=90, alpha=0.5)
ax.scatter(rC[0],rC[1],rC[2],c=col[2], s=90, alpha=0.5)
ax.scatter(rD[0],rD[1],rD[2],c=col[3], s=90, alpha=0.5)
ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#Voronoi Areas: Defining the square of the distance between two points in 3D space
def eucl(p1,p2): # square of the Euclidean distance
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 
#Function to choose the nearest color/neighbor
def col_char(p):
    dist=[eucl(p,rA),eucl(p,rB),eucl(p,rC),eucl(p,rD)] # array of distances
    ind_min = np.argmin(dist)                          # index of the nearest point
    return col[ind_min]
                                    # color of the nearest point
#Picking the nearest neighbor and plotting in the 3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for x1 in np.linspace(0,1,70): # 70 points in x
    for x2 in np.linspace(0,1,70): # 70 points in y
        for x3 in np.linspace(0,1,70): # 70 points in z
           ax.scatter3D(x1,x2,x3,c=col_char([x1,x2,x3])) 

ax.scatter(samA[:,0],samA[:,1],samA[:,2],c='black', s=10)
ax.scatter(samB[:,0],samB[:,1],samB[:,2],c='black', s=10)
ax.scatter(samC[:,0],samC[:,1],samC[:,2],c='black', s=10)
ax.scatter(samD[:,0],samD[:,1],samD[:,2],c='black', s=10)

ax.scatter(rA[0],rA[1],rA[2],c='black', s=90, alpha=.5)
ax.scatter(rB[0],rB[1],rB[2],c='green', s=90, alpha=.5)
ax.scatter(rC[0],rC[1],rC[2],c='red', s=90, alpha=.5)
ax.scatter(rD[0],rD[1],rD[2],c='blue', s=90, alpha=.5)

ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#Naive Clusterization
alls=np.concatenate((samA, samB, samC, samD))
np.random.shuffle(alls)
#Starting with one representative point and training the network
R=np.array([np.random.random(),np.random.random(),np.random.random()]) # initial location

print("initial location:")
print(np.round(R,3))
print("round   location")

eps=.5                         # initial learning speed

for j in range(50):            # rounds
    eps=0.85*eps               # decrease the learning speed 
    np.random.shuffle(alls)    # reshuffle the sample
    for i in range(len(alls)): # loop over points of the whole sample
        R+=eps*(alls[i]-R)     # update/learning
    if j%5==4: print(j+1, "    ",np.round(R,3))  # print every 5th step
    
#Checking the position of the characterstic point
R_mean=[st.mean(alls[:,0]),st.mean(alls[:,1]),st.mean(alls[:,2])]
print(np.round(R_mean,3))
#PLotting for one characterstic point
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(alls[:,0],alls[:,1],alls[:,2],c='brown', s=10)
ax.scatter(R[0],R[1],R[2],c='black', s=90, alpha=.5)
ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#Starting with two representative points
R1=np.array([np.random.random(), np.random.random(), np.random.random()])
R2=np.array([np.random.random(), np.random.random(), np.random.random()])
#Training for two representative points
print("initial locations:")
print(np.round(R1,3), np.round(R2,3))
print("rounds  locations")

eps=.5

for j in range(40):             
    eps=0.85*eps
    np.random.shuffle(alls) 
    for i in range(len(alls)):
        p=alls[i]   
        dist=[func.eucl(p,R1), func.eucl(p,R2)] # squares of distances
        ind_min = np.argmin(dist)               # index of the minimum
        if ind_min==0:         # if R1 closer to the new data point
            R1+=eps*(p-R1)     # update R1                
        else:                  # if R2 closer ... 
            R2+=eps*(p-R2)     # update R2       

    if j%5==4: print(j+1,"    ", np.round(R1,3), np.round(R2,3)) 
#PLotting for two representative points
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(alls[:,0],alls[:,1],alls[:,2],c='brown', s=10)
ax.scatter(R1[0],R1[1],R1[2],c='black', s=90, alpha=.5)
ax.scatter(R2[0],R2[1],R2[2],c='red', s=90, alpha=.5)

ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#Starting with four representative points
R1=np.array([np.random.random(), np.random.random(), np.random.random()])
R2=np.array([np.random.random(), np.random.random(), np.random.random()])
R3=np.array([np.random.random(), np.random.random(), np.random.random()])
R4=np.array([np.random.random(), np.random.random(), np.random.random()])


print("initial locations:")
print(np.round(R1,3), np.round(R2,3), np.round(R3,3), np.round(R4,3))   
print("rounds   locations")

eps=.5

for j in range(40):
    eps=0.85*eps
    np.random.shuffle(alls)
    for i in range(len(alls)):
        p=alls[i]
        dist=[func.eucl(p,R1), func.eucl(p,R2), func.eucl(p,R3), func.eucl(p,R4)]
        ind_min = np.argmin(dist)
        if ind_min==0:
            R1+=eps*(p-R1)
        elif ind_min==1:
            R2+=eps*(p-R2)  
        elif ind_min==2:
            R3+=eps*(p-R3)  
        else:
            R4+=eps*(p-R4) 
    if j%5==4: print(np.round(R1,3), np.round(R2,3), np.round(R3,3), np.round(R4,3))   

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(alls[:,0],alls[:,1],alls[:,2],c='brown', s=10)
ax.scatter(R1[0],R1[1],R1[2],c='black', s=90, alpha=.5)
ax.scatter(R2[0],R2[1],R2[2],c='red', s=90, alpha=.5)
ax.scatter(R3[0],R3[1],R3[2],c='green', s=90, alpha=.5)
ax.scatter(R4[0],R4[1],R4[2],c='yellow', s=90, alpha=.5)
ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()           
#Dynamic cluserization
d=0.2   # clustering scale
eps=0.5 # initial learning speed

for r in range(20):               # rounds
    eps=0.85*eps                  # decrease the learning speed 
    np.random.shuffle(alls)       # shuffle the sample
    if r==0:                      # in the first round
        R=np.array([alls[0]])     # R - array of representative points
                                  # initialized to the first data point
    for i in range(len(alls)):    # loop over the sample points
        p=alls[i]                 # new data point
        dist=[func.eucl(p,R[k]) for k in range(len(R))] 
         # array of squares of distances of p from the current repr. points in R
        ind_min = np.argmin(dist) # index of the closest repr. point
        if dist[ind_min] > d*d:   # if its distance square > d*d
                                  # dynamical creation of a new category
            R=np.append(R, [p], axis=0)    # add new repr. point to R
        else:   
            R[ind_min]+=eps*(p-R[ind_min]) # otherwise, apdate the "old" repr. point

print("Number of representative points: ",len(R))
#2D Plots
#For 2D plot
fig=plt.figure(figsize=(2.3,2.3),dpi=120)
plt.title("d="+str(d),fontsize=10) 
plt.xlim(-.1,1.1)
plt.ylim(-.1,1.1)
    
# drawing the circles
for k in range(len(R)):
    circ=plt.Circle((R[k][0],R[k][1]), radius=d, color='orange', fill=True, alpha=0.5)
    plt.gca().add_artist(circ)

# the sample points         
plt.scatter(alls[:,0],alls[:,1],c='brown', s=10 ,zorder=5)

# characteristic points
for k in range(len(R)):
    plt.scatter(R[k][0],R[k][1],c='black', s=20, zorder=10)

plt.xlabel('$x_1$',fontsize=11)
plt.ylabel('$x_2$',fontsize=11)
plt.show()
#3D plottig
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# drawing the circles
for k in range(len(R)):
    circ=plt.Circle((R[k][0],R[k][1]), radius=d, color='orange', fill=True, alpha=0.5)
    ax.add_patch(circ)
    art3d.pathpatch_2d_to_3d(circ, z=0, zdir="y")
# the sample points         
ax.scatter(alls[:,0],alls[:,1],alls[:,2],c='brown', s=10 ,zorder=5)
# characteristic points
for k in range(len(R)):
    ax.scatter(R[k][0],R[k][1],R[k][2],c='black', s=20, zorder=10)
    ax.scatter(R1[0],R1[1],R1[2],c='black', s=90, alpha=.5)
    ax.scatter(R2[0],R2[1],R2[2],c='black', s=90, alpha=.5)
    ax.scatter(R3[0],R3[1],R3[2],c='black', s=90, alpha=.5)
    ax.scatter(R4[0],R4[1],R4[2],c='black', s=90, alpha=.5)

ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
#
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# drawing the circles
for k in range(len(R)):
    circ=plt.Circle((R[k][0],R[k][1]), radius=d, color='orange', fill=True, alpha=0.5)
    ax.add_patch(circ)
    art3d.pathpatch_2d_to_3d(circ, z=0, zdir="x")
# the sample points         
ax.scatter(alls[:,0],alls[:,1],alls[:,2],c='brown', s=10 ,zorder=5)
# characteristic points
for k in range(len(R)):
    ax.scatter(R[k][0],R[k][1],R[k][2],c='black', s=20, zorder=10)
    ax.scatter(R1[0],R1[1],R1[2],c='black', s=90, alpha=.5)
    ax.scatter(R2[0],R2[1],R2[2],c='blue', s=90, alpha=.5)
    ax.scatter(R3[0],R3[1],R3[2],c='green', s=90, alpha=.5)
    ax.scatter(R4[0],R4[1],R4[2],c='red', s=90, alpha=.5)

ax.set_xlabel('$x_1$',fontsize=14)
ax.set_ylabel('$x_2$',fontsize=14)
ax.set_zlabel('$x_3$',fontsize=14)
plt.show()
