import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

power = 18
N = 3000
cmap = 'hot'



def run():

    coef = np.zeros((N, N))
    
    for  i in range(2**power):

        k = bin(i)[2:]
        k = k.zfill(power)
        k = k.replace('0', '3')
        k = np.polynomial.Polynomial([int(k[i])  - 2 for i in range(len(k))])
        rootsOfK = k.roots()

        for j in rootsOfK:
            x = round(np.imag( j ) * N/3 + N/2)
            y = round(np.real( j ) * N/3 + N/2)

            if x < N and x > 0 and y < N and y > 0 and coef[x, y] < power:
                coef[x, y] += 1

            #print(rootsOfK)
    
    #coef = np.rot90(coef)

    filenameArr = f'coef_N_{N}_p_{power}'
    np.save(filenameArr, coef)

    ####

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 700 
    ####

    plt.figure(num = None, figsize=(6, 6), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos' )

    ####

    filenameImage = f'N_{N}_cmap_{cmap}_p_{power}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight')

    ####

    plt.show()
    plt.close()


        






if __name__ == '__main__':
    run()
