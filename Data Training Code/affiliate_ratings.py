# Library Imports.
import csv
import glob
import matplotlib.pyplot as plt
import numpy as np
import random

def dam_rating(dam_event_error_dict):
    """ """
    dam_rating_value_dict = dict()

    for dam_ID, error_array in dam_event_error_dict.items():
        if len(error_array) >= 1:
            error_array.sort()
            mean = sum(error_array) // len(error_array)
            error_range = error_array[-1] - error_array[0]
            std_dev = 0
            for error in error_array:
                std_dev += (error - mean) ** 2

            std_dev = int(np.sqrt(std_dev / len(error_array)))

            dam_rating_value_dict[dam_ID] = (mean, std_dev)

    return dam_rating_value_dict


def sire_rating(sire_event_error_dict):
    """ """
    sire_rating_value_dict = dict()

    for sire_ID, error_array in sire_event_error_dict.items():
        if len(error_array) >= 1:
            error_array.sort()
            mean = sum(error_array) // len(error_array)
            error_range = error_array[-1] - error_array[0]
            std_dev = 0
            for error in error_array:
                std_dev += (error - mean) ** 2

            std_dev = int(np.sqrt(std_dev / len(error_array)))

            sire_rating_value_dict[sire_ID] = (mean, std_dev)

    return sire_rating_value_dict 


def jockey_rating(jockey_event_error_dict):
    """ """
    jockey_rating_value_dict = dict()

    for jockey, error_array in jockey_event_error_dict.items():
        if len(error_array) >= 1:
            error_array.sort()
            mean = sum(error_array) // len(error_array)
            error_range = error_array[-1] - error_array[0]
            std_dev = 0
            for error in error_array:
                std_dev += (error - mean) ** 2

            std_dev = int(np.sqrt(std_dev / len(error_array)))

            jockey_rating_value_dict[jockey] = (mean, std_dev)

    return jockey_rating_value_dict 


def trainer_rating(trainer_event_error_dict):
    """ """
    trainer_rating_value_dict = dict()

    for trainer, error_array in trainer_event_error_dict.items():
        if len(error_array) >= 1:
            error_array.sort()
            mean = sum(error_array) // len(error_array)
            error_range = error_array[-1] - error_array[0]
            std_dev = 0
            for error in error_array:
                std_dev += (error - mean) ** 2

            std_dev = int(np.sqrt(std_dev / len(error_array)))

            trainer_rating_value_dict[trainer] = (mean, std_dev)

    return trainer_rating_value_dict 