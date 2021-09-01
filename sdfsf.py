import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

power = 12
N = 3000
cmap = 'hot'

base = 3
scalF = 3

middle = (-1, 0)
r = 0.15
#Z_99_N_3000_cmap_hot_p_12_arg1_0.8323852790856805_0.5541973900709793_arg2_0.9824290934640806_0.1869039226859017_arg3_1.0_0.01
arg1 = complex(0.8323852790856805, 0.5541973900709793) 
arg2 = complex(0.9824290934640806, 0.1869039226859017)
arg3 = complex(1, 0.01)



def insideCircle(x, y):
    return math.dist((x, y), middle) < 0.15

def insideRect(x, y):
    return x < middle[0] + r and x > middle[0] - r  and y < middle[1] + r and y > middle[1] - r  

def run(iteration):

    

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

            #if insideRect(np.real( j ), np.imag( j )):

            y = round(  np.imag( j )*N*3      + N/2)

            x = round(  (np.real( j )  + 1)*N*3    + N/2)

            if  x > 0 and x < N and y > 0 and y < N and coef[y, x] < 20:
            #if  coef[y, x] < 20:
                coef[y, x] += 1

            
    
    #coef = np.rot90(coef)

    #filenameArr = f'coef_N_{N}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}'
    #np.save(filenameArr, coef)

    ####

    for i in range(N):
        for j in range(N):
            if coef[i, j]:
                coef[i, j] += 700 
    ####

    plt.figure(num = None, figsize=(10, 10), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos')

    ####

    filenameImage = f'Z_{iteration}_N_{N}_cmap_{cmap}_p_{power}_arg1_{arg1.real}_{arg1.imag}_arg2_{arg2.real}_{arg2.imag}_arg3_{arg3.real}_{arg3.imag}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight', pad_inches=0.0)

    ####

    #plt.show()
    plt.close()




if __name__ == '__main__':
    print('start')

    for p in range(100, 500):

        run(p)

        arg1 *= complex(1, -0.002)/abs(complex(1, 0.002))
        arg2 *= complex(1, 0.002)/abs(complex(1, 0.002))

        print(p)


    