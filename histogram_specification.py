import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import random

#function for matching histogram
def search(arr, x):
    for i in range(256):
        if arr[i]>=x:
            return i
        
#user define value       
miu, sigma = [int(x) for x in input("Enter miu and sigma : ").split()]

#input image
img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image',img)
#input image histogram
plt.hist(img.ravel(),256,[0,255])
plt.show()
#image total length
z = img.shape[0]*img.shape[1]


#gaussian / normal distribution
g = random.normal(miu, sigma, size=(img.shape[0],img.shape[1]))
#print(g)
#round up and type cust to int from float
g = np.round(g).astype(int);
# make the range between 0-255
g[g>255]=255
g[g<0]= 0
#print(g[2][2])
#g = (255*(gaussian - np.min(gaussian))/np.ptp(gaussian)).astype(int)

#print(g)
#print the gaussian histogram
plt.hist(g.ravel(),256,[0,255])
plt.show()


n = np.zeros((256), dtype=float)        #input image frequency variable
n2 = np.zeros((256), dtype=float)       #gaussian distribution frequency variable
p = np.zeros((256), dtype=float)        #input image probability variable
p2 = np.zeros((256), dtype=float)       #gaussian distribution probability variable
s = np.zeros((256), dtype=int)          #input image cdf variable
s2 = np.zeros((256), dtype=int)         #gaussian distribution cdf variable

x = 0

#find the frequency in input image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n[img[i][j]]=n[img[i][j]]+1


#  find the frequency in gaussian distribution
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        n2[g[i][j]]=n2[g[i][j]]+1        

# use histogram equalization in input image
for i in range(0,256):
    p[i]=n[i]/(z)
    x = x+p[i]
    s[i]=round(255*x)
    

x=0
# use histogram equalization in gaussian distribution
for i in range(0,256):
    p2[i]=n2[i]/(z)
    x = x+p2[i]
    s2[i]=round(255*x)


#finally apply histrogram matching
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        val = img[i][j]
        res = search(s2,s[val])
        img.itemset((i,j),res)

#show the output histogram and image
plt.hist(img.ravel(),256,[0,255])
plt.show()     
cv2.imshow('output image', img)

cv2.imwrite("output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows() 
