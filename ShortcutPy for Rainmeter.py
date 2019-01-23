#####startup
import os, sys, winsound
import tkinter as tk
from tkinter import filedialog

image_path = ""
shortcut_path = ""
name = ""
feedback = ""
current_location = str(os.getcwd()) + "\\"

def ask_file(init_dir = "root pro"):
    global image_path
    global current_location
    if init_dir == "root pro":
        init_dir = current_location
    a = filedialog.askopenfilename(initialdir = init_dir,title = "Select file")
    image_path = a

def ask_fileb(init_dir = "root pro"):
    global shortcut_path
    global current_location
    if init_dir == "root pro":
        init_dir = current_location
    a = filedialog.askopenfilename(initialdir = init_dir,title = "Select file")
    shortcut_path = a

def newdirectory(newdoss):
    if not os.path.exists(newdoss):
        os.makedirs(newdoss)

def new_shortcut():
    global feedback
    global name
    global image_path
    global shortcut_path
    feedback = "Started"
    global current_location

    image_name_file = os.path.basename(image_path)


    # asking variables
    name_of_shortcut = name
    name_of_shortcut_file = name_of_shortcut
    if os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
        print("Warning: The shortcut already exist !")
        i = 0
        while os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
            i = i + 1
            name_of_shortcut_file = name_of_shortcut_file + " alt " + str(i)

    #create file
    newdirectory(current_location + "ini files\\" + name_of_shortcut + "\\")
    with open(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".txt", mode = "w") as fichier:
        fichier.write("[" + name_of_shortcut_file + "]" + "\n")
        fichier.write("Meter=Image" + "\n")#############################################
        fichier.write("ImageName=" + image_name_file + "\n")
        fichier.write("H=90" + "\n")####################################################
        fichier.write('LeftMouseUpAction=["' + shortcut_path +'"]' + "\n")
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

    feedback = "file created"

#####
fenetre_principale = tk.Tk()

####
Widget_label_name = tk.Label(fenetre_principale, text="Name of the shortcut: ")
Widget_label_name.grid(row=0, column=0)

Widget_label_image = tk.Label(fenetre_principale, text="Path to the image: ")
Widget_label_image.grid(row=1, column=0)

Widget_label_shorcut = tk.Label(fenetre_principale, text="Path to the shortcut: ")
Widget_label_shorcut.grid(row=2, column=0)

Widget_label_feedback = tk.Label(fenetre_principale, text="")
Widget_label_feedback.grid(row=4, column=0, columnspan=5)
#Widget_label_percent

###

Widget_entry_name = tk.Entry(fenetre_principale)
Widget_entry_name.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
Widget_entry_image = tk.Label(fenetre_principale, text= "")
Widget_entry_image.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
Widget_entry_shorcut = tk.Label(fenetre_principale, text= "")
Widget_entry_shorcut.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

###

Widget_button_image = tk.Button(fenetre_principale, text = "...", command = ask_file)
Widget_button_image.grid(row=1, column=5, padx=5, pady=5)
Widget_button_shortcut = tk.Button(fenetre_principale, text = "...", command = ask_fileb)
Widget_button_shortcut.grid(row=2, column=5, padx=5, pady=5)
Widget_button_start = tk.Button(fenetre_principale, text = "Create Shortcut", command = new_shortcut)
Widget_button_start.grid(row=3, column=2, padx=5, pady=5)

while True:
    #mainloop
    name = Widget_entry_name.get()
    Widget_entry_image.configure(text = str(image_path))
    Widget_entry_shorcut.configure(text = str(shortcut_path))
    Widget_label_feedback.configure(text = str(feedback))
    fenetre_principale.update_idletasks()
    fenetre_principale.update()




#####functions

# function that create the new shortcurt
