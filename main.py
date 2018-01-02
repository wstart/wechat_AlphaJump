# coding: utf-8
import os
import math
import random
import time
from PIL import Image, ImageDraw


def getDst(im):
    global last_x
    global last_y
    width = im.size[0]
    height = im.size[1]
    pix = im.load()

    mov_top_x = 1920
    mov_top_y = 1920

    mov_bottom_x = 0
    mov_bottom_y = 0  ## lowest


    maxload_x2 = -1
    baseconfolr = pix[0, 0]
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = pix[x, y]
            ## clear bg
            if (r in range(240, 256) and g in range(240, 256) and b in range(240, 256)):
                pix[x, y] = (0, 255, 0)
            ## clear bg
            elif (r in range(baseconfolr[0] - 50, baseconfolr[0] + 50) and g in range(baseconfolr[1] - 50, baseconfolr[
                1] + 50) and b in range(baseconfolr[2] - 50, baseconfolr[2] + 50)):
                pix[x, y] = (255, 255, 255)
            ## find movtarget
            elif (r in range(40, 61) and g in range(40, 61) and b in range(80, 103)):
                pix[x, y] = (0, 0, 0)
                if ( y > mov_bottom_y):
                    mov_bottom_x = x
                    mov_bottom_y = y
                if (y < mov_top_y):
                    mov_top_y = y
                    mov_top_x = x




    target_top_x = -1
    target_top_y = 0
    target_bottom_x = 0
    target_bottom_y = 0


    for y in range(int(height * 0.3), mov_bottom_y):
        is_newblank = True
        for x in range(0, width):
            r, g, b = pix[x, y]
            if (r > 250 and g > 250 and b > 250):
                is_newblank = True
            else:
                is_newblank = False
                break
        if is_newblank:
            target_top_y = y
            break

    baserang = range(0, int(width / 2))
    if mov_top_x <= width / 2:
        baserang = range(int(width / 2), width)

    while (target_top_x == -1):
        for x in baserang:
            r, g, b = pix[x, target_top_y]
            if (r < 240 or g < 240 or b < 240):
                target_top_x = x
                break

        target_top_y = target_top_y+1

    for y in range(target_top_y, height):
        r, g, b = pix[target_top_x, y]
        if (r > 240 and g > 240 and b > 240):
            target_bottom_x = target_top_x
            target_bottom_y = y
            break

    target_x = target_top_x
    target_y = target_top_y + int((mov_bottom_y - mov_top_y) * (2 + random.random() * 0.5) / 5)

    #distinc = (maxload_x - target_x) * (maxload_x - target_x) + (maxload_y - target_y) * (maxload_y - target_y)
    distinc = (mov_bottom_x - target_x) * (mov_bottom_x - target_x)
    distinc = math.sqrt(distinc)

    #clolor top
    for x in range(0, width):
        pix[x, mov_top_y] = (0, 255, 0)

    # clolor bottom
    for x in range(0, width):
        pix[x, mov_bottom_y] = (0, 0, 0)

    # clolor target_top
    for x in range(0, width):
        pix[x, target_top_y] = (0, 0, 0)

    # clolor target
    for j in range(target_x - 3, target_x + 3):
        for i in range(target_y - 3, target_y + 3):
            pix[j, i] = (0, 0, 255)

    pix[target_x, target_y] = (60, 60, 100)

    return distinc


def start():
    img_i = 0
    while True:
        print('start!')
        os.system('adb shell screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png ./screenshot.png')
        im = Image.open('./screenshot.png').convert('RGB')
        im.save('./record/imageNor_' + str(img_i) + '.jpg')
        im = im.transpose(Image.ROTATE_90)
        distance = getDst(im)
        im.save('./record/image_' + str(img_i) + '.jpg')
        print("D:"+str(distance))
        press_time = distance * 780 / 480
        press_time = int(press_time)
        print("T:" + str(press_time))
        if press_time < 200:
            press_time = 200
        img_i = img_i + 1
        cmd = 'adb shell input swipe 0 0 0 0 '+str(press_time)
        os.system(cmd)
        time.sleep(1.5)

if __name__ == '__main__':
    start()
