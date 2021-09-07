import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
from tqdm import tqdm
from datetime import datetime

power = 15
N = 4000
cmap = 'hot'
size = 10
scale = N /4


arg1 = complex( 1, 0) #/math.sqrt(2)
arg2 = complex(-1, 0)


def log_dansity_map(val, max_count):
    max_count +=1
    brightness = math.log(val) / math.log(max_count)
    gamma = 2.2
    brightness = math.pow(brightness, 1/gamma)

    return brightness


def run(it):
    power = it
    coef = np.zeros((N, N))
    
    for  i in tqdm(range(2**power)): #range(2**power)

        k = format(i, "b")
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)

        listK = np.empty((power), dtype = np.complex128)

        for p in range(len(k)):
            #if p == len(k) -1:
            #if p == 0:
            #    listK[p] = complex(100, 0)
            if k[p] == '0':
                listK[p] = arg1
            else:
                listK[p] = arg2

        #print(listK)
        magn = np.linalg.norm(listK)


        k = np.polynomial.Polynomial(listK)
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * scale + N/2)
            y = round(np.real( j ) * scale + N/2)

            if x < N and x > 0 and y < N and y > 0 and magn > 1 and np.imag( j ) != 0 :
                coef[x, y] += 1

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    #filenameArr = f'coef_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}'
    #np.save(filenameArr, coef)

    ####

    max_count = np.max(coef)

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] = 256*log_dansity_map(coef[i, j], max_count)

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos' )

    now =  str(datetime.now()).replace(" ", '_')
    now =  now.replace(":", '_')

    filenameImage = f'N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_{now}.png'
    
    print(filenameImage)

    plt.savefig( filenameImage, bbox_inches = 'tight', pad_inches=0.0 )

    #plt.show()
    plt.close()

def run_increase_dot(it):
    power = it
    coef = np.zeros((N, N))
    if it < 15:
        diam = 30 - it
    else:
        diam = 2
    
    for  i in tqdm(range(2**power)): #range(2**power)

        k = format(i, "b")
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)

        listK = np.empty((power), dtype = np.complex128)

        for p in range(len(k)):
            #if p == len(k) -1:
            if p == 0:
                listK[p] = complex(100, 0)
            elif k[p] == '0':
                listK[p] = arg1
            else:
                listK[p] = arg2

        #print(listK)

        k = np.polynomial.Polynomial(listK)
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * scale + N/2)
            y = round(np.real( j ) * scale + N/2)

            r = diam//2
            for c in range(diam+1):
                for d in range(diam+1):

                    tempx = x + c - r
                    tempy = y + d - r
                    dist = math.dist((tempx, tempy), (x, y))

                    if dist < r and tempx < N and tempx > 0 and tempy < N and tempy > 0 :
                        coef[tempx, tempy] += r/(dist + 1)

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    #filenameArr = f'coef_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}'
    #np.save(filenameArr, coef)

    ####

    #max_count = np.max(coef)

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 20 

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos' )

    now =  str(datetime.now()).replace(" ", '_')
    now =  now.replace(":", '_')

    filenameImage = f'K{it}_N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_{now}.png'
    
    print(filenameImage)

    plt.savefig( filenameImage, bbox_inches = 'tight', pad_inches=0.0 )

    plt.show()
    plt.close()

def run_animation ():
    print('start')
    dt = complex(1, 0.005)

    for i in range(350):
        arg1 = arg1 * dt / abs(dt)

        arg2 = arg2 * np.conjugate(dt) / abs(dt)

        run(i)

        #print(i)


def run_animation_pow ():
    for i in range(2, 22):

        run_increase_dot(i)

        print(i)

def run_animation_pow ():
    for i in range(2, 22):

        run_increase_dot(i)

        print(i)


def sqrt(k):
  n = math.floor(math.sqrt(k))
  temp = n + (k -n**2)/(2*n)
  print(temp)
  for i in range(3):
    temp = temp/2 + k/(2*temp)
  return temp

if __name__ == '__main__':
    #print(90/(np.angle(complex(1, 0.005))*57.2958) )
    #run_animation_pow()
    run(0)
    
    
