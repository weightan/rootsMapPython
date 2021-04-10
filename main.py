import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

power = 18
N = 3000
cmap = 'magma'



def run():

    coef = np.zeros((N, N))
    for h in range(5, power+1):
        for  i in range(2**h):

            k = bin(i)[2:]
            k = k.zfill(power)
            k = k.replace('0', '3')
            k = np.polynomial.Polynomial([int(k[i])  - 2 for i in range(len(k))])
            rootsOfK = k.roots()

            for j in rootsOfK:
                x = np.real( j ) * N/3 + N/2
                y = np.imag( j ) * N/3 + N/2
                if round(x)<N and round(x) > 0 and round(y) < N and round(y) > 0 and coef[round(x)][round(y)] < power:
                    coef[round(x)][round(y)] += 1

            #print(rootsOfK)
    
    coef = np.rot90(coef)
    np.save('coef_' +  str(N) + '_' + str(power) , coef)

    '''
    for i in range(N):
        for j in range(N):
            if coef[i][j] < 2:
                coef[i][j] = 0
    '''


    plt.figure(num = None, figsize=(6, 6), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap)

    #plot = plt.imshow(coef, cmap = cmap, norm=colors.LogNorm(vmin=1, vmax=255))
    plt.savefig(str(N) + 'A' + str(i) + '_' + cmap + str(N) + '.png', bbox_inches = 'tight')

    plt.show()
    plt.close()


        






if __name__ == '__main__':
    run()