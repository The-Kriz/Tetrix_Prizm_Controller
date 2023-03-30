import serial
from time import sleep

'''
Forward   = 1
Left      = 2
Right     = 3
Backward  = 4
'''


def motionPlan(path):
    i = 0
    bot_movements = []
    if path[i] == "Left":
        bot_movements.append("2")
    elif path[i] == "Right":
        bot_movements.append("3")

    while True:
        bot_movements.append("1")
        i += 1
        if i >= len(path):
            if path[i-1] == "Left":
                bot_movements.append("3")
            elif path[i-1] == "Right":
                bot_movements.append("2")
            break
        if path[i-1] != path[i] or i < len(path):
            if path[i-1] == "Left" and path[i] == "Forward":
                bot_movements.append("3")
            elif path[i-1] == "Left" and path[i] == "Right":
                bot_movements.append("3")
                bot_movements.append("3")
            elif path[i-1] == "Right" and path[i] == "Forward":
                bot_movements.append("2")
            elif path[i-1] == "Right" and path[i] == "Left":
                bot_movements.append("2")
                bot_movements.append("2")
            elif path[i-1] == "Forward" and path[i] == "Right":
                bot_movements.append("3")
            elif path[i-1] == "Forward" and path[i] == "Left":
                bot_movements.append("2")
    return bot_movements


def sendMovement(bot_path, btModule):
    bot_movements_str = ''.join(bot_path)
    btModule.write(bot_movements_str.encode())


def turnOfTetrix(btModule):
    stop = 9
    btModule.write(stop.encode())


def btConnect():
    btModule = serial.Serial('/dev/tty.HC-05-DevB', 9600)
    sleep(3)
    return btModule


def btDisconnect(btModule):
    btModule.close()




# path = ["Left","Left","Forward","Forward","Forward","Left"]
# movement = motionPlan(path)
# print(movement)
# bot_movements_str = ''.join(movement)
# print(bot_movements_str.encode())