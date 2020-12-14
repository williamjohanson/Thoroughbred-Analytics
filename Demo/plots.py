# Create a file to plot the times against different factors.

# Imports.
import matplotlib.pyplot as plt
import numpy as np

def time_vs_distance(event_array):
    """ Plot the times against the different differences raced. """
    distances_array = []
    time_array = []
    i = 0

    for event in event_array:
        if event.Distance not in distances_array:
            distances_array.append(event.Distance)       
    
    for event in event_array:
        if event.Distance == '2000':
            if len(event.Actualtime.split(".")) == 3:
                time = event.Actualtime.split(".")                       
                milliseconds = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])
                if len(event.Last600mTime.split(".")) == 3:
                    time_600m = event.Last600mTime.split(".")  
                    milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])
                    if (milliseconds_600m != 0) and (milliseconds != 0):
                        plt.scatter(float(milliseconds_600m), int(milliseconds))
                        i += 1

    plt.show()

    print(distances_array)