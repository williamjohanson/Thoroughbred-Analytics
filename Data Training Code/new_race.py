# Library Imports.
import csv
import glob
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import math


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

    i = 0
    winning_list = []

    while i < 1000:
        current_winner = ""
        current_winner_val = -10000
        
        for horse, (mean, std_dev) in result_dict.items(): 
            val = np.random.randn()
            scaled_value = mean + val * std_dev

            if scaled_value > current_winner_val:
                current_winner = horse
                current_winner_val = scaled_value
        winning_list.append(current_winner)

        i += 1
        
        print("Running Simulation {:.2f}%".format(i/1000 * 100))

    for horse in result_dict.keys():
        wins = 0
        for winner in winning_list:
            if winner == horse:
                wins += 1

        print("{} : {}".format(horse, wins))


'''
# For this to work need to have a record of Horse Trainer and Dam and Sire and Jockey or add that into the file when creating the new race. Maybe begin to use a csv.
def compile_horse_error_data(new_horse_array, event_array, horse_event_error_dict, dam_rating_value_dict, sire_rating_value_dict, jockey_rating_value_dict, trainer_rating_value_dict):
    """ Taking the error ratings for each horse, adapt it into a price for the runners chance. """

    predicted_winners_dict = dict()
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

        i = 0
        winning_list = []

        while i < 1000:
            current_winner = ""
            current_winner_val = -math.inf
            
            for horse, (mean, std_dev) in result_dict.items(): 
                for event in event_array:

                    if event.RaceID == race_number and event.HorseName == horse:

                        (mean_dam, std_dev_dam) = dam_rating_value_dict[event.DamID]
                        (mean_sire, std_dev_sire) = sire_rating_value_dict[event.SireID]
                        (mean_jockey, std_dev_jockey) = jockey_rating_value_dict[event.JockeyName]
                        (mean_trainer, std_dev_trainer) = trainer_rating_value_dict[event.Trainer]

                    else:
                        continue

                    val = np.random.randn()
                    #val_dam = np.random.randn()
                    #val_sire = np.random.randn()
                    #val_jockey = np.random.randn()
                    #val_trainer = np.random.randn()
                    # Create random vals for each std_dev?
                    scaled_value = mean + mean_dam + mean_sire + mean_jockey + mean_trainer + val * std_dev + val * std_dev_dam + val * std_dev_sire + val * std_dev_jockey + val * std_dev_trainer
                    #scaled_value = mean + mean_dam + mean_sire + mean_jockey + mean_trainer + val * std_dev + val_dam * std_dev_dam + val_sire * std_dev_sire + val_jockey * std_dev_jockey + val_trainer * std_dev_trainer

                    if scaled_value > current_winner_val:
                        current_winner = horse
                        current_winner_val = scaled_value

            winning_list.append(current_winner)

            i += 1
            

        for horse in result_dict.keys():
            wins = 0
            for winner in winning_list:
                if winner == horse:
                    if horse not in winning_dict.keys():
                        winning_dict[horse] = 1
                    else:
                        winning_dict[horse] += 1

            current_winner = ''
            current_winner_num = 0

            for horse, wins in winning_dict.items():
                if wins > current_winner_num:
                    current_winner = horse
                    current_winner_num = wins
            
            predicted_winners_dict[race_number] = (current_winner, current_winner_num/i)

        print("Analyzed file {}".format(x))

        x += 1

    return predicted_winners_dict
'''

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

