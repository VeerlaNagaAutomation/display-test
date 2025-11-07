import pytest
import os
import time
import subprocess
import psutil

VIDEO_PATH = r"C:\Videos\sample.mp4"  # Change this to your video file path

@pytest.mark.video
def test_play_video():
    """Play a video file locally to validate media playback"""
    assert os.path.exists(C:\Documents\WIN_20251107_22_20_49_Pro.mp4), f"Video not found: {C:\Documents\WIN_20251107_22_20_49_Pro.mp4}"

    print(f"Playing video: {C:\Documents\WIN_20251107_22_20_49_Pro.mp4}")
    
    # Open video file using system default player (Windows)
    proc = subprocess.Popen(["start", C:\Documents\WIN_20251107_22_20_49_Pro.mp4], shell=True)
    
    # Give time for the player to open
    time.sleep(5)
    
    # Check if a video player process is running
    player_running = any("vlc" in p.name().lower() or "wmplayer" in p.name().lower() for p in psutil.process_iter())
    
    assert player_running, "Video player did not start successfully"
    
    print("Video playback started successfully ✅")

    # (Optional) close the player after 10 seconds
    time.sleep(10)
    os.system("taskkill /IM vlc.exe /F")
    os.system("taskkill /IM wmplayer.exe /F")
