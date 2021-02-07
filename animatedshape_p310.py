# this program "animates" line segments

# Import drawing library
import matplotlib.pyplot as plt
    
ax = plt.gca()
ax.cla()  # clear things for fresh plot

for x in range(5,12):  # sets counter
    circle1 = plt.Circle((x, x), 4, color='b')  # make the red face
    circle2 = plt.Circle((x-1.8, x+2), 0.4, color='r')  # left eye, blue
    circle3 = plt.Circle((x+1.8, x+2), 0.4, color='r')  # right eye, blue
    plt.title("animated face")  # put title on plot
    # change default range so that new circles will work
    ax.set_xlim((0, 20))
    ax.set_ylim((0, 20))
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    plt.plot([x-2,x+2], [x-2,x-2], "k")
    
plt.show()