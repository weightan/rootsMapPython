import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
from tqdm import tqdm
from datetime import datetime

power = 18
N = 5000
cmap = 'hot'

base = 2
scale = N * 0.6 #0.7
size = 10


def log_dansity_map(val, max_count):
    max_count +=1
    brightness = math.log(val) / math.log(max_count)
    gamma = 2.2
    brightness = math.pow(brightness, 1/gamma)

    return brightness

def run():

    arg1 = complex(0, 0)
    arg2 = complex(1, 0)
    arg3 = complex(0, 1)

    #arg1 = arg1/abs(arg1)
    #arg2 = (arg2/abs(arg2))#*0.001
    #arg3 = (arg3/abs(arg3))#0.001


    coef = np.zeros((N, N), dtype = np.int32)
    
    for  i in tqdm(range(base**power)):

        #k = bin(i)[2:]

        newNum = ''
        num = i

        while num > 0:
            newNum = str(num % base) + newNum
            num //= base

        k = newNum   
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)
        listK = np.empty((power), dtype=np.complex128)

        for p in range(len(k)):
            if p == len(k) -1:
                listK[p] = complex(100, 0)
            if k[p] == '0':
                listK[p] = arg1
            elif  k[p] == '1':
                listK[p] = arg2
            else:
                listK[p] = arg3

        #print(listK)

        k = np.polynomial.Polynomial(listK)
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * scale + N/2)
            y = round(np.real( j ) * scale + N/2)

            if x < N and x > 0 and y < N and y > 0:
                coef[x, y] += 1

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    filenameArr = f'N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####
    max_count = np.max(coef)

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] = 256*log_dansity_map(coef[i, j], max_count) 
    ####

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap)#, interpolation='bicubic' )

    ####

    filenameImage = f'N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight')

    ####

    #plt.show()
    plt.close()

def run_increase_dot_f(it, constt):
    power = it
    
    diam = round(26 - 2*it)
    if diam <=3:
        pass
    diam = 10

    #args = np.roots([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0  , 0 , -1])

    #base = len(args)
    arg1 = -1
    arg2 = 1
    arg3 = 1j
    arg4 = 0
    arg5 = -1j

    coef = np.zeros((N, N), dtype = np.int32)
    
    for  i in tqdm(range(base**power)):

        #k = bin(i)[2:]

        newNum = ''
        num = i

        while num > 0:
            newNum = str(num % base) + newNum
            num //= base

        k = newNum   
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)
        listK = np.empty((power), dtype=np.complex128)

        for p in range(len(k)):
            if p == len(k) -1:
                listK[p] = constt
            elif k[p] == '0':
                listK[p] = arg1
            elif  k[p] == '1':
                listK[p] = arg2
            elif k[p] == '2' :
                listK[p] = arg3
            elif k[p] == '3':
                listK[p] = arg4
            else :
                listK[p] = arg5
        #print(listK)

        k = np.polynomial.Polynomial(listK)
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * scale + N/2)
            y = round(np.real( j ) * scale + N/2)

            r = diam//2
            if (not(np.imag( j ) == 0 and np.real( j )==0)): #and (abs(np.imag( j )) > 0.000001):

                for c in range(diam+1):
                    for d in range(diam+1):

                        tempx = x + c - r
                        tempy = y + d - r
                        dist = math.dist((tempx, tempy), (x, y))

                        if dist < r and tempx < N and tempx > 0 and tempy < N and tempy > 0 :
                            coef[tempx, tempy] += r/(dist + 1)

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    #filenameArr = f'K{it}_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 200 
    ####

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap)

    ####

    now =  str(datetime.now()).replace(" ", '_')
    now =  now.replace(":", '_')

    filenameImage = f'C_{constt}N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}_{now}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight', pad_inches=0.0 )

    ####

    #plt.show()
    plt.close()
        
