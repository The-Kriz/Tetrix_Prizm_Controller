import numpy as np
import cv2
from cv2 import aruco


def Distance(P1, P2):
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
    return Perspective_wrap_crop(point_0_2, point_3_1, point_2_0, point_1_3, image)
    # return Perspective_wrap_crop(     BL  ,    TL   ,   TR    ,   BR    , image)


def DetectAruco(Image, cornerReturn=False, imageReturn=False):
    grayImage = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(grayImage, aruco_dict, parameters=parameters)
    if imageReturn:
        markedImage = aruco.drawDetectedMarkers(Image.copy(), corners, ids)
    # print(ids)
    if cornerReturn and imageReturn:
        return ids, corners, markedImage
    elif cornerReturn:
        return ids, corners
    elif imageReturn:
        return ids, markedImage
    else:
        return ids


def rearrangeAruco(ids, corners, CustomOrder=False):
    if CustomOrder:
        desiredOrder = CustomOrder
    else:
        desiredOrder = [0, 1, 2, 3]
    idsX = [np.where(ids == i)[0][0] for i in desiredOrder]
    idsReordered = ids[idsX]
    cornersReordered = corners[idsX]

    return idsReordered, cornersReordered


def ArucoCropImage(Image):
    croppedImage = None
    ids, corners = DetectAruco(Image, cornerReturn=True)

    if ids is not None:
        int_corners = np.int0(corners)
        reorderedIds, reorderedCorners = rearrangeAruco(ids, int_corners)

        pos = []
        for i in range(len(reorderedIds)):
            pos.append(i)
        if len(reorderedIds) == 4:
            sortedCoordinates = []
            for j in range(4):
                arrEachPoint = []
                for X_id in range(len(reorderedIds)):
                    arrays = reorderedCorners[X_id]
                    arrEachPoint.append(arrays[0][j])
                sortedCoordinates.append(arrEachPoint)
            croppedImage = Coordinates(sortedCoordinates, Image, pos)
    return croppedImage


def SplitImage(image):
    height, width, _ = image.shape
    cell_size = int(min(height, width) / 4)
    cellArucoID = []
    for i in range(4):
        for j in range(4):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cell = image[y1:y2, x1:x2]
            arucoIdNo = DetectAruco(cell)
            cellArucoID.append(arucoIdNo)
    return cellArucoID

def ArucoIdToGrid(idLocation):
    start = 4
    home = 5
    holeMarkerID = [16, 17, 18, 19]
    frozenFloorMarkerID = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    grid = []
    for i in range(4):
        row = ""
        for j in range(4):
            index = i * 4 + j
            if idLocation[index] == 4:
                row += "S"
            elif idLocation[index] in frozenFloorMarkerID:
                row += "F"
            elif idLocation[index] == 5:
                row += "G"
            elif idLocation[index] in holeMarkerID:
                row += "H"
        grid.append(row)
    return grid






#######################################################################################################################
# testing

# # Example usage
# arr = [5,7,8,9,10,17,11,18,12,13,14,19,20,15,16,6]
# layout = ArucoIdToMatrix(arr)
# print(layout)  # prints ["SFFF", "FHFH", "FFFH", "HFFG"]

# def Tester():
#     # Load image
#     image = cv2.imread('aruco2.jpg')
#     cv2.imshow("before", image)
#     cropped_image = ArucoCropImage(image)
#     cv2.imshow('Cropped Image', cropped_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# Tester()


# ids = DetectAruco(Image)
# idsReordered, cornersReordered = rearrangeAruco(ids)

#
# def Tester2():
#     # Load image
#     image = cv2.imread('aruco6.jpg')
#     # cv2.imshow("orginal image",image)
#     cropped_image = ArucoCropImage(image)
#     ids = DetectAruco(cropped_image)
#     val = SplitImage(cropped_image)
#     array = ArucoIdToMatrix(val)
#     print(array)
#     return array
#     # cv2.imshow('Cropped Image', cropped_image)
#     # cv2.waitKey(0)
#     cv2.destroyAllWindows()

