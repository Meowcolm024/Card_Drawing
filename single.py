import os


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


def main():
    tap(900, 900)
    swipe(700, 800, 1500, 300, 1000)


main()
