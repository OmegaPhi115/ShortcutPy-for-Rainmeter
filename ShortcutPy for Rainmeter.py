#startup
import os, sys, winsound
import tkinter as tk
from tkinter import filedialog

def path_exist(path):
    if os.path.exists(path):
        return "ok"
    else:
        return "nope"

def newdirectory(newdoss):
    if not os.path.exists(newdoss):
        os.makedirs(newdoss)

def ask_file(init_dir = "//"):
    a = filedialog.askopenfilename(initialdir = init_dir,title = "Select file")
    return a

ask_file()

# function that create the new shortcurt
def new_shortcut():
    fen = tk.Tk()
    current_location = str(os.getcwd()) + "\\"

    # asking variables
    name_of_shortcut = input("Name of the Shortcut")
    name_of_shortcut_file = name_of_shortcut
    if os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
        file_conflit = int(input("Warning: The shortcut already exist, Do you want to replace it (1) or create a variant ? (2)"))
        if file_conflit == "1":
            file_conflit = "replace"
        elif file_conflit == "2":
            i = 0
            while os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
                i = i + 1
                name_of_shortcut_file = name_of_shortcut_file + " alt " + str(i)


    image_name = input("Image Name ?")##    debug patacorn by justpatacorn.jpg
    image_name_file = "#@#Images\\" + image_name
    if not os.path.exists("@Resources\\Images\\" + image_name):
        return "The name of the image is incorect. Please try again"

    path_to_executable = input("Path to the executable")##        C:\\Users\\François\\Documents\\speak 2 me.vbs
    if not os.path.exists(path_to_executable):
        return "The path to the executable is incorect. Please try again"

    #create file
    newdirectory(current_location + "ini files\\" + name_of_shortcut + "\\")
    with open(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".txt", mode = "w") as fichier:
        fichier.write("[" + name_of_shortcut_file + "]" + "\n")
        fichier.write("Meter=Image" + "\n")#############################################
        fichier.write("ImageName=" + image_name_file + "\n")
        fichier.write("H=90" + "\n")####################################################
        fichier.write('LeftMouseUpAction=["' + path_to_executable +'"]' + "\n")
        fichier.write("" + "\n")########################################################
        fichier.write("[Rainmeter]" + "\n")#############################################
        fichier.write("Update=1000" + "\n")#############################################
        fichier.write("" + "\n")########################################################
        fichier.write("[Metadata]" + "\n")##############################################
        fichier.write("Name=" + name_of_shortcut_file + "\n")
        fichier.write("Author=" + "\n")#################################################
        fichier.write("Information=" + "\n")############################################
        fichier.write("License=" + "\n")################################################
        fichier.write("Version=" + "\n")################################################

    thisFile = current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".txt"
    base = os.path.splitext(thisFile)[0]
    os.rename(thisFile, base + ".ini")

    print("file created")
    return "success"
#mainloop
while 1:
    a = input("Create a new shortcut ? Y/N")
    if a == "Y" or a == "y":
        b = new_shortcut()
        if b != "success":
            print("Error: " + b)
    else:
        break