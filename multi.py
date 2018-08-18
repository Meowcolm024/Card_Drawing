import os
import cv2
import time


def tap(x0, y0):
    cmdTap = 'adb shell input tap {x1} {y1}'.format(
        x1=x0,
        y1=y0
    )
    print(cmdTap)
    os.system(cmdTap)


def swipe(a0, b0, a1, b1, delay0):
    cmdSwipe = 'adb shell input swipe {a2} {b2} {a3} {b3} {delay1}'.format(
        a2=a0,
        b2=b0,
        a3=a1,
        b3=b1,
        delay1=delay0
    )
    print(cmdSwipe)
    os.system(cmdSwipe)


def sr(sh):
    imgSR = cv2.imread(sh, 0)
    templateSR = cv2.imread('SR.png', 0)

    resSR = cv2.matchTemplate(imgSR, templateSR, cv2.TM_CCOEFF_NORMED)
    thresholdSR = 0.30
    if (resSR >= thresholdSR).any():
        tap(1000, 600)


def ssr(sh):
    imgSSR = cv2.imread(sh, 0)
    templateSSR = cv2.imread('SR.png', 0)

    resSSR = cv2.matchTemplate(imgSSR, templateSSR, cv2.TM_CCOEFF_NORMED)
    thresholdSSR = 0.30
    if (resSSR >= thresholdSSR).any():
        tap(1000, 600)


def end(sh):
    imgEND = cv2.imread(sh, 0)
    templateEND = cv2.imread('END.png', 0)

    resEND = cv2.matchTemplate(imgEND, templateEND, cv2.TM_CCOEFF_NORMED)
    thresholdEND = 0.40
    if (resEND >= thresholdEND).any():
        return 'e'
    else:
        return 'c'


def screenshot():
    os.system('adb shell screencap -p /sdcard/sh.png')
    os.system('adb pull /sdcard/sh.png .')
    return "sh.png"


def main():
    tap(900, 900)
    swipe(700, 800, 1500, 250, 1000)
    time.sleep(5)

    while screenshot():
        time.sleep(1)
        sh = screenshot()
        if end(sh) == 'c':
            ssr(sh)
            sr(sh)
        elif end(sh) == 'e':
            tap(1000, 600)
            break


main()
