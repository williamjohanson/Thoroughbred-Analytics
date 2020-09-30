# Create weightings to sum to the actual run time.

# Imports.
import matplotlib.pyplot as plt
import numpy as np

def weightings_main(event_array):
    """ Main function to create the weightings values. """
    y_array = []
    final_600m_array = []
    weight_array = []
    track_con_array = []
    barrier_array = []
    age_array = []
    est_dict = dict()
    est_array = []
    error_array = []
    distance_array = []

    # Need to keep this for loop as milliseconds = y
    for event in event_array:
        #if event.Distance == '1000':
        if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
            time = event.Actualtime.split(".")                       
            milliseconds = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])
            time_600m = event.Last600mTime.split(".")  
            milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])

            if (milliseconds_600m != 0) and (milliseconds != 0):
                y_array.append(milliseconds)
                final_600m_array.append(milliseconds_600m)
                weight_array.append(float(event.CarriedWeight))
                track_con_array.append(int(event.RaceTrackConditionScale))
                barrier_array.append(int(event.Barrier))
                age_array.append(int(event.Age))

    trans_y_array = np.transpose(y_array)
    A_array = np.array([final_600m_array,weight_array,track_con_array,barrier_array,age_array])
    A_array = np.transpose(A_array)
    #print(A_array.shape)
    print(trans_y_array.shape)    
    trans_A_array = np.transpose(A_array)
    theta = np.dot(trans_A_array,A_array)
    theta = np.linalg.inv(theta)
    theta = np.dot(theta, trans_A_array)
    theta = np.dot(theta, trans_y_array) 
    print(theta)

    for event in event_array:
        #if event.Distance == '1000':
        if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
            time = event.Actualtime.split(".")                       
            actual_time = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])
            time_600m = event.Last600mTime.split(".")  
            milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])

            if (milliseconds_600m != 0) and (actual_time != 0):
                estimate = theta[0] * milliseconds_600m + theta[1] * float(event.CarriedWeight) + theta[2] * int(event.RaceTrackConditionScale) + theta[3] * int(event.Barrier) + theta[4] * int(event.Age)
                #est_dict[event.Distance] = (estimate, actual_time - estimate)
                est_array.append(estimate)

    est_array = np.array(est_array)
    #for key, (est, error) in est_dict.items():
     #   if key not in distance_array:
      #      distance_array.append(key)
       # est_array.append
    #print(len(distance_array))
    plt.subplot(121)
    plt.scatter(est_array, y_array)

    error = np.absolute(est_array - y_array)

    average_error = sum(error) / len(error)
    print(average_error)

    plt.subplot(122)
    plt.scatter(y_array, error)

    plt.show()
'''

# Start with mapping Last 600m to the actual time 

# Run through again and estimate.

# Plot the error!

# Plot the error against distance, assume sprints will be closer approximation!'''