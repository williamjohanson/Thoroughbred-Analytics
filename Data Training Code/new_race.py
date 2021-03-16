# Library Imports.
import csv
import glob
import matplotlib.pyplot as plt
import numpy as np
import random

def compile_horse_error_data(new_horse_array, horse_event_error_dict):
    """ Taking the error ratings for each horse, adapt it into a price for the runners chance. """
    result_dict = dict()

    for horse in new_horse_array:
        for horse_name, error_array in horse_event_error_dict.items():
            if horse == horse_name:
                if len(error_array) > 1:
                    error_array.sort()
                    mean = sum(error_array) // len(error_array)
                    error_range = error_array[-1] - error_array[0]
                    std_dev = 0
                    for error in error_array:
                        std_dev += (error - mean) ** 2

                    std_dev = int(np.sqrt(std_dev / len(error_array)))

                    result_dict[horse_name] = (mean, std_dev)

    for horse, (mean, std_dev) in result_dict.items():       
        plt.plot()
        print("{} : {} +- {}".format(horse, mean, std_dev))



def return_horse_error_data(new_horse_array, horse_event_error_dict):
    """ Return the error array calculated in event rating for the horses in the new race. """

    for horse in new_horse_array:
        for horse_name, error_array in horse_event_error_dict.items():
            if horse == horse_name:

                print("{} - {}".format(horse_name, error_array))


def open_new_race():
    """ Open a new race file containing the names of the horses."""
    
    race_number = input("What is the race number for analysis? ")
    race_file = "New Race Events/Race " + race_number + ".txt"

    new_horse_array = []

    with open(race_file, mode='r') as txt_file:

        lines = txt_file.readlines()

        for line in lines:
            new_horse_array.append(line.strip())

    return new_horse_array

