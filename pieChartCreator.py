import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import logging
from tkinter import *
Tk().withdraw()
from tkinter import messagebox

# Welcome message
messagebox.showinfo("Welcome", "Welcome to Piechart Creator!!!")

try:
   # Input file name from the user
    filename = input("Enter the file name (with .csv extension) to be fetched: ")
    logging.debug(filename)
    desktop_path = os.path.join(os.path.expanduser("~"), filename)
    logging.debug(desktop_path)

    # Attempt to open the file
    outfile = open(desktop_path, "r")
except IOError:
    # Error message if file is not found or is not in the correct format
    messagebox.showinfo("alert", "Enter a valid file in .csv extension or place file in the correct location!")
else:
    file = csv.reader(outfile)
    next(file, None)  # Skip the header
    row1 = []
    row2 = []

    for row in file:
        row1.append(row[0])
        try:
            row2.append(float(row[1]))  # Convert data to float for pie chart
        except ValueError:
            messagebox.showinfo("alert", "Data in the second column must be numerical!")
            outfile.close()
            exit()

    plt.pie(row2, labels=row1)
    plt.axis('equal')
    reply = messagebox.askquestion("question", "Do you want the piechart to be created?")

    if reply == "yes":
        try:
            plt.show(block=False)
        except:
            plt.close()
finally:
    # Thank you message
    messagebox.showinfo("thank you", "Thank you for using Piechart Creator!")
