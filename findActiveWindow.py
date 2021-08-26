import win32gui
import re

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
            win32gui.SetForegroundWindow(i[0])
            break

if __name__ == "__main__":
    findDiscordWindow()
    