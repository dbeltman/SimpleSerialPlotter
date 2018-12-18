import serial, gc
import matplotlib.pyplot as plt
from drawnow import *
arduinodata = serial.Serial('COM4', 115200)

distances=[]
def makeFig():
    plt.ylim(0,200)
    plt.xlim(0, 50)
    plt.plot(distances)

# last_three=[]

while True:

    while (arduinodata.inWaiting()==0):

        # pass

        distance = float(arduinodata.readline())
        if distance < 500:
            distances.append(distance)
            # last_three.append(distance)
        if (len(distances)>50):
            templist=distances[49:len(distances)]
            distances=templist
            gc.collect()
        print(distance)
        drawnow(makeFig)
