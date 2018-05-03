from PIL import Image
import numpy as np
import scipy.misc

#讀取圖檔

key1    = Image.open("key1.png")
key2    = Image.open("key2.png")
I       = Image.open("I.png")
E       = Image.open("E.png")
Eprime  = Image.open("Eprime.png")

#設置高寬

W , H = key1.size

#創建array

data = np.zeros((120000,3),int)
E_ar = np.zeros((120000),int)

#讀入key1,key2,I至data

for y in range(H):
    for x in range(W):
        data[y*400+x][0] =  key1.getpixel((x,y))
        data[y*400+x][1] =  key2.getpixel((x,y))
        data[y*400+x][2] =  I.getpixel((x,y))
        E_ar[y*400+x]    =  E.getpixel((x,y))

w = np.array([0,0,0])

#LMS

A = 0.00001
maxlimit = 10
w0 = 1
w1 = 1
w2 = 1

epoch = 1
while epoch < maxlimit and abs(w[0] - w0) > 0.00001 and abs(w[1] - w1) > 0.00001 and abs(w[2] - w2) > 0.00001:
    
    w0 = w[0]
    w1 = w[1]
    w2 = w[2]
    
    for i, x in enumerate(data): 
            a = w[0] * x[0] + w[1] * x[1] + w[2] * x[2]
            e = E_ar[i] - a
            w = w + A * e * x

    print(w[0], w[1], w[2])
    epoch += 1

#輸出

out = np.zeros((H,W),int)

for y in range(H):
    for x in range(W):
        out[y][x] = (Eprime.getpixel((x,y)) - w[0] *key1.getpixel((x,y)) -w[1] * key2.getpixel((x,y)))/w[2]
        
        
    

scipy.misc.imsave('output.jpg', out)
