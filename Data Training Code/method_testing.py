###################################################################################################
###################################################################################################
# Library Imports.
import csv
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
import random

###################################################################################################
###################################################################################################

def average_winning_odds(event_array):
    """ Find the average winning price of every winner. """

    price_sum = 0
    num_events = 0

    for event in event_array:
        if event.Finishingposition == '1':

            try:
                price_sum += float(event.StartingPriceWin)
                num_events += 1

            except ValueError:
                pass
                

    print("{} {}".format(num_events, price_sum/num_events))



def seperate_race_events(event_array):
    """ Find all the seperate events and create a tuple array pointing to the start position, end position and the winning horse from the race. """
    race_ID_dict = dict()


    for event in event_array:
        if event.RaceID not in race_ID_dict.keys():
            race_ID_dict[event.RaceID] = [event.HorseName + '\n']
        else:
            race_ID_dict[event.RaceID].append(event.HorseName + '\n')

    
    for race_ID, horse_name_array in race_ID_dict.items():
        save_path = "C:/Users/willi/OneDrive/Documents/Personal/Thoroughbred-Analytics/Historical Race Events" 

        file_name = race_ID + ".txt"
        race_file = os.path.join(save_path, file_name)
        

        with open(race_file, mode='w') as txt_file:
            txt_file.writelines(horse_name_array)

    return race_ID_dict 


def estimate_winner(race_ID_dict, event_array, horse_event_error_dict, dam_rating_value_dict, sire_rating_value_dict, jockey_rating_value_dict, trainer_rating_value_dict):
    """ Estimate a winner using all career values using new race technique. """

    predicted_winners_dict = dict()

    x = 0

    for race_number in race_ID_dict.keys():


        race_file = "Historical Race Events/" + race_number + ".txt"

        existing_event_horse_array = []

        with open(race_file, mode='r') as txt_file:

            lines = txt_file.readlines()

            for line in lines:
                existing_event_horse_array.append(line.strip())

        result_dict = dict()
        winning_dict = dict()

        for horse in existing_event_horse_array:
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

        #for horse, (mean, std_dev) in result_dict.items():       
            #plt.plot()

        i = 0
        winning_list = []

        while i < 100:
            current_winner = ""
            current_winner_val = -10000
            
            for horse, (mean, std_dev) in result_dict.items(): 
                for event in event_array:

                    if event.RaceID == race_number and event.HorseName == horse:

                        (mean_dam, std_dev_dam) = dam_rating_value_dict[event.DamID]
                        (mean_sire, std_dev_sire) = sire_rating_value_dict[event.SireID]
                        (mean_jockey, std_dev_jockey) = jockey_rating_value_dict[event.JockeyName]
                        (mean_trainer, std_dev_trainer) = trainer_rating_value_dict[event.Trainer]

                    val = np.random.randn()
                    scaled_value = mean + mean_dam + mean_sire + mean_jockey + mean_trainer + val * std_dev + val * std_dev_dam + val * std_dev_sire + val * std_dev_jockey + val * std_dev_trainer

                    if scaled_value > current_winner_val:
                        current_winner = horse
                        current_winner_val = scaled_value

                    break

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
            
            predicted_winners_dict[race_number] = (current_winner, current_winner_num/100)

        print("Analyzed file {}".format(x))

        x += 1

    return predicted_winners_dict

def compare_estimate_to_winners(predicted_winners_dict, event_array):
    """ See what the true winners were and identify if value over time. """
    price_sum = 0
    num_win_events = 0
    num_total_events = 0

    unit = 100
    total_spend_dict = dict()
    total_return_dict = dict()
    
    for event in event_array:
        pred_winning_horse, pred_win_value = predicted_winners_dict[event.RaceID]
        try:
            if event.HorseName == pred_winning_horse and pred_win_value < float(event.StartingPriceWin):

                value_ratio = pred_win_value / float(event.StartingPriceWin)
                num_total_events += 1

                if event.Distance in total_spend_dict.keys():
                    if float(event.StartingPriceWin) < 2:
                        total_spend_dict[event.Distance] += unit * value_ratio * 3

                    elif float(event.StartingPriceWin) > 3.5:
                        total_spend_dict[event.Distance] += unit * value_ratio * 1
                    else:
                        total_spend_dict[event.Distance] += unit * value_ratio * 2
                else:
                    if float(event.StartingPriceWin) < 2:
                        total_spend_dict[event.Distance] = unit * value_ratio * 3

                    elif float(event.StartingPriceWin) > 3.5:
                        total_spend_dict[event.Distance] = unit * value_ratio * 1
                    else:
                        total_spend_dict[event.Distance] = unit * value_ratio * 2


        except ValueError:
                    pass
    
    
    for event in event_array:
        if event.Finishingposition == '1':
            pred_winning_horse, pred_win_value = predicted_winners_dict[event.RaceID]
            if event.HorseName == pred_winning_horse:
                try:
                    
                    if pred_win_value < float(event.StartingPriceWin):

                        value_ratio = pred_win_value / float(event.StartingPriceWin)

                        price_sum += float(event.StartingPriceWin)
                        num_win_events += 1

                        if event.Distance in total_return_dict.keys():
                            if float(event.StartingPriceWin) < 2:
                                total_return_dict[event.Distance] += unit * value_ratio * 3 * float(event.StartingPriceWin)

                            elif float(event.StartingPriceWin) > 3.5:
                                total_return_dict[event.Distance] += unit * value_ratio * 1 * float(event.StartingPriceWin)
                            else:
                                total_return_dict[event.Distance] += unit * value_ratio * 2 * float(event.StartingPriceWin)
                        else:
                            if float(event.StartingPriceWin) < 2:
                                total_return_dict[event.Distance] = unit * value_ratio * 3 * float(event.StartingPriceWin)

                            elif float(event.StartingPriceWin) > 3.5:
                                total_return_dict[event.Distance] = unit * value_ratio * 1 * float(event.StartingPriceWin)
                            else:
                                total_return_dict[event.Distance] = unit * value_ratio * 2 * float(event.StartingPriceWin)

                    else:
                        pass
                    
                except ValueError:
                    pass          
                

    for distance_staked, staked in total_spend_dict.items():
        for distance_return, returned in total_return_dict.items():
            if distance_staked == distance_return:           

                print("At a distance of {}, ${:.2f} was returned from ${:.2f} staked. \n Giving a return percentage of {:.2f}% :(".format(distance_staked, returned, staked, returned/staked))


