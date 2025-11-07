import pytest
import os
import time
import subprocess
import psutil

# ✅ Put your video file path in quotes
VIDEO_PATH = r"C:\Users\nveerlax\Documents\WIN_20251107_22_20_49_Pro.mp4"

@pytest.mark.video
def test_play_video():
    """Play a video file locally to validate playback"""
    # ✅ Check that file exists
    assert os.path.exists(VIDEO_PATH), f"Video not found: {VIDEO_PATH}"

    print(f"Playing video: {VIDEO_PATH}")

    # ✅ Start video playback using default media player
    subprocess.Popen(["start", VIDEO_PATH], shell=True)

    time.sleep(5)

    # ✅ Check if a media player process is running
    player_running = any(
        "vlc" in p.name().lower() or "wmplayer" in p.name().lower()
        for p in psutil.process_iter()
    )

    assert player_running, "Video player did not start successfully"
    print("Video playback started successfully ✅")

    # ✅ Optional: wait 10 seconds then close it
    time.sleep(10)
    os.system("taskkill /IM vlc.exe /F >nul 2>&1")
    os.system("taskkill /IM wmplayer.exe /F >nul 2>&1")
