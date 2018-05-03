from PIL import Image
import numpy as np

key1    = Image.open("key1.png")
key2    = Image.open("key2.png")
I       = Image.open("I.png")
E       = Image.open("E.png")
Eprime  = Image.open("Eprime.png")

W , H = key1.size

data = np.zeros((120000,3),int)
E_ar = np.zeros((120000),int)

for y in range(H):
    for x in range(W):
        data[y*400+x][0] =  I.getpixel((x,y))
        data[y*400+x][1] =  key1.getpixel((x,y))
        data[y*400+x][2] =  key2.getpixel((x,y))
        E_ar[y*400+x]    =  E.getpixel((x,y))
