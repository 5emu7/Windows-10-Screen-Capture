import pyscreenshot as ImageGrab
import os
import time
import multiprocessing
import sys
# Module multiprocessing is organized differently in Python 3.4+
#------------------------------------------------------------------#
#snipping for fix bug in pyinstaller multiprocessing#
try:
    # Python 3.4+
    if sys.platform.startswith('win'):
        import multiprocessing.popen_spawn_win32 as forking
    else:
        import multiprocessing.popen_fork as forking
except ImportError:
    import multiprocessing.forking as forking

if sys.platform.startswith('win'):
    # First define a modified version of Popen.
    class _Popen(forking.Popen):
        def __init__(self, *args, **kw):
            if hasattr(sys, 'frozen'):
                # We have to set original _MEIPASS2 value from sys._MEIPASS
                # to get --onefile mode working.
                os.putenv('_MEIPASS2', sys._MEIPASS)
            try:
                super(_Popen, self).__init__(*args, **kw)
            finally:
                if hasattr(sys, 'frozen'):
                    # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                    # available. In those cases we cannot delete the variable
                    # but only set it to the empty string. The bootloader
                    # can handle this case.
                    if hasattr(os, 'unsetenv'):
                        os.unsetenv('_MEIPASS2')
                    else:
                        os.putenv('_MEIPASS2', '')

    # Second override 'Popen' class with our modified version.
    forking.Popen = _Popen
#snipping for fix bug in pyinstaller multiprocessing#
#------------------------------------------------------------------#
class ScreenGrab:
    def __init__(self):
        self.name = "sample_{}.png".format(str(int(time.time())))
        self.directory_image = "image_capture"
    def directory(self):
        directory = self.directory_image
        if not os.path.exists(directory):
            os.makedirs(directory)

    def screenGrab(self):
        self.im = ImageGrab.grab()
        self.im.save(os.getcwd() +"\\"+self.directory_image+"\\"+self.name)
    

if __name__ == '__main__':
    multiprocessing.freeze_support()
    m = ScreenGrab()
    m.directory()
    print(m.name)
    m.screenGrab()

    
