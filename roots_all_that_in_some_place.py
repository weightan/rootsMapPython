import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math
from tqdm import tqdm

power = 12
N = 3000
cmap = 'hot'

base = 3
scalF = 3

middle = (0, 1)
r = 0.05

#Z_99_N_3000_cmap_hot_p_12_arg1_0.8323852790856805_0.5541973900709793_arg2_0.9824290934640806_0.1869039226859017_arg3_1.0_0.01
arg1 = complex(0, 1) 
arg2 = complex(0.1, 1)
arg3 = complex(-0.4, -1)



def insideCircle(x, y):
    #return 1
    return math.dist((x, y), middle) < r

def insideRect(x, y):
    return x < middle[0] + r and x > middle[0] - r  and y < middle[1] + r and y > middle[1] - r  

def run(iteration):

    

    coef = np.zeros((N, N))
    
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


            if insideCircle(np.real( j ), np.imag( j )):
                #print(k)
                for q in rootsOfK:
                    #print('ok')
                    x = round(np.imag( q ) * N/4 + N/2)
                    y = round(np.real( q ) * N/4 + N/2)

                    if x < N and x > 0 and y < N and y > 0 and coef[x, y] < power:
                        #print('ok')
                        coef[x, y] += 1

                break

            
    
    #coef = np.rot90(coef)

    #filenameArr = f'coef_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####

    print('main done')

    for i in range(N):
        for j in range(N):
            if coef[i, j]:

                coef[i, j] += 700 
    ####

    plt.figure(num = None, figsize=(10, 10), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos')

    ####

    filenameImage = f'U_{iteration}_{r}_{middle}_N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight', pad_inches=0.0)

    ####

    plt.show()
    plt.close()


if __name__ == '__main__':
    r = 0.005
    print('start')

    run('test2')
    #print(p)


    