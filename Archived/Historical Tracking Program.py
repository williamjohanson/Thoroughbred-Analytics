#Split data into individual races.

#Create a horse object.

#Create a dictionary of horses.

# Create a dictionary of jockeys?

#For each horse manipulate its data based on previous runs and the conditions which led to its run, toughness of opponents, distance from its opponenets. 

#Need a bias on each factor.

#Iterate through all races so that all horses race history is stored.

#Output to a .csv file.

#Reupload .csv file everytime to then manipulate ratings and then overwrite  original file so that it is updated. 

#Using upcoming races, compare all the horses in the race from the dictionary.

#---------------------------------------------------------------------------------------------------#

""" Import Libraries. """

import csv

#---------------------------------------------------------------------------------------------------#

""" GLOBAL VARIABLES. """

HORSE_LIST = []

#---------------------------------------------------------------------------------------------------#

""" Define the horse class to contain attributes for data. """
class Horse:
    
    def __init__(self, name, ID_number, current_age, current_gender, current_trainer, current_trainer_location, sireID, sire, damID, dam):
        self.name = name
        self.ID_number = ID_number
        self.current_age = current_age
        self.current_gender = current_gender
        self.current_trainer = current_trainer
        self.current_trainer_location = current_trainer_location
        self.sireID = sireID
        self.sire = sire
        self.damID = damID
        self.dam = dam
    
    #def jockey_performances():
         
    #def track_performances():
        
    #def track_condition_performances():
        
    #age_performances():
    
    #day_type_performances():
    
    #rail_performances():
    
    #race_type_performances():
    
    #distance_performances():
    
    #race_class_performances():
    
    #barrier_performances():
    
    #weight_performances():       
        
#---------------------------------------------------------------------------------------------------#
    
def update_HORSE_LIST():
    """ Read the horse records and update the HORSE_LIST global variable. """
    global HORSE_LIST
    j = 0
    i = 0
    with open('Horse Records.csv') as csvfile:
        horse_file_lines = csv.reader(csvfile, delimiter=',')
        for row in horse_file_lines:    
            i += 1
            try:
                name = row[0]
                ID_number = row[1]
                current_age = row[2]
                current_gender = row[3]
                current_trainer = row[4]
                current_trainer_location = row[5]
                sireID = row[6]
                sire = row[7]
                damID = row[8]
                dam = row[9]
                HORSE_LIST.append(Horse(name, ID_number, current_age, current_gender, current_trainer, current_trainer_location, sireID, sire, damID, dam))
            except IndexError:
                break
        # Clear the read horse records file
    filename = "Horse Records.csv"
    # opening the file with w+ mode truncates the file
    f = open(filename, "w")
    f.truncate()
    f.close()
    
#--------------------------------------------------------------------------------------------------#    

def get_result_csv_file():
    """ Upload the results file in the .csv format. """
    name_file = input("What is the number of the race? ")
    open_race_file = open("Race_" + name_file + ".csv", mode='r')  
    race_file_lines = []
    i = 0
    line_list = open_race_file.readline().strip().split(",")
    while i < 2:
        if line_list == ['']:
            i += 1
        if ((len(line_list) > 1) and (line_list[25] == '"c') and (line_list[26] == 'g&e"')):
            line_list_a = line_list[27:]
            line_list = line_list[0:25]
            line_list.append('cg&e')
            for item in line_list_a:
                line_list.append(item)
        race_file_lines.append(line_list)
        line_list = open_race_file.readline().strip().split(",")
    
    race_file_lines = race_file_lines[3:-1]       
    
    return race_file_lines   

#---------------------------------------------------------------------------------------------------#

def print_race_file_lines(race_file_lines):
    """ Print the race file lines in raw form. """
    for line in race_file_lines:
        print(len(line))
        print(line)

#---------------------------------------------------------------------------------------------------#

def race_result(individual_race_array):
    """ Analysis of the race result"""
    runners = len(individual_race_array)
    print(runners)
    for line in individual_race_array:  
        race_position = line[37].strip('"')
        try:
            margin = line[40].strip('"')
        except ValueError:
            margin = None
    
    return None
        
#---------------------------------------------------------------------------------------------------#

def fill_horse_dict(race_file_lines):
    """ Fill out a horse dictionary, adding new horses (objects)
    if they aren't already contained. Eventually have an object for every horse raced in NZ. """
    global HORSE_LIST
    j = 0
    i = 0
    k = 1
    individual_race_array = []
    for line in race_file_lines:
        
        # Extract Horse Information
        name = line[33].strip('"')
        ID_number = line[30].strip('"')
        current_age = line[34].strip('"')
        current_gender = line[35].strip('"')
        current_trainer = line[42].strip('"')
        current_trainer_location = line[43].strip('"')
        sireID = line[54].strip('"')
        sire = line[55].strip('"')
        damID = line[56].strip('"')
        dam = line[57].strip('"').strip()
        
        race_number = int(line[13].strip('"'))
        
        # Extract Race Results
        if (race_number == k):
            individual_race_array.append(line)
        else:
            race_grade = race_result(individual_race_array)
            k += 1
            individual_race_array = []
        jockey = line[47].strip('"')
        track = line[3].strip('"')
        track_condition = line[27].strip('"')
        day_type = line[29].strip('"')
        rail = line[11].strip('"')
        race_type = line[15].strip('"')
        distance = line[16].strip('"')
        race_class = line[17].strip('"')
        barrier = line[32].strip('"')
        try:
            weight = int(line[48].strip('"'))
        except ValueError:
            weight = int(float(line[36].strip('"')))
        
        horse = Horse(name, ID_number, current_age, current_gender, current_trainer, current_trainer_location, sireID, sire, damID, dam)
        
        # Remove double ups by comparing to horses already in HORSE_LIST
        for horsey in HORSE_LIST:
            ID_number_2 = int(horsey.ID_number)
            if (ID_number_2 == int(ID_number)):
                i = 1
            else:
                j = 0
        if ((j == 0) and (i != 1)):         
            HORSE_LIST.append(horse)
        i = 0
        
#---------------------------------------------------------------------------------------------------#

def export_updated_horse_list():
    """ Print the global Horse list that has been updates with newly discovered horses each iteration. """
    global HORSE_LIST
    i = 1
    open_horse_file = open("Horse Records.csv", mode='w', newline = '')  
    horse_writer = csv.writer(open_horse_file, delimiter=',', quotechar='"')

    for horsey in HORSE_LIST:  
        horse_writer.writerow([horsey.name, horsey.ID_number, horsey.current_age, horsey.current_gender, horsey.current_trainer, horsey.current_trainer_location, horsey.sireID, horsey.sire, horsey.damID, horsey.dam])    
        i += 1

#---------------------------------------------------------------------------------------------------#

def clear_HORSE_LIST():
    """ Run through the list and remove all the elements so that the output isn't doubling up! """
    global HORSE_LIST
    del HORSE_LIST[:]
    
#---------------------------------------------------------------------------------------------------#
def main():
    """ Main program uses a sequencer. """
    global HORSE_LIST
    while (1): 
        
        race_file_lines = get_result_csv_file() # Return a list of lines from the CSV file with the /n removed.
        
        #print_race_file_lines(race_file_lines)
        
        update_HORSE_LIST()
        
        fill_horse_dict(race_file_lines)
        
        export_updated_horse_list()
        
        clear_HORSE_LIST()

#---------------------------------------------------------------------------------------------------#

main()