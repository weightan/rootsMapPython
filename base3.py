import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

power = 12
N = 3000
cmap = 'hot'

base = 3




def run():
    arg1 = complex(1, 1)
    arg2 = complex(1, 0)
    arg3 = complex(-1, 0)

    coef = np.zeros((N, N))
    
    for  i in range(base**power):

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
            x = round(np.imag( j ) * N/4.8 + N/2)
            y = round(np.real( j ) * N/4.8 + N/2)

            if x < N and x > 0 and y < N and y > 0 and coef[x, y] < power:
                coef[x, y] += 1

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    filenameArr = f'coef_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    np.save(filenameArr, coef)

    ####

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 700 
    ####

    plt.figure(num = None, figsize=(10, 10), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos' )

    ####

    filenameImage = f'N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight')

    ####

    plt.show()
    plt.close()


        






if __name__ == '__main__':
    run()
