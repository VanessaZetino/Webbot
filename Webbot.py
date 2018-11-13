    """
    
    All coordinates assume a screen resolution of 1280x1024, and Chrome
    maximized with the Bookmarks Toolbar enabled.
    Down key has been hit 4 times to center play area in browser.
    x_pad = 190
    y_pad = 151
    Play area =&nbsp; x_pad+1, y_pad+1, 830, 631
    """

    from PIL import ImageGrab
    import PIL
    from PIL import Image
    import os
    import time
    import win32api, win32con
    from PIL import ImageOps
    from numpy import *
    
    x_pad = 190
    y_pad = 151


    def screenGrab():
        box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)


    im = ImageGrab.grab(box)

    ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


    def grab():
        box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print('a')
    return a


    def startGame():


    # location of first menu
    mousePos((319, 196))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((302, 389))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((598, 441))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((338, 371))
    leftClick()
    time.sleep(.1)


    def leftClick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click.")


    def leftDown():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


    time.sleep(.1)
    print('left Down')


    def leftUp():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    time.sleep(.1)
    print('left release')


    def mousePos(cord):
        win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


    def get_cords():
        x, y = win32api.GetCursorPos()


    x = x - x_pad
    y = y - y_pad
    print(x, y)

    """
    
    Plate cords:
    
    76, 204
    186, 201
    277, 205
    394, 209
    493, 204
    591, 206
    """


    class Cord:
        f_shrimp = (39, 333)


    f_rice = (96, 330)
    f_nori = (36, 387)
    f_roe = (91, 384)
    f_salmon = (30, 438)
    f_unagi = (92, 439)
    # -----------------------------------

    phone = (614, 338)
    menu_toppings = (577, 266)
    t_shrimp = (506, 219)
    t_nori = (505, 273)
    t_roe = (589, 272)
    t_salmon = (503, 338)
    t_unagi = (585, 217)
    t_exit = (555, 329)
    t_exit_rice = (510, 332)
    menu_rice = (549, 291)
    buy_rice = (562, 283)
    delivery_norm = (500, 295)


    def clear_tables():
        mousePos((103, 208))


    leftClick()

    mousePos((211, 206))
    leftClick()

    mousePos((293, 202))
    leftClick()

    mousePos((410, 197))
    leftClick()

    mousePos((497, 210))
    leftClick()

    mousePos((595, 210))
    leftClick()
    time.sleep(1)


    def foldMat():
        mousePos((Cord.f_rice[0] + 40, Cord.f_rice[1]))


    leftClick()
    time.sleep(.1)

    '''
    Recipes:
    
    onigiri
    2 rice, 1 nori
    
    caliroll:
    1 rice, 1 nori, 1 roe
    
    gunkan:
    1 rice, 1 nori, 2 roe
    '''


    def makeFood(food):
        if food == 'caliroll':
            print('Making a caliroll')


    foodOnHand['rice'] -= 1
    foodOnHand['nori'] -= 1
    foodOnHand['roe'] -= 1
    mousePos(Cord.f_rice)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_nori)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_roe)
    leftClick()
    time.sleep(.1)
    foldMat()
    time.sleep(1.5)

    elif food == 'onigiri':
    print('Making a onigiri')
    foodOnHand['rice'] -= 2
    foodOnHand['nori'] -= 1
    mousePos(Cord.f_rice)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_rice)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_nori)
    leftClick()
    time.sleep(.1)
    foldMat()
    time.sleep(.05)
    time.sleep(1.5)

    elif food == 'gunkan':
    print('Making a gunkan')
    foodOnHand['rice'] -= 1
    foodOnHand['nori'] -= 1
    foodOnHand['roe'] -= 2
    mousePos(Cord.f_rice)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_nori)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_roe)
    leftClick()
    time.sleep(.05)
    mousePos(Cord.f_roe)
    leftClick()
    time.sleep(.1)
    foldMat()
    time.sleep(1.5)


    def checkFood():
        for i, j in foodOnHand.items():
            if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 4:
            print('%s is low and needs to be replenished' % i)


    buyFood(i)


    def buyFood(food):
        if food == 'rice':
            global s


    mousePos(Cord.phone)
    time.sleep(.1)
    leftClick()
    mousePos(Cord.menu_rice)
    time.sleep(.5)
    leftClick()
    s = screenGrab()
    if s.getpixel(Cord.buy_rice) != (127, 127, 127):
        print('rice is available')
    mousePos(Cord.buy_rice)
    time.sleep(.5)
    leftClick()
    mousePos(Cord.delivery_norm)
    time.sleep(.1)
    leftClick()
    time.sleep(.5)
    else:
    print('rice is NOT available')
    mousePos(Cord.t_exit_rice)
    leftClick()
    time.sleep(.1)
    buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
    time.sleep(.1)
    leftClick()
    mousePos(Cord.menu_toppings)
    time.sleep(.1)
    leftClick()
    s = screenGrab()
    print('test')
    time.sleep(.1)
    if s.getpixel(Cord.t_nori) != (33, 30, 11):
        print('nori is available')
    mousePos(Cord.t_nori)
    time.sleep(.5)
    leftClick()
    mousePos(Cord.delivery_norm)
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    else:
    print('nori is NOT available')
    mousePos(Cord.t_exit)
    leftClick()
    time.sleep(1)
    buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
    time.sleep(.1)
    leftClick()
    mousePos(Cord.menu_toppings)
    time.sleep(.1)
    leftClick()
    s = screenGrab()
    time.sleep(.1)
    if s.getpixel(Cord.t_roe) != (127, 61, 0):
        print('roe is available')
    mousePos(Cord.t_roe)
    time.sleep(.1)
    leftClick()
    mousePos(Cord.delivery_norm)
    time.sleep(.1)
    leftClick()
    time.sleep(.1)
    else:
    print('roe is NOT available')
    mousePos(Cord.t_exit)
    leftClick()
    time.sleep(1)
    buyFood(food)

    foodOnHand = {'shrimp': 5,
                  'rice': 10,
                  'nori': 10,
                  'roe': 10,
                  'salmon': 5,
                  'unagi': 5}


    def get_seat_one():
        box = (218, 211, 218 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_seat_two():
        box = (319, 211, 319 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_seat_three():
        box = (420, 211, 420 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_seat_four():
        box = (521, 211, 521 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_seat_five():
        box = (622, 211, 622 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_seat_six():
        box = (723, 211, 723 + 60, 211 + 16)


    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a


    def get_all_seats():
        get_seat_one()


    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

    sushiTypes = {1923: 'onigiri',
                  2567: 'caliroll',
                  1930: 'gunkan'}


    class Blank:
        seat_1 = 6540


    seat_2 = 5938
    seat_3 = 11305
    seat_4 = 10565
    seat_5 = 6912
    seat_6 = 8993


    def check_bubs():
        checkFood()


    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s1])
    makeFood(sushiTypes[s1])
    else:
    print('sushi not found!\n sushiType = %i' % s1)

    else:
    print('Table 1 unoccupied')
    clear_tables()
    checkFood()

    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs %s' % sushiTypes[s2])
    makeFood(sushiTypes[s2])
    else:
    print('sushi not found!\n sushiType = %i' % s2)

    else:
    print('Table 2 unoccupied')
    checkFood()

    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs %s' % sushiTypes[s3])
    makeFood(sushiTypes[s3])
    else:
    print('sushi not found!\n sushiType = %i' % s3)

    else:
    print('Table 3 unoccupied')
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs %s' % sushiTypes[s4])
    makeFood(sushiTypes[s4])
    else:
    print('sushi not found!\n sushisushuType = %i' % s4)

    else:
    print('Table 4 unoccupied')
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs %s' % sushiTypes[s5])
    makeFood(sushiTypes[s5])
    else:
    print('sushi not found!\n sushiType = %i' % s5)
    else:
    print('Table 5 unoccupied')
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 1 is occupied and needs %s' % sushiTypes[s6])
    makeFood(sushiTypes[s6])
    else:
    print('sushi not found!\n sushiType = %i' % s6)

    else:
    print('Table 6 unoccupied')

    clear_tables()


    def main():
        startGame()


    while True:
        check_bubs()

    if __name__ == '__main__':
        main()