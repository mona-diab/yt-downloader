import pytest
from main import download_video

def test_download_video():
    url = "https://www.youtube.com/watch?v=tPEE9ZwTmy0"
    resolution = download_video(url)
    
    assert resolution in ["720p", "1080p", "480p"], "Test failed: Resolution is not valid!"
