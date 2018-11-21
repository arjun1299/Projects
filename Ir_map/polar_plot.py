import numpy as np
import matplotlib.pyplot as plt
import serial

#angle of servo sweep
N=180
#connect to serial port
scan = 0
r=[]
while scan<100:
        try:
            ser = serial.Serial('/dev/ttyACM'+str(scan),baudrate='9600')
            if ser.isOpen():
                print('Connected to'+'/dev/ttyACM'+str(scan))
                break
        except:
            print("access error")
            scan+=1

#taking multiple readings of the sensor
for i in range(N):
    s=ser.readline(100)
    print(i,float(s))
    r.append(float(s))

print(r)

#setting theta values
theta = [np.pi/180*i for i in range(1,(N)+1)] 
colors = r
#plotting the graph
fig = plt.figure()
ax = fig.add_subplot(111,projection='polar')
c = ax.plot(theta, r)

plt.show()