def run_increase_dot(it):
    power = it
    
    diam = round(30 - 2*it)

    args = np.roots([1, 0, 0, -1])
    arg1 = args[0]
    arg2 = args[1]
    arg3 = args[2]

    coef = np.zeros((N, N), dtype = np.int32)
    
    for  i in tqdm(range(base**power)):

        #k = bin(i)[2:]

        newNum = ''
        num = i

        while num > 0:
            newNum = str(num % base) + newNum
            num //= base

        k = newNum   
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)
        listK = np.empty((power), dtype=np.complex128)

        for p in range(len(k)):
            if p == len(k) -1:
                listK[p] = complex(10, 0)
            elif k[p] == '0':
                listK[p] = arg1
            elif  k[p] == '1':
                listK[p] = arg2
            else:
                listK[p] = arg3

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

    #filenameArr = f'K{it}_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 300 
    ####

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos' )

    ####

    now =  str(datetime.now()).replace(" ", '_')
    now =  now.replace(":", '_')

    filenameImage = f'N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}_{now}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight', pad_inches=0.0 )

    ####

    #plt.show()
    plt.close()

def run_increase_dot_const(it, constt, dt, p):
    power = it

    
    arg1 = -1
    arg2 = 1
    arg3 = 1j
    arg4 = 0
    arg5 = -1j

    coef = np.zeros((N, N), dtype = np.int32)
    
    for  i in tqdm(range(base**power)):

        #k = bin(i)[2:]

        newNum = ''
        num = i

        while num > 0:
            newNum = str(num % base) + newNum
            num //= base

        k = newNum   
        k = k.zfill(power)
        #k = k.replace('0', '2')
        #k = list(k)
        listK = np.empty((power), dtype=np.complex128)

        for p in range(len(k)):
            if p == len(k) -1:
                listK[p] = constt
            elif k[p] == '0':
                listK[p] = arg1
            elif  k[p] == '1':
                listK[p] = arg2
            elif k[p] == '2' :
                listK[p] = arg3
            elif k[p] == '3':
                listK[p] = arg4
            else :
                listK[p] = arg5
        #print(listK)

        k = np.polynomial.Polynomial(listK)
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * scale + N/2)
            y = round(np.real( j ) * scale + N/2)

            if p and np.imag( j ) !=0:
                if  x < N and x > 0 and y < N and y > 0 :
                    coef[x, y] = 1

                if  x-1 < N and x-1 > 0 and y < N and y > 0 :
                    coef[x-1, y] = 1
                if  x+1 < N and x+1 > 0 and y < N and y > 0 :
                    coef[x+1, y] = 1
                if  x < N and x > 0 and y -1< N and y-1> 0 :
                    coef[x, y-1] = 1
                if  x < N and x > 0 and y+1 < N and y+1 > 0 :
                    coef[x, y+1] = 1
            elif np.imag( j ) !=0:
                if  x < N and x > 0 and y < N and y > 0 :
                    coef[x, y] += 1

                if  x-1 < N and x-1 > 0 and y < N and y > 0 :
                    coef[x-1, y] += 1
                if  x+1 < N and x+1 > 0 and y < N and y > 0 :
                    coef[x+1, y] += 1
                if  x < N and x > 0 and y -1< N and y-1> 0 :
                    coef[x, y-1] += 1
                if  x < N and x > 0 and y+1 < N and y+1 > 0 :
                    coef[x, y+1] += 1
            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    #filenameArr = f'K{it}_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####
    """
    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 7000 
    """
    ####

    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap)

    ####

    now =  str(datetime.now()).replace(" ", '_')
    now =  now.replace(":", '_')

    filenameImage = f'C_{dt}_{constt}N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}_{now}.png'
    
    plt.savefig(filenameImage, bbox_inches = 'tight', pad_inches=0.0 )

    ####

    #plt.show()
    plt.close()

def run_animation_pow ():
    for i in range(2, 17):

        run_increase_dot_f(i)

        print(i)

def run_animation_const ():
    dt = 0

    print('start')
    
    for i in np.linspace(-100, -10, 14):

        run_increase_dot_const(14, i, dt, 0)
        dt+=1

    for i in np.linspace(-10, 0, 20):

        run_increase_dot_const(14, i, dt, 1)
        dt+=1


if __name__ == '__main__':
  
    # a = [abs(np.random.beta(0.01, 0.01) - 0.5) for i in range(100_0)]
    # print(min(a), max(a))
        
    #run_increase_dot_const(23, 20000, 0,  0)


 
    


