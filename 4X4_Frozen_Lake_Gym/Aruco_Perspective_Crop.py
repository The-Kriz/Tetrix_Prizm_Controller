import numpy as np
import cv2, PIL
from cv2 import aruco
import pandas as pd
import math


def Distance(P1,P2):
    distance = np.sqrt(((P1[0] - P2[0]) ** 2) + ((P1[1] - P2[1]) ** 2))
    return distance


def MaxDistance(A, B, C, D):
    width_AB = Distance(A, B)
    width_CD = Distance(C, D)
    maxDistance = max(int(width_AB), int(width_CD))
    return maxDistance


def Perspective_wrap_crop(pt_A, pt_B, pt_C, pt_D, img):
    maxWidth = MaxDistance(pt_A, pt_D, pt_B, pt_C)
    maxHeight = MaxDistance(pt_A, pt_B, pt_C, pt_D)
    input_pts = np.float32([pt_A, pt_B, pt_C, pt_D])
    output_pts = np.float32([[0, 0],
                             [0, maxHeight - 1],
                             [maxWidth - 1, maxHeight - 1],
                             [maxWidth - 1, 0]])
    M = cv2.getPerspectiveTransform(input_pts, output_pts)
    output_img = cv2.warpPerspective(img, M, (maxWidth, maxHeight), flags=cv2.INTER_LINEAR)
    return output_img


def Coordinates(coordinates_sorted, image, location):
    arr1 = coordinates_sorted[0]
    point_0_0 = arr1[location[0]]
    point_1_0 = arr1[location[1]]
    point_2_0 = arr1[location[2]]
    point_3_0 = arr1[location[3]]
    arr1 = coordinates_sorted[1]
    point_0_1 = arr1[location[0]]
    point_1_1 = arr1[location[1]]
    point_2_1 = arr1[location[2]]
    point_3_1 = arr1[location[3]]
    arr1 = coordinates_sorted[2]
    point_0_2 = arr1[location[0]]
    point_1_2 = arr1[location[1]]
    point_2_2 = arr1[location[2]]
    point_3_2 = arr1[location[3]]
    arr1 = coordinates_sorted[3]
    point_0_3 = arr1[location[0]]
    point_1_3 = arr1[location[1]]
    point_2_3 = arr1[location[2]]
    point_3_3 = arr1[location[3]]
    return Perspective_wrap_crop(point_0_3, point_3_0, point_2_1, point_1_2, image)
    # return Perspective_wrap_crop(     BL  ,    TL   ,   TR    ,   BR    , image)


def DetectAruco(Image, cornerReturn=False, imageReturn=False):
    grayImage = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create
    corners, ids, rejectedImgPoints = aruco.drawDetectedMarkers(grayImage, aruco_dict, parameters=parameters)
    markedImage = aruco.drawDetectedMarkers(Image.copy(), corners, ids)

    if cornerReturn and imageReturn:
        return ids, corners, markedImage
    elif cornerReturn:
        return ids, corners
    elif imageReturn:
        return ids, markedImage
    else:
        return ids


def ArucoCropImage(Image):
    croppedImage = None
    ids, corners = DetectAruco(Image, cornerReturn=True)
    if ids is not None:
        int_corners = np.int0(corners)
        pos = []
        for i in range(len(ids)):
            pos.append(i)
        if len(ids) == 4:
            sortedCoordinates = []
            for j in range(4):
                arrEachPoint = []
                for X_id in range(len(ids)):
                    arrays = int_corners[X_id]
                    arrEachPoint.append(arrays[0][j])
                sortedCoordinates.append(arrEachPoint)
            croppedImage = Coordinates(sortedCoordinates, Image, pos)
    return croppedImage

