import os
import sys

def enable_windows_ansi():
    if os.name != "nt":
        return
      
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32

        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
      
        mode = ctypes.c_uint()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))

        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING

        kernel32.SetConsoleMode(handle, new_mode)

    except Exception:
        pass