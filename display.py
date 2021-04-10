import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def run():
    coef = np.load('coef_N_3000_p_18.npy')
    N = 3000
    cmap ='hot'

    print('done load')

    for i in range(N):
        for j in range(N):
            if coef[i][j]:
                coef[i][j] += 700 

    plt.figure(num = None, figsize=(10, 10), dpi=300)

    plt.axis('off')

    plot = plt.imshow(coef, cmap = cmap, interpolation='lanczos')

    #plot = plt.imshow(coef, cmap = cmap, norm=colors.LogNorm(vmin=1, vmax=255))
    plt.savefig( 'd' +  '_' + cmap + str(N) + '.png', bbox_inches = 'tight')

    plt.show()
    plt.close()



if __name__ == '__main__':
    run()
