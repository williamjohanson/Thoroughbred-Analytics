# Extract data from the records folder.
# Determine averages from the data.
# Create sets of data for each runner from the data.

# Set of inputs.
# Convolve the inputs.
# Determine weightings to match expected outcome to the actual outcome.
# Forwards and backwards until the perfect weights?? Dont know if possible without being a very small learning rate and difference value.
# Use those weightings on imported set of runners.


# Import sets of runners.
# Evaluate runner set based on trained data.
# Since we know all the inputs for the new set of runners and have trained the data to determine the weights based on historical weights...

##  Inputs
#- Average speed difference on same track.
#- Average speed difference on different tracks.
#- Left hand, right hand.
#- Track conditions.
#- Last 600.
#- Trainer results.
#- Jockey results.
#- Weather conditions.
#- Weight conditions.
#- Barrier.
#- Expected distance change times (based on previous percentage changes from distance change).
#- Ratings (expected race difficulty).

# Run the weightings over all data and then increases for previous 3 months?

# Create a GUI.
# Create an API.
# Create a web based APP.
# Create a website.
# Sell the product.
# Make the moneys.

# Library Imports.
import csv
import glob

# File imports.
from RaceEvent import RaceEvent
from plots import time_vs_distance
from weightings import weightings_main

def new_race_runners():
    """ Open a text file of runners in the upcoming race.
    To be expanded into new race events in future. """
    file_location = 'NewRace.txt'
    new_horse_array = []
    with open(file_location, mode='r') as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            new_horse_array.append(line.strip())

    return new_horse_array

def discover_files():
    """ Using the glob import discover all the file locations from the base folder. """
    # Count the number of discovered files for matching.
    i = 0
    # Create an array to place all the file locations for access.
    file_array = []
    # Create a list of the record directory seperated by month and year.
    directs = list(glob.glob('Records/20*'))

    # Iterate through each directory and find each file in them.
    for direct in directs:
        filenames = list(glob.glob(direct + '/Race_*'))
        # Save the file locations to the array.
        for files in filenames:
            file_array.append(files)
            i += 1

    return file_array

def read_records(file_array):
    """ Read the records from the downloaded .csv files. """
    # Read all the csv files.
    line_count = 0
    row_array = []
    for file_location in file_array:
        with open(file_location, newline='') as csv_file:
            # Read the files into a dictionary.
            csv_reader = csv.DictReader(csv_file)
            try:
                for row in csv_reader:
                    # First line is the dictionary headers.
                    if line_count == 0:
                        fieldnames = row[None]
                        line_count += 1
                    else:
                        try:
                            row_array.append(row[None])
                        except KeyError:
                            pass
            except UnicodeDecodeError:
                pass
        line_count = 0
    
    return row_array, fieldnames

def compile_records(row_array, fieldnames):
    """ Compile all the records into one .csv file. """
    # Open the .csv file to write too.
    with open('TrainingData.csv', mode='w') as csv_write_file:
        writer = csv.writer(csv_write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        # Write the rows in row array which is from all the files into the .csv.
        for row in row_array:
            writer.writerow(row)

def construct_event_array():
    """ Place all the events into RaceEvent class and append to a list. """
    event_array = []
    with open('TrainingData.csv', mode='r') as csv_training_file:
        reader = csv.DictReader(csv_training_file)
        for row in reader:
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

def print_new_race_form(new_horse_array, event_array):
    """ Print out all the available form of each horse in the new race. """
    for horse in new_horse_array:
        for RaceEvent in event_array:
            if horse == RaceEvent.HorseName:
                line = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},".format(RaceEvent.Date, RaceEvent.JetBet, RaceEvent.Track, RaceEvent.DayType, RaceEvent.MeetingType, RaceEvent.Club, RaceEvent.MeetingName,
    RaceEvent.TrackCondition, RaceEvent.TrackConditionScale, RaceEvent.TrackWeather, RaceEvent.Rail, RaceEvent.RaceID, RaceEvent.RaceNumber, RaceEvent.RaceGroup,
    RaceEvent.RaceType, RaceEvent.Distance,	RaceEvent.RaceClass, RaceEvent.RaceName, RaceEvent.Stake, RaceEvent.Time, RaceEvent.NoAllowances, RaceEvent.MinWeight, RaceEvent.ClassAge,	
    RaceEvent.Class, RaceEvent.ClassGender,	RaceEvent.ClassWeight, RaceEvent.RaceTrackCondition, RaceEvent.RaceTrackConditionScale, RaceEvent.RaceWeather,	
    RaceEvent.HorseID, RaceEvent.ToteNumber, RaceEvent.Barrier, RaceEvent.HorseName, RaceEvent.Age, RaceEvent.Gender, RaceEvent.Weight, RaceEvent.Finishingposition, RaceEvent.Actualtime,	
    RaceEvent.Last600mTime, RaceEvent.Decimalmargin, RaceEvent.Traditionalmargin, RaceEvent.Trainer, RaceEvent.TrainerLocation, RaceEvent.StartingPriceWin,	
    RaceEvent.StartingPricePlace, RaceEvent.JockeyName, RaceEvent.CarriedWeight, RaceEvent.WeightDifference, RaceEvent.DomesticRating, 
    RaceEvent.HurdlesRating, RaceEvent.SteeplesRating, RaceEvent.GearWorn, RaceEvent.SireID, RaceEvent.Sire, RaceEvent.DamID, RaceEvent.Dam)

                print(horse + " : " + line)

def main(): 
    """ The main function. """
    new_horse_array = new_race_runners()

    file_array = discover_files()
    
    row_array, fieldnames = read_records(file_array)
    
    compile_records(row_array, fieldnames)

    event_array = construct_event_array()

    #distance_dict = construct_distance_dict(event_array)

    #horse_dict = construct_horse_dict(event_array)

    #print_new_race_form(new_horse_array, event_array)

    #time_vs_distance(event_array)

    weightings_main(event_array)
    

main()