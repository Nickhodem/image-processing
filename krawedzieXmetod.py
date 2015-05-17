"""
Algorytm po kolei:  >wczytuje obraz, >zmienia go na szary > bineryzuje >
>transformacja log polar  > wykrywa krawedzi Cannym  > wyswietla wszystkei wynikowe obrazy
"""
from Narzedzia import *
import cv2
from progress.bar import Bar
filename='laska.jpg'
img=io.imread(filename)

progress = Bar('Progress', max=4)
#a=binearyzuj(filename)
#b=a.squeeze(axis=2)

"""zamiana na obraz z odcieniami szarosci """
grey_image=myrgb2grey(filename)
progress.next()
""" zamiana na obraz binarny"""
binary_image = np.where(grey_image > np.mean(grey_image),1.0,0.0)
progress.next()
#show_images([grey_image,binary_image],titles=['grey image', 'binary image'])

"""transformacja log polar"""
image_polar=cv2.logPolar(img, (img.shape[0]/2, img.shape[1]/2), 40, cv2.WARP_FILL_OUTLIERS)
progress.next()
"""
from skimage.transform import swirl
swirled = swirl(image, rotation=0, strength=10, radius=120, order=2)

show_images([image, swirled],titles=['logpolar opencv','scikit swirl'])
"""

"""detekcja krawedzi"""
wiersze=img.__len__()
kolumny=img[1].__len__()
edges = cv2.Canny(img,wiersze,kolumny)
progress.next()

show_images([grey_image,binary_image,image_polar, edges],titles=['grey image', 'binary image', 'transformacja log polar','krawedzie canny'])

