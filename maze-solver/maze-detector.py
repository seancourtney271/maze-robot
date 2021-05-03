import cv2
import numpy as np
import os

filename = './maze-solver/images/maze.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
centroids = centroids[1:]
corners = corners[1:]
#print(centroids)
# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
#img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]




#for index in range(1,len(corners)-1):
#    #print(corners[index+1])
#    #print(corners[index])
#    dist = np.subtract(corners[index+1],corners[index])
#    #print(dist)
#    
#    dist = dist**2
#    #print(dist)
#    
#    dist = np.sqrt(np.sum(dist))
#    #print(dist)
#    #print("--------")
#    print(corners[index])
#    if(dist <= 20):
#        print(int(corners[index][0]))
#        print(int(corners[index][1]))
#        img[int(corners[index][0]),int(corners[index][1])] = [255,0,0]
#        img[int(corners[index+1][0]),int(corners[index+1][1])] = [255,0,0]

cv2.imwrite('subpixel5.png',img)