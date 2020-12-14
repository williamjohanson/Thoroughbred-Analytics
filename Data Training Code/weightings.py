# Create weightings to sum to the actual run time.

# Imports.
import matplotlib.pyplot as plt
import numpy as np
import random

def estimate_historical(event_array):
    """ Estimate the historical times expected for each event based on all existing events. """

    # Set up data arrays to create A matrix.
    distance_dict = dict()
    theta_dict = dict()

    # Find all the distances and cases at each distance.
    for event in event_array:
        if event.Distance not in distance_dict.keys():
            distance_dict[event.Distance] = 1
        else:
            distance_dict[event.Distance] += 1

    for distance, value in distance_dict.items():
        print("{} - {} unique values.".format(distance, value))

    print(len(distance_dict.keys()))

    # Create a numerically ordered list of the distances. 
    # Since strings < 1000 comes up as largest!
    event_distances = sorted(distance_dict.keys())


    print(event_distances)

    # Iterate through all distances.
    for i in range(len(event_distances)):

        # Reset all the arrays/dicts used for each distance.
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
            # Define each distance range. 
            # Must be a better way than by each individual distance.
            if event.Distance == event_distances[i]:
                # Ensure there is a time value entered in spreadsheet.
                if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
                    time = event.Actualtime.split(".")                       
                    milliseconds = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])                          # Millisecond sum. 1/100th of a second.
                    time_600m = event.Last600mTime.split(".")  
                    milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])      # Millisecond sum. 1/100th of a second.

                    
                    if (milliseconds_600m != 0) and (milliseconds != 0):
                        y_array.append(milliseconds)
                        final_600m_array.append(milliseconds_600m)
                        weight_array.append(float(event.CarriedWeight))
                        track_con_array.append(int(event.RaceTrackConditionScale))
                        barrier_array.append(int(event.Barrier))
                        age_array.append(int(event.Age))

        #print(i)

        # Issue with not enough events causing a singularity.
        try:

            trans_y_array = np.transpose(y_array)
            A_array = np.array([final_600m_array,weight_array,track_con_array,barrier_array,age_array])
            A_array = np.transpose(A_array)
            #print(A_array.shape)
            #print(trans_y_array.shape)    
            trans_A_array = np.transpose(A_array)
            theta = np.dot(trans_A_array,A_array)
            theta = np.linalg.inv(theta)
            theta = np.dot(theta, trans_A_array)
            theta = np.dot(theta, trans_y_array) 
            theta_dict[event_distances[i]] = theta
            #print(theta)

            for event in event_array:
                if event.Distance == event_distances[i]:
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
            #plt.subplot(121)
            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)

            plt.subplot(121)
            plt.scatter(est_array, y_array, color=color, alpha=0.2, label=event_distances[i])

            error = np.absolute(est_array - y_array)

            average_error = sum(error) / len(error)
            print("{} {}".format(event_distances[i], average_error))

            plt.subplot(122)
            plt.scatter(y_array, error)

        except:
            pass


    for distance, theta in theta_dict.items():
        print("{}, {}".format(distance, theta))
 
###################################################################################################
    return theta_dict
###################################################################################################

def estimate_filtered_historical(event_array):
    """ Use a Iglewicz and Hoaglin modified Z-score filter to get a better estimation by removing outliers. """
    # Set up data arrays to create A matrix.
    distance_dict = dict()
    theta_dict = dict()

    # Find all the distances and cases at each distance.
    for event in event_array:
        if event.Distance not in distance_dict.keys():
            distance_dict[event.Distance] = 1
        else:
            distance_dict[event.Distance] += 1

    for distance, value in distance_dict.items():
        print("{} - {} unique values.".format(distance, value))

    print(len(distance_dict.keys()))

    # Create a numerically ordered list of the distances. 
    # Since strings < 1000 comes up as largest!
    event_distances = sorted(distance_dict.keys())


    print(event_distances)

    # Iterate through all distances.
    for i in range(len(event_distances)):

        # Reset all the arrays/dicts used for each distance.
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
            # Define each distance range. 
            # Must be a better way than by each individual distance.
            if event.Distance == event_distances[i]:
                # Ensure there is a time value entered in spreadsheet.
                if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
                    time = event.Actualtime.split(".")                       
                    milliseconds = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])                          # Millisecond sum. 1/100th of a second.
                    time_600m = event.Last600mTime.split(".")  
                    milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])      # Millisecond sum. 1/100th of a second.

                    
                    if (milliseconds_600m != 0) and (milliseconds != 0):
                        y_array.append(milliseconds)
                        final_600m_array.append(milliseconds_600m)
                        weight_array.append(float(event.CarriedWeight))
                        track_con_array.append(int(event.RaceTrackConditionScale))
                        barrier_array.append(int(event.Barrier))
                        age_array.append(int(event.Age))

        print(i)

        # Issue with not enough events causing a singularity.
        try:

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
            theta_dict[event_distances[i]] = theta
            print(theta)

            for event in event_array:
                if event.Distance == event_distances[i]:
                    if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
                        time = event.Actualtime.split(".")                       
                        actual_time = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])
                        time_600m = event.Last600mTime.split(".")  
                        milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])

                        if (milliseconds_600m != 0) and (actual_time != 0):
                            estimate = theta[0] * milliseconds_600m + theta[1] * float(event.CarriedWeight) + theta[2] * int(event.RaceTrackConditionScale) + theta[3] * int(event.Barrier) + theta[4] * int(event.Age)
                            #est_dict[event.Distance] = (estimate, actual_time - estimate)
                            est_array.append(estimate)

                            error_array.append(actual_time - estimate)
            

            error_array = sorted(error_array)
            median = error_array[int(len(error_array) / 2)]

            abs_error_array = [abs(ele) for ele in error_array]
            abs_error_array = sorted(abs_error_array)
            abs_median = abs_error_array[int(len(abs_error_array) / 2)]

            M_array = []

            for error in error_array:
                M_array.append(0.6745 * (float(error) - float(median)) / float(abs_median))

            filtered_actual_time = []
            filtered_est_array = []

            for j in range(len(M_array)):
                if abs(M_array[j]) <= 3.5:
                    filtered_est_array.append(est_array[j])
                    filtered_actual_time.append(y_array[j])
                    

            filtered_est_array = np.array(filtered_est_array)
            filtered_actual_time = np.array(filtered_actual_time)
            
            error_avg = sum(abs(abs(filtered_actual_time) - abs(filtered_est_array))) / len(filtered_actual_time)

            print("{} : {}".format(event_distances[i], error_avg))

            r = random.random()
            b = random.random()
            g = random.random()
            color = (r, g, b)

            plt.subplot(122)
            plt.scatter(filtered_est_array, filtered_actual_time, color=color, alpha=0.2, label=event_distances[i])


        

        except:
            pass


def weightings_main(event_array):
    """ Main function of all the weightings data. """

    theta_dict = estimate_historical(event_array)

    #estimate_filtered_historical(event_array)

    plt.show()
    
    return theta_dict
    
    #plt.legend()
    

    
'''

# Start with mapping Last 600m to the actual time 

# Run through again and estimate.

# Plot the error!

# Plot the error against distance, assume sprints will be closer approximation!'''