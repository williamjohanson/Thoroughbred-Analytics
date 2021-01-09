# Construct arrays/dicts to compile similar data into respective arrays.

###################################################################################################
###################################################################################################
# Library Imports.
import csv
import glob
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
def construct_event_array():
    """ Place all the events into RaceEvent class and append to a list. """
    event_array = []
    with open('TrainingData.csv', mode='r') as csv_training_file:
        reader = csv.DictReader(csv_training_file)

        for row in reader:
            if row['Date'] != 'Date':
                # Append the array with the RaceEvent class type.
                event_array.append(RaceEvent(row['Date'], row['JetBet'], row['Track'], row['DayType'], row['MeetingType'], row['Club'], row['MeetingName'],
                row['TrackCondition'], row['TrackConditionScale'], row['TrackWeather'], row['Rail'], row['RaceID'], row['RaceNumber'], row['RaceGroup'],
                row['RaceType'], row['Distance'], row['RaceClass'], row['RaceName'], row['Stake'], row['Time'], row['NoAllowances'], row['MinWeight'], row['ClassAge'],	
                row['Class'], row['ClassGender'], row['ClassWeight'], row['RaceTrackCondition'], row['RaceTrackConditionScale'], row['RaceWeather'],	
                row['HorseID'], row['ToteNumber'], row['Barrier'], row['HorseName'], row['Age'], row['Gender'], row['Weight'], row['Finishingposition'], row['Actualtime'],	
                row['Last600mTime'], row['Decimalmargin'], row['Traditionalmargin'], row['Trainer'], row['TrainerLocation'], row['StartingPriceWin'],	
                row['StartingPricePlace'], row['JockeyName'], row['CarriedWeight'], row['WeightDifference'], row['DomesticRating'], 
                row['HurdlesRating'], row['SteeplesRating'], row['GearWorn'], row['SireID'], row['Sire'], row['DamID'], row['Dam']))


    return event_array
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
def construct_distance_dict(event_array):
    """ Create a dictionary of the range of distances against the number of data points. """
    distance_dict = {}

    for event in event_array:
        if event.Distance not in distance_dict.keys():
            distance_dict[event.Distance] = 1
        else:
            distance_dict[event.Distance] += 1

    for distance, number in distance_dict.items():
        print("{} : {}".format(distance, number))


    return distance_dict
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
def construct_horse_dict(event_array):
    """ Construct dictionary of the number of each horses runs. """
    horse_dict = {}
    i = 0

    for event in event_array:
        if event.HorseName not in horse_dict.keys():
            horse_dict[event.HorseName] = 1
            i += 1
        else:
            horse_dict[event.HorseName] += 1

    max_array = [] 

    for horse, number in horse_dict.items():
        print("{} : {}".format(horse, number))
        if number > 10:
            i += 1
    print(i)


    return horse_dict
###################################################################################################
###################################################################################################

