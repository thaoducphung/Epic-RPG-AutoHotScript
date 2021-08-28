import win32gui
import re
import pyautogui

# Reference
# https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        # print(re.match(wildcard, str(win32gui.GetWindowText(hwnd))))
        # print(win32gui.GetWindowText(hwnd))
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


# w = WindowMgr()
# w.find_window_wildcard(".*Discord.*")
# w.set_foreground()

# if __name__ == '__main__':
#     w = WindowMgr()
#     w.find_window_wildcard(".*Discord.*")
#     w.set_foreground()

#     import pyautogui
#     result = 1
#     pyautogui.press('Enter')
#     pyautogui.write(str(result))
#     pyautogui.press('Enter')

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def findDiscordWindow():
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "discord" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            print(i[0])
            win32gui.SetForegroundWindow(i[0])
            break

def raise_window(my_window):

    import win32con
    import win32gui

    def get_window_handle(partial_window_name):

        # https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

        def window_enumeration_handler(hwnd, windows):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        windows = []
        win32gui.EnumWindows(window_enumeration_handler, windows)

        for i in windows:
            if partial_window_name.lower() in i[1].lower():
                return i
                break

        print('window not found!')
        return None

    # https://stackoverflow.com/questions/6312627/windows-7-how-to-bring-a-window-to-the-front-no-matter-what-other-window-has-fo

    def bring_window_to_foreground(HWND):
        win32gui.ShowWindow(HWND, win32con.SW_RESTORE)
        win32gui.SetWindowPos(HWND, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(HWND, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)

    hwnd = get_window_handle(my_window)

    if hwnd is not None:
        bring_window_to_foreground(hwnd[0])
        return hwnd




if __name__ == "__main__":

    findDiscordWindow()
    # from win32gui import GetWindowText, GetForegroundWindow
    # import time 
    # print(GetWindowText(GetForegroundWindow()))
    # name_current_window = GetWindowText(GetForegroundWindow())

    test_window = raise_window('Discord')
    win32gui.SetForegroundWindow(test_window[0])
    print('test_window',test_window)
    print(type(test_window))
    pyautogui.press('Enter') # Enter all the current text then type result2

    pyautogui.write('Bảo một lằn') # prints out result instantly
    pyautogui.press('Enter') # Enter the result

    # print(GetWindowText(GetForegroundWindow()))
    # name_discord_window = GetWindowText(GetForegroundWindow())

    # time.sleep(1)

    # raise_window(name_current_window)
    # print(GetWindowText(GetForegroundWindow()))

