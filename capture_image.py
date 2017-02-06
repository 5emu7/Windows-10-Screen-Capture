import pyscreenshot as ImageGrab
import os
import time

class ScreenGrab:
    def __init__(self):
        self.name = "sample_{}.png".format(str(int(time.time())))

    def screenGrab(self):
        self.im = ImageGrab.grab()
        self.im.save(os.getcwd() + "\\"+self.name)


if __name__ =='__main__':
    m = ScreenGrab()
    print(m.name)
    m.screenGrab()
    
