import numpy as np
from math import cos, sin

def create_rotation_mat_from_rpy(roll, pitch, yaw):
    Rx = np.array([
        1, 0, 0,
        0, cos(roll),  -sin(roll),
        0, sin(roll), cos(roll)]).reshape((3,3))
    Ry=np.array([
        cos(pitch), 0, sin(pitch),
        0 ,1, 0,
        -sin(pitch), 0, cos(pitch)]).reshape((3,3))
    Rz = np.array([
        cos(yaw), -sin(yaw), 0,
        sin(yaw), cos(yaw), 0,
        0, 0, 1]).reshape((3,3))
    R = Rz.dot(Ry.dot(Rx))
    return R

def points_to_homogeneous_coordinates(points, homogeneous_value=1):
    dim, num = points.shape
    return np.vstack((points, np.full((1, num), homogeneous_value)))

def normalize_homogeneous_coordinates(points):
    normalized_points = []
    if points.ndim == 2:
        normalized_points = points[:-1, :] / points[-1,:]
    elif points.ndim == 1:
        normalized_points = points[:-1] / points[-1]
    return normalized_points

def translation_to_skew_symetric_mat(translation):
    a1, a2, a3 = translation
    return np.array([[0, -a3, a2],[a3, 0, -a1],[-a2, a1, 0]])

def skew_symetric_mat_to_translation(skew_symetric_mat):
    return np.array([skew_symetric_mat[2,1], skew_symetric_mat[0,-1], skew_symetric_mat[1,0]])
