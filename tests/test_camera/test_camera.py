import pytest

import zoloto.cameras
from zoloto.marker_type import MarkerType


@pytest.mark.parametrize(
    "camera_class", [zoloto.cameras.Camera, zoloto.cameras.camera.SnapshotCamera]
)
def test_enumerate_all_cameras(camera_class, mocker) -> None:
    class TestCamera(camera_class):
        marker_type = MarkerType.DICT_4X4_100

        def get_marker_size(self, marker_id):
            return 100

    VideoCapture = mocker.patch("zoloto.cameras.camera.VideoCapture")
    VideoCapture.return_value.isOpened.return_value = True
    discovered_cameras = list(TestCamera.discover())
    assert len(discovered_cameras) == 8
    for camera in discovered_cameras:
        assert isinstance(camera, TestCamera)


@pytest.mark.parametrize(
    "camera_class", [zoloto.cameras.Camera, zoloto.cameras.camera.SnapshotCamera]
)
def test_enumerate_no_cameras(camera_class, mocker) -> None:
    class TestCamera(camera_class):
        marker_type = MarkerType.DICT_4X4_100

        def get_marker_size(self, marker_id):
            return 100

    VideoCapture = mocker.patch("zoloto.cameras.camera.VideoCapture")
    VideoCapture.return_value.isOpened.return_value = False
    discovered_cameras = list(TestCamera.discover())
    assert len(discovered_cameras) == 0


def test_get_camera_ids(mocker) -> None:
    VideoCapture = mocker.patch("zoloto.cameras.camera.VideoCapture")
    VideoCapture.return_value.isOpened.return_value = True
    discovered_ids = list(zoloto.cameras.camera.find_camera_ids())
    assert discovered_ids == [0, 1, 2, 3, 4, 5, 6, 7]


def test_get_no_camera_ids(mocker) -> None:
    VideoCapture = mocker.patch("zoloto.cameras.camera.VideoCapture")
    VideoCapture.return_value.isOpened.return_value = False
    discovered_ids = list(zoloto.cameras.camera.find_camera_ids())
    assert len(discovered_ids) == 0
