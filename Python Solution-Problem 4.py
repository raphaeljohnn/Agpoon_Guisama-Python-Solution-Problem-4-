import matplotlib.pyplot as plt
import numpy as np

h_initial = int(input('Input initial height: '))
V = int(input('Input velocity: '))
theta = int(input('Input theta (angle) in degrees: '))
ax = int(input('Input horizontal acceleration (signed): '))
ay = int(input('Input vertical acceleration (signed): '))

if ay == 0:
    exit('Vertical acceleration cant be equal to zero.')

Viy = V*np.sin(theta*np.pi/180) # Y-component of velocity
Vix = V*np.cos(theta*np.pi/180) # X-component of velocity
time_pk = -Viy/ay # Time to peak height
totaly = h_initial + Viy*time_pk + 0.5*ay*(time_pk**2) # Total y traveled
tpk_gnd = np.sqrt(2*totaly/np.absolute(ay)) # Time from peak height to ground

time_flight = time_pk + tpk_gnd # Total time traveled
x_range = Vix*time_flight + 0.5*np.absolute(ax)*time_flight # Total range in x-axis
time = np.linspace(0, time_flight, num=999) # Time for x-axis and height computations.
y = h_initial + time*Viy + (time**2)*0.5*ay # y values

if Vix > 0 and ax >= 0:
    x = np.arange(0, x_range-(x_range/1000), x_range/1000)
elif Vix < 0 and ax < 0:
    x = np.arange(x_range+np.absolute(x_range)/1000, 0, np.absolute(x_range)/1000)
    y = np.fliplr(y)


plt.plot(x, y)
plt.title('Projectile Trajectory')
plt.xlabel('Horizontal displacement (m)')
plt.ylabel('Vertical displacement (m)')
plt.show()