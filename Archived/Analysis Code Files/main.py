# main.py
# Set up the code to iterate through as desired utilising a GUI for inputs.
# Need to add user inputs for race meet and number of races and can then record the race data down.

# Imports. 
import fill_txt_data

# GUI Specific Imports. 
import tkinter as tk
from tkinter import *
import os 
from PIL import Image, ImageTk

# Create the Thoroughbred Class
from thoroughbred import Thoroughbred

# Set canvas size variables.
HEIGHT = 900
WIDTH = 1500

# Globals.
MEETING = 0.1
TOTAL_RACES = 0.1

# Run the config function init to set up globals.
# Dont have a config set up yet.

# Enter main functions for both GUI and analysis.
def fill_data(meet, race):
    """ Fill the text files with data. """
    global MEETING
    global TOTAL_RACES
    if race == None:
        try:
            MEETING = float(meet)
            results['text'] = str(int(MEETING))
        except ValueError:
            results['text'] = "Try entering meeting code again."
    elif meet == None:
        try:
            TOTAL_RACES = float(race)
            results['text'] = str(int(MEETING))
        except ValueError:
            results['text'] = "Try entering the number of races again."

    # Extract race information.
    if MEETING.is_integer() and TOTAL_RACES.is_integer():
        fill_txt_data.web_extract(int(MEETING), int(TOTAL_RACES))

# Try except commented out to allow debugging.
# Lots of new code going in.
def main(race_num):
    """ Main function to poll other functions. """
    #try:
    #new_race_file = race_file.get_race_file(race_num)
    
    #runners_list, num_runners = runners_dict.create_horses_running(new_race_file) 

    

    #results['text'] = result_str

    

    #except:
       # results['text'] = "There has been an error analysing this race."

#-------------------------------------------------------------------------------------------------#

# GUI Setup. 
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="#263D42")

background_image = ImageTk.PhotoImage(Image.open('Images/background.png'))
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

upper_frame = Frame(root,  bg='#42c2f4', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

frame = Frame(root,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

meet_textbox = Entry(upper_frame, font=40)
meet_textbox.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

race_textbox = Entry(upper_frame, font=40)
race_textbox.place(relx=0.5, rely=0,relwidth=0.5, relheight=0.5)

meet_exe_button = Button(upper_frame, text='Enter Meet No.', font=40, command=lambda: fill_data(meet_textbox.get(), None))
meet_exe_button.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)

race_exe_button = Button(upper_frame, text='Enter No. of Races', font=40, command=lambda: fill_data(None, race_textbox.get()))
race_exe_button.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.45, anchor='n')

textbox = Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

race_1_button = Button(frame, text='Analyse Race 1', font=40, command=lambda: main('1.txt'))
race_1_button.place(relx=0, rely=0, relheight=0.33, relwidth=0.2)

race_2_button = Button(frame, text='Analyse Race 2', font=40, command=lambda: main('2.txt'))
race_2_button.place(relx=0.2, rely=0, relheight=0.33, relwidth=0.2)

race_3_button = Button(frame, text='Analyse Race 3', font=40, command=lambda: main('3.txt'))
race_3_button.place(relx=0.4, rely=0, relheight=0.33, relwidth=0.2)

race_4_button = Button(frame, text='Analyse Race 4', font=40, command=lambda: main('4.txt'))
race_4_button.place(relx=0.6, rely=0, relheight=0.33, relwidth=0.2)

race_5_button = Button(frame, text='Analyse Race 5', font=40, command=lambda: main('5.txt'))
race_5_button.place(relx=0.8, rely=0, relheight=0.33, relwidth=0.2)

race_6_button = Button(frame, text='Analyse Race 6', font=40, command=lambda: main('6.txt'))
race_6_button.place(relx=0, rely=0.33, relheight=0.33, relwidth=0.2)

race_7_button = Button(frame, text='Analyse Race 7', font=40, command=lambda: main('7.txt'))
race_7_button.place(relx=0.2, rely=0.33, relheight=0.33, relwidth=0.2)

race_8_button = Button(frame, text='Analyse Race 8', font=40, command=lambda: main('8.txt'))
race_8_button.place(relx=0.4, rely=0.33, relheight=0.33, relwidth=0.2)

race_9_button = Button(frame, text='Analyse Race 9', font=40, command=lambda: main('9.txt'))
race_9_button.place(relx=0.6, rely=0.33, relheight=0.33, relwidth=0.2)

race_10_button = Button(frame, text='Analyse Race 10', font=40, command=lambda: main('10.txt'))
race_10_button.place(relx=0.8, rely=0.33, relheight=0.33, relwidth=0.2)

race_11_button = Button(frame, text='Analyse Race 11', font=40, command=lambda: main('11.txt'))
race_11_button.place(relx=0, rely=0.67, relheight=0.33, relwidth=0.2)

race_12_button = Button(frame, text='Analyse Race 12', font=40, command=lambda: main('12.txt'))
race_12_button.place(relx=0.2, rely=0.67, relheight=0.33, relwidth=0.2)

race_13_button = Button(frame, text='Analyse Race 13', font=40, command=lambda: main('13.txt'))
race_13_button.place(relx=0.4, rely=0.67, relheight=0.33, relwidth=0.2)

race_14_button = Button(frame, text='Analyse Race 14', font=40, command=lambda: main('14.txt'))
race_14_button.place(relx=0.6, rely=0.67, relheight=0.33, relwidth=0.2)

race_15_button = Button(frame, text='Analyse Race 15', font=40, command=lambda: main('15.txt'))
race_15_button.place(relx=0.8, rely=0.67, relheight=0.33, relwidth=0.2)

bg_colour = 'white'
results = Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=("Courier", 10), bg=bg_colour)
results.place(relwidth=1, relheight=1)

root.mainloop()
