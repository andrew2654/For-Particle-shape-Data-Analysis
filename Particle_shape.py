# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:40:48 2019

@author: Andrew LIU
"""
import cv2
import numpy as np
import math
import itertools

frame = cv2.imread("C:/Users/Andrew LIU/Desktop/Feret Diameter_Test Image.png")
if frame is None:
  print("ERROR LOADING IMAGE")
  exit()
#    img_chs = cv2.split(frame)

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#blurred = cv2.GaussianBlur(frame, (11, 11), 0)
###    binaryIMG = cv2.Canny(blurred, 20, 160)
ret, blurred = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)
blurred, contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
shape_A = []
for i in range(0, len(contours)):
    hull = cv2.convexHull(contours[i])
    Ach = cv2.contourArea(hull)
    Ach = int(Ach)
    hull_all = []
    for pt in hull:
        hull_all.append(pt.flatten())
#    print("after convexHull, there are " + str(len(hull)) + " points", i+1)
#    cv2.drawContours(blurred,[hull],0,(255,0,0),-1)

    hull_x=[]
    hull_y=[]
    fList=[]
    for j in range(len(hull_all)):
        hull_x = hull_all[j][0]
        hull_y = hull_all[j][1]
        fList += [(hull_x, hull_y)]
    
#    x,y = float(mInput[0]), float(mInput[1])
#    fList += [(float(hull_x), float(hull_y))]
#arr_List = np.array(fList)
        
    def distance(p0, p1):
        return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    max_distance = distance(fList[0], fList[1])
        
    for p0, p1 in itertools.combinations(fList, 2):
        max_distance = max(max_distance, distance(p0, p1))
    #print(str(Ach),i+1)

    if Ach != 0:
        z = (max_distance)/(Ach /(max_distance))
    else:
        z = 0
    shape_A.append(z)
print(shape_A)

cv2.imshow("blurred",blurred)
#cv2.imshow("frame", frame)
cv2.waitKey(0)