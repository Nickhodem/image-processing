from math import hypot, pi, cos, sin
import Image
from progress.bar import Bar

def hough(im, ntx=460, mry=360):


    pim = im.load()
    nimx, mimy = im.size
    mry = int(mry/2)*2
    him = Image.new("L", (ntx, mry), 255)
    phim = him.load()

    rmax = hypot(nimx, mimy)
    dr = rmax / (mry/2)
    dth = pi / ntx
    bar = Bar('Processing', max=nimx)
    for jx in xrange(nimx):
        for iy in xrange(mimy):
            col = pim[jx, iy]
            if col == 255: continue
            for jtx in xrange(ntx):
                th = dth * jtx
                r = jx*cos(th) + iy*sin(th)
                iry = mry/2 + int(r/dr+0.5)
                try:
                    phim[jtx, iry] -= 1
                except:
                    print 'error'
        bar.next()
    del bar
    return him


im = Image.open("laska.jpg").convert("L")
him = hough(im)
him.save("laskhough.bmp")
him.show(title="Log Hough transformation")

