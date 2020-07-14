# Weighting Variables #
                
def get_race_file():
    """ Find the data file created for the particular race and create a dictionary of all the runners in that file. """
    name_file = input("What is the number of the race? ")
    open_race_file = open("race" + name_file + ".txt", 'r')
    race_file_lines = []
    line = open_race_file.readline()
    while line != "Back to top":
        line = open_race_file.readline()
        race_file_lines.append(line.strip())
    
    return race_file_lines

def build_runners_dict(race_file):
    """ Build the dictionary containing the horses name, number and barrier number"""
    runner_dict = dict()
    i = 1
    for j in range(1, len(race_file)):
        try:
            if int(race_file[j].strip()) == i:
                name_line = race_file[j + 3].strip('\n').split("(")
                horse_name = (name_line[0])[:-1]
                horse_barrier = name_line[1].split(")")[0]
                jockey_line_amat = race_file[j + 4].strip('\n').split("(")
                try:
                    weight_reduction = float(jockey_line_amat[1].strip("a").strip('\n').strip(")"))
                except IndexError:
                    weight_reduction = 0
                
                if race_file[j + 5].strip('\n') != "SCRATCHED":
                    jockey_line = race_file[j + 10].strip('\n').split("(")
                    jockey = (jockey_line[0])[:-1]
                    jockey_weight = jockey_line[1].split(")")[0]
                    runner_dict[horse_name] = (i, horse_barrier, jockey, jockey_weight, weight_reduction)
                else:
                    runner_dict[horse_name] = (i, horse_barrier, None, None, 0)
                i += 1 
        except ValueError:
            i += 0

    return runner_dict

def ask_user():
    response = ''
    while response.lower() not in {"good", "slow", "dead", "heavy"}:
        response = input("Please enter the track condition: ")
     
    response2 = ''
    while response2.lower() not in {"cw", "acw"}:
        response2 = input("Please enter the direction the race is run? \n (clockwise : cw, anticlockwise : acw) ")
     
    return response.lower(), response2.lower

def runners_chance_dict(runner_dict):
    """ Give all runners a proportional chance to the number of runners in the race in a new dictionary with name as key and weighting as value. """
    weighted_dict = dict()
    i = 0
    for runner, (number, barrier, jockey, jockey_weight, weight_reduction) in runner_dict.items():
        if jockey == None or jockey_weight == None:
            i += 1
        else:
            i += 0
    for runner, (number, barrier, jockey, jockey_weight, weight_reduction) in runner_dict.items():
        if jockey == None or jockey_weight == None:
            weighted_dict[runner] = 1/i
        
    return weighted_dict 
                        
def runners_print(runner_dict):
        print("The runners are: \n ")
        print(runner_dict)
        i = 0
        for key, value in runner_dict.items():   
            number, barrier, jockey, jockey_weight, weight_reduction = value
            if (jockey != None or jockey_weight != None) and (weight_reduction != 0):
                weight = float(jockey_weight.strip("kg"))
                print("- Horse number {} is called {}, barrier {}\n    Jockeyed by apprentice {} at {} minus apprentice claim of {} to ride at {}.\n".format(number, key, barrier, jockey, jockey_weight, weight_reduction, str(weight - weight_reduction) + "kg"))
            elif (jockey != None or jockey_weight != None) and (weight_reduction == 0):
                weight = float(jockey_weight.strip("kg"))
                print("- Horse number {} is called {}, barrier {}\n    Jockeyed by {} at {}\n".format(number, key, barrier, jockey, jockey_weight))                
            else:
                print("- The horse that was number {}, called {}, has been scratched.\n".format(number, key))
                
def main():
    """ Main function to purely call other functions"""
    while (1):
        race_file = get_race_file()
        
        track_condition, direction = ask_user()
    
        runner_dict = build_runners_dict(race_file)
        
        runners_print(runner_dict)
        
        weighted_dict = runners_chance_dict(runner_dict)
        print(weighted_dict)
        
main()
