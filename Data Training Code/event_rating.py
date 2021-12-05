# Initially will filter by the error over all distances but ideally should be filtered at each distance.


# Import event array.
def find_error(event_array, theta_dict, horse_dict):
    """ Find the error between expected and actual times to create the variance set at each distance for the time of a race run. """

    horse_event_error_dict = dict()     # Value will be an array of errors for each event to the horseName.
    dam_event_error_dict = dict()       # Value will be an array of errors for each event to the DamID.
    sire_event_error_dict = dict()      # Value will be an array of errors for each event to the SireID.
    jockey_event_error_dict = dict()    # Value will be an array of errors for each event to the Jockey.
    trainer_event_error_dict = dict()   # Value will be an array of errors for each event to the Trainer.
    errors_array = []                   # Need all the errors to implement some filtering

    #for horse_name in horse_dict.keys():

        #horse_result_dict = dict()      # Just to observe each horse estimate and actual
        #horse_event_error_array = []    # Create an array to hold the errors then append this array to horse_error_dict.

    for event in event_array:

        #if horse_name == event.HorseName:
            
        try:
            theta_distance_set = theta_dict[event.Distance]
        except KeyError:
            pass

        # Ensure there is a time value entered in spreadsheet.
        if (len(event.Actualtime.split(".")) == 3) and (len(event.Last600mTime.split(".")) == 3):
            time = event.Actualtime.split(".")                       
            milliseconds = int(time[0]) * 6000 + int(time[1]) * 100 + int(time[2])                          # Millisecond sum. 1/100th of a second.
            time_600m = event.Last600mTime.split(".")  
            milliseconds_600m = int(time_600m[0]) * 6000 + int(time_600m[1]) * 100 + int(time_600m[2])      # Millisecond sum. 1/100th of a second.

        estimate = theta_distance_set[0] * milliseconds_600m + theta_distance_set[1] * float(event.CarriedWeight) + theta_distance_set[2] * int(event.RaceTrackConditionScale) + theta_distance_set[3] * int(event.Barrier) + theta_distance_set[4] * int(event.Age) + theta_distance_set[5] * int(event.DomesticRating)

        #horse_result_dict[estimate] = milliseconds
        error_diff = int(estimate - milliseconds)

        if event.HorseName not in horse_event_error_dict.keys():
            horse_event_error_dict[event.HorseName] = [error_diff]
        else:
            horse_event_error_dict[event.HorseName].append(error_diff)
        '''
        if event.DamID not in dam_event_error_dict.keys():
            dam_event_error_dict[event.DamID] = [error_diff]
        else:
            dam_event_error_dict[event.DamID].append(error_diff)

        if event.SireID not in sire_event_error_dict.keys():
            sire_event_error_dict[event.SireID] = [error_diff]
        else:
            sire_event_error_dict[event.SireID].append(error_diff)

        if event.JockeyName not in jockey_event_error_dict.keys():
            jockey_event_error_dict[event.JockeyName] = [error_diff]
        else:
            jockey_event_error_dict[event.JockeyName].append(error_diff)

        if event.Trainer not in trainer_event_error_dict.keys():
            trainer_event_error_dict[event.Trainer] = [error_diff]
        else:
            trainer_event_error_dict[event.Trainer].append(error_diff)

            #horse_event_error_array.append(error_diff)
            #errors_array.append(error_diff)

        #horse_event_error_dict[horse_name] = horse_event_error_array

        #for horse, arrays in horse_event_error_dict.items():
        #    print("{} - {}".format(horse, arrays))
        '''
    print(len(horse_event_error_dict.keys()))
    print(len(horse_dict.keys()))
    #for names in jockey_event_error_dict.keys():
    #    print(names + "\n")

    return horse_event_error_dict#, dam_event_error_dict, sire_event_error_dict, jockey_event_error_dict, trainer_event_error_dict

            

# Need to import a median and a variance for each distance.
# ---- This would be more efficient than how i recalculate everything.


# Find where the event sits relative to the median - gives a distance/error offset. Add in the variance.

# The error is the PRE - Performance Relative to Expectation.

# Plot the errors, should be a bell curve! 

# Remove outliers/filter but need to ensure dont remove freaks just frogs.

# Over the range give the best a 100? and the worst a 0?  Develop a rating/handicap system.

# Apply ratings to horse/dam/sire/trainer/jockey.

# New file: Apply regression to the five factors to determine its final rating.

# Compare ratings across horses in a race.

# How do i apply all the intial conditions for the specific race as in the initial rating? Without the final 600m