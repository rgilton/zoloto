"""
This example required `opencv-contrib-python` rather than `opencv-contrib-python-headless`
"""

from chrono import Timer
from cv2 import imshow, waitKey
from cv2.aruco import DICT_6X6_50

from yuri.cameras.camera import Camera


class TestCamera(Camera):
    pass


camera = TestCamera(0, marker_dict=DICT_6X6_50)

while True:
    with Timer() as capture_timer:
        frame = camera.capture_frame()
    with Timer() as annotate_timer:
        camera._annotate_frame(frame)
    imshow("demo", frame)
    waitKey(1)
    print(  # noqa: T001
        round(capture_timer.elapsed * 1000),
        round(annotate_timer.elapsed * 1000),
        end="\r",
    )