import numpy as np
import matplotlib.pyplot as plt

from multiple_view_geometry.scene import Scene
from multiple_view_geometry.cube import Cube
from multiple_view_geometry.camera import Camera
from multiple_view_geometry.camera_image_renderer import CameraImageRenderer
from multiple_view_geometry.homogeneous_matrix import HomogeneousMatrix
from multiple_view_geometry.transform_utils import create_rotation_mat_from_rpy

if __name__ == "__main__":
    camera0_extrinsic = HomogeneousMatrix.create(
        [1.7, 0.0, 0.5], create_rotation_mat_from_rpy(-np.pi / 2, 0, -np.pi / 4)
    )
    camera0 = Camera("0", camera0_extrinsic)
    camera1_extrinsic = HomogeneousMatrix.create([2.3, 0.0, 0.5], create_rotation_mat_from_rpy(-np.pi / 2, 0.0, 0))
    camera1 = Camera("1", camera1_extrinsic)

    cube = Cube((2, 3, 0), (2, 2, 2), resolution=1)
    renderer = CameraImageRenderer({camera0: "red", camera1: "blue"}, show_image_frame=True, show_epipolar_lines=True)
    scene = Scene(cube, [camera0, camera1], renderer)
    scene.project(True)
    plt.waitforbuttonpress(-1)
