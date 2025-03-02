import pytest
import time
from main import download_video

def test_download_speed():
    url = "https://www.youtube.com/watch?v=tPEE9ZwTmy0"

    start_time = time.time()
    download_video(url)
    end_time = time.time()

    execution_time = end_time - start_time
    assert execution_time < 10, f"Test failed: Download took too long ({execution_time:.2f} seconds)!"
