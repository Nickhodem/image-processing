"""
skrypt testujacy test mierzacy czas wykonywania skryptu
"""
import time
import cv2
img1=cv2.imread('laska.jpg')

f1=time.clock()
g1=time.time()
for i in xrange(5,99,2):
    img1 = cv2.medianBlur(img1,i)

f2=time.clock()
g2=time.time()
df=f2-f1
dg=g2-g1
print 'roznica miedzy funkcjami: '+str(dg-df)


e1 = cv2.getTickCount()
for i in xrange(5,99,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t




print df
print 'roznica czasu to'
print df-t
