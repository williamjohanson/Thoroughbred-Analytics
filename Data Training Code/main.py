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

###################################################################################################
###################################################################################################
# Library Imports.
import csv
import glob
###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
# File imports.
from RaceEvent import RaceEvent
#from plots import time_vs_distance
from weightings import weightings_main
from compile_records import *
from construct_data_arrays import *
from event_rating import *
from new_race import *
from method_testing import *
from affiliate_ratings import *

###################################################################################################
###################################################################################################


###################################################################################################
###################################################################################################
def main(): 
    """ The main function. """
    # Only required to refresh with new data.
    ##################################################################################

    #file_array = discover_files()
    
    #row_array, fieldnames = read_records(file_array)
    
    #compile_records(row_array, fieldnames)

    ###################################################################################

    event_array = construct_event_array()
    horse_dict = construct_horse_dict(event_array)
    theta_dict = weightings_main(event_array)

    horse_event_error_dict = find_error(event_array, theta_dict, horse_dict) 
    '''
    horse_event_error_dict, dam_event_error_dict, sire_event_error_dict, jockey_event_error_dict, trainer_event_error_dict = find_error(event_array, theta_dict, horse_dict)
    
    dam_rating_value_dict = dam_rating(dam_event_error_dict)
    sire_rating_value_dict = sire_rating(sire_event_error_dict)
    jockey_rating_value_dict = jockey_rating(jockey_event_error_dict)
    trainer_rating_value_dict = trainer_rating(trainer_event_error_dict)

    #layer_2_horse_event_error_dict = weight_key_factor_errors(dam_rating_value_dict, sire_rating_value_dict, jockey_rating_value_dict, trainer_rating_value_dict)

    #average_winning_odds(event_array)

    race_ID_dict = seperate_race_events(event_array)

    predicted_winners_dict = estimate_winner(race_ID_dict, event_array, horse_event_error_dict, dam_rating_value_dict, sire_rating_value_dict, jockey_rating_value_dict, trainer_rating_value_dict)

    compare_estimate_to_winners(predicted_winners_dict, event_array)
    '''   

    while(1):
        
        new_horse_array = open_new_race()

        return_horse_error_data(new_horse_array, horse_event_error_dict)

        compile_horse_error_data(new_horse_array, horse_event_error_dict)
        #compile_horse_error_data(new_horse_array, event_array, horse_event_error_dict, dam_rating_value_dict, sire_rating_value_dict, jockey_rating_value_dict, trainer_rating_value_dict)

    #distance_dict = construct_distance_dict(event_array)

    #print_new_race_form(new_horse_array, event_array)

    #time_vs_distance(event_array)

    #theta_dict = weightings_main(event_array)


###################################################################################################
###################################################################################################   
main()
###################################################################################################
###################################################################################################