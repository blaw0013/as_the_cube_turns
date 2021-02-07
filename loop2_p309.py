# this program uses the counter variable in a "for" loop to draw line segments

# Import drawing library
import matplotlib.pyplot as plt

plt.title("Stepping Lines")  # put title on plot
for G in range(3,10):  # begins at G=3, and does the following commands until G=10, a total of 7 line segments
    plt.plot([G,G+3], [G,G+1], "b")  # Plot a line segment
plt.show()
