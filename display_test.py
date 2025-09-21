# display_test.py
import ctypes

def get_resolution():
    user32 = ctypes.windll.user32
    # Recommended for correct values on high-DPI displays
    try:
        user32.SetProcessDPIAware()
    except Exception:
        pass
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    return width, height

if __name__ == "__main__":
    w, h = get_resolution()
    print(f"Current screen resolution: {w}x{h}")
