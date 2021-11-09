import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import random


def search(arr, x):
    for i in range(256):
        if arr[i]>=x:
            return i
        
miu, sigma = [int(x) for x in input("Enter miu and sigma : ").split()]

img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image',img)
plt.hist(img.ravel(),256,[0,255])
plt.show()
z = img.shape[0]*img.shape[1]



g = random.normal(miu, sigma, size=(img.shape[0],img.shape[1]))
#print(g)
g = np.round(g).astype(int);
g[g>255]=255
g[g<0]= 0
#print(g[2][2])
#g = (255*(gaussian - np.min(gaussian))/np.ptp(gaussian)).astype(int)

#print(g)

plt.hist(g.ravel(),256,[0,255])
plt.show()

n = np.zeros((256), dtype=float)
n2 = np.zeros((256), dtype=float)
p = np.zeros((256), dtype=float)
p2 = np.zeros((256), dtype=float)
s = np.zeros((256), dtype=int)
s2 = np.zeros((256), dtype=int)

x = 0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n[img[i][j]]=n[img[i][j]]+1


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n2[g[i][j]]=n2[g[i][j]]+1        

    
for i in range(0,256):
    p[i]=n[i]/(z)
    x = x+p[i]
    s[i]=round(255*x)
    

x=0

for i in range(0,256):
    p2[i]=n2[i]/(z)
    x = x+p2[i]
    s2[i]=round(255*x)


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        val = img[i][j]
        res = search(s2,s[val])
        img.itemset((i,j),res)


plt.hist(img.ravel(),256,[0,255])
plt.show()     
cv2.imshow('output image', img)

cv2.imwrite("output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows() 
