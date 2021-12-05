# Take the .csv files downloaded and compile to a single useful file.

###################################################################################################
###################################################################################################
# Library Imports.
import csv
import glob
###################################################################################################
###################################################################################################

###################################################################################################
###################################################################################################
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
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
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
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
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
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
def compile_records(row_array, fieldnames):
    """ Compile all the records into one .csv file. """
    # Open the .csv file to write too.
    with open('TrainingData.csv', mode='w') as csv_write_file:
        writer = csv.writer(csv_write_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        # Write the rows in row array which is from all the files into the .csv.
        for row in row_array:
            # Check the row has all the complete information.
            ### Do something here lol ###
            writer.writerow(row)
###################################################################################################
###################################################################################################

