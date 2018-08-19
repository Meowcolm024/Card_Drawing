import cv2
import time
import random
import lib.ats
import numpy as np


def sr(sh):
    xSR = random.randrange(800, 1200)
    ySR = random.randrange(400, 800)

    imgSR = cv2.imread(sh, 0)
    templateSR = cv2.imread('res/SR.png', 0)

    resSR = cv2.matchTemplate(imgSR, templateSR, cv2.TM_CCOEFF_NORMED)
    thresholdSR = 0.30
    if (resSR >= thresholdSR).any():
        lib.ats.tap(xSR, ySR)


def ssr(sh):
    xSSR = random.randrange(800, 1200)
    ySSR = random.randrange(400, 800)

    imgSSR = cv2.imread(sh, 0)
    templateSSR = cv2.imread('res/SR.png', 0)

    resSSR = cv2.matchTemplate(imgSSR, templateSSR, cv2.TM_CCOEFF_NORMED)
    thresholdSSR = 0.30
    if (resSSR >= thresholdSSR).any():
        lib.ats.tap(xSSR, ySSR)


def end(sh):
    imgEND = cv2.imread(sh, 0)
    templateEND = cv2.imread('res/END.png', 0)

    resEND = cv2.matchTemplate(imgEND, templateEND, cv2.TM_CCOEFF_NORMED)
    thresholdEND = 0.40
    if (resEND >= thresholdEND).any():
        return 0
    else:
        return 1


def start(sh):
    imgSTART = cv2.imread(sh, 0)
    templateSTART = cv2.imread('res/START.png', 0)

    resSTART = cv2.matchTemplate(imgSTART, templateSTART, cv2.TM_CCOEFF_NORMED)
    thresholdSTART = 0.85
    pos = []

    if (resSTART >= thresholdSTART).any():
        loc = np.where(resSTART >= thresholdSTART)
        for pt in zip(*loc[::-1]):
            pos.append(pt)
        return pos
    else:
        return 0


def main():
    delay = random.randrange(1, 5)
    x1 = random.randrange(600, 800)
    y1 = random.randrange(600, 800)
    x2 = random.randrange(1300, 1500)
    y2 = random.randrange(200, 400)
    dly = random.randrange(500, 1000)

    sh = lib.ats.screenshot()
    pos = start(sh)

    if pos != 0:
        lib.ats.tap(pos[0][0], pos[0][1])
        lib.ats.swipe(x1, y1, x2, y2, dly)

        time.sleep(delay)

        while lib.ats.screenshot():
            gap = random.uniform(0.5, 1.5)
            time.sleep(gap)

            sh = lib.ats.screenshot()

            if end(sh) == 1:
                ssr(sh)
                sr(sh)
            elif end(sh) == 0:
                xEND = random.randrange(800, 1200)
                yEND = random.randrange(400, 800)
                lib.ats.tap(xEND, yEND)
                print("Finished")
                break
    else:
        print("Error")


main()
