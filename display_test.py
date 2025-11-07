import pytest
import platform
import psutil

def test_system_info():
    """Check basic system details"""
    os_name = platform.system()
    os_version = platform.version()
    print(f"System: {os_name}, Version: {os_version}")
    assert os_name != "", "OS name missing"

def test_cpu_usage():
    """Ensure CPU usage is below 95%"""
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {usage}%")
    assert usage < 95, "CPU overloaded"

def test_memory():
    """Check RAM usage"""
    mem = psutil.virtual_memory()
    print(f"Memory Used: {mem.percent}%")
    assert mem.percent < 95, "Memory too high!"
