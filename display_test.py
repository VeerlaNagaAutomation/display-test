import pytest
import psutil
import pyautogui

def test_screen_resolution():
    """Check if screen resolution is detected"""
    width, height = pyautogui.size()
    print(f"Screen resolution: {width}x{height}")
    assert width > 0 and height > 0, "Invalid screen resolution"

def test_cpu_usage():
    """Check that CPU usage is below 90%"""
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")
    assert cpu < 90, "High CPU usage detected"

def test_memory_usage():
    """Check that RAM usage is below 90%"""
    memory = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory}%")
    assert memory < 90, "Memory usage too high"
