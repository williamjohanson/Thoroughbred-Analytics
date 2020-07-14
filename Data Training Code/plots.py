# Create a file to plot the times against different factors.

# Imports.
import matplotlib.pyplot as plt
import numpy as np

def time_vs_distance(event_array):
    """ Plot the times against the different differences raced. """
    distances_array = []
    i = 0

    for event in event_array:
        if event.Distance not in distances_array:
            distances_array.append(event.Distance)       
    
    for event in event_array:
        if event.Distance == '1600':
            if len(event.Actualtime.split(".")) == 3:
                time = event.Actualtime.split(".")
                seconds = int(time[0]) * 60 + int(time[1])
                plt.scatter(int(seconds), float(event.Weight))
                print(seconds)
                i += 1
            
            

    plt.show()

    print(distances_array)