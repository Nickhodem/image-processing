'''
Toolbox narzedzia umozliwiaja transformacje obrazu pomagajaca w pracy sieciom neuronowym
'''
import os
import skimage
import skimage.io as io
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import numpy as np

from progress.bar import Bar

def show_images(images,titles=None):
    """Wyswietlanie zdjec
    zdjecia maja format  a=numpy.ndarray(shape=(480, 272, 3), dtype=numpy.uint8)
    okreslanie poszczegolnych pikseli odbywa sie przez referencje a[0][0]=[1,2,3]
    otwiera tez zdjecia ze scikit-image
    """
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n) # Make subplot
        if image.ndim == 2: # Is image grayscale?
            plt.gray() # Only place in this blog you can't replace 'gray' with 'grey'
        plt.imshow(image)
        a.set_title(title)
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()

def myrgb2grey(image):
    '''
    Skrypt umozliwia stworzenie nowego obrazu po transformacji wg wzoru zaproponowanego przez doktora Mikruta
    z parametrami:
    value=0.2989*R+0.5870*G+0.1140*B
    '''
    images=io.imread(image)
    maxWiersz=images.__len__()
    maxKolumn=images[1].__len__()
    images_grey=np.ndarray(shape=(maxWiersz, maxKolumn, 3), dtype=np.uint8)
    bar = Bar('Processing', max=maxWiersz)
    for i in range(0,maxWiersz):
        for j in range(0, maxKolumn):
            value=0.2989*images[i][j][0]+images[i][j][1]*0.5870+images[i][j][2]*0.1140
            images_grey[i][j]=value
        bar.next()
    del bar
    return images_grey
def binearyzuj(image):
    binary_image = np.where(image > np.mean(image),1.0,0.0)
    return binary_image



