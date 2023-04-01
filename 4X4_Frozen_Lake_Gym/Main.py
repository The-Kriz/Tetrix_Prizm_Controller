from Aruco_Perspective_Crop import *
from path import *
from Tetrix_Motion import *

## no HC05 part

# image = cv2.imread('aruco6.jpg')
# # cv2.imshow("Orginal image",image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# cropped_image = ArucoCropImage(image)
# # cv2.imshow('Cropped Image', cropped_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# ids = DetectAruco(cropped_image)
# val = SplitImage(cropped_image)
# grid = ArucoIdToGrid(val)
#
grid = ["HHHH", "FHHH", "FHHS", "GFFF"]
print(grid)
env, qtable = gymActivation(grid)
sequence = seq(env, qtable)
path = PathText(sequence)

movement = motionPlan(path)
print(movement)
bot_movements_str = ''.join(movement)
print(bot_movements_str.encode())



#
# image = cv2.imread('aruco6.jpg')
# # cv2.imshow("Orginal image",image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# cropped_image = ArucoCropImage(image)
# # cv2.imshow('Cropped Image', cropped_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
# ids = DetectAruco(cropped_image)
# val = SplitImage(cropped_image)
# grid = ArucoIdToGrid(val)
# print(grid)
#
# env, qtable = gymActivation(grid)
# sequence = seq(env, qtable)
# path = PathText(sequence)
#
# movement = motionPlan(path)
# print(movement)
#
# btModule = btConnect()
# sendMovement(movement, btModule)
