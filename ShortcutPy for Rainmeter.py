#####startup
import os, sys, winsound
import tkinter as tk
from tkinter import filedialog

image_path = ""
shortcut_path = ""
name = ""
feedback = ""

def ask_file(init_dir = "//"):
    global image_path
    a = filedialog.askopenfilename(initialdir = init_dir,title = "Select file")
    image_path = a

def ask_fileb(init_dir = "//"):
    global shortcut_path
    a = filedialog.askopenfilename(initialdir = init_dir,title = "Select file")
    shortcut_path = a

def newdirectory(newdoss):
    if not os.path.exists(newdoss):
        os.makedirs(newdoss)

def start():
    global feedback
    print("I have started")
    feedback = "Started"

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
Widget_button_start = tk.Button(fenetre_principale, text = "Create Shortcut", command = start)
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
# def new_shortcut():
#     current_location = str(os.getcwd()) + "\\"

#     # asking variables
#     name_of_shortcut = input("Name of the Shortcut")
#     name_of_shortcut_file = name_of_shortcut
#     if os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
#         file_conflit = int(input("Warning: The shortcut already exist, Do you want to replace it (1) or create a variant ? (2)"))
#         if file_conflit == "1":
#             file_conflit = "replace"
#         elif file_conflit == "2":
#             i = 0
#             while os.path.exists(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".ini"):
#                 i = i + 1
#                 name_of_shortcut_file = name_of_shortcut_file + " alt " + str(i)


#     image_name = input("Image Name ?")##    debug patacorn by justpatacorn.jpg
#     image_name_file = "#@#Images\\" + image_name
#     if not os.path.exists("@Resources\\Images\\" + image_name):
#         return "The name of the image is incorect. Please try again"

#     path_to_executable = input("Path to the executable")##        C:\\Users\\François\\Documents\\speak 2 me.vbs
#     if not os.path.exists(path_to_executable):
#         return "The path to the executable is incorect. Please try again"

#     #create file
#     newdirectory(current_location + "ini files\\" + name_of_shortcut + "\\")
#     with open(current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".txt", mode = "w") as fichier:
#         fichier.write("[" + name_of_shortcut_file + "]" + "\n")
#         fichier.write("Meter=Image" + "\n")#############################################
#         fichier.write("ImageName=" + image_name_file + "\n")
#         fichier.write("H=90" + "\n")####################################################
#         fichier.write('LeftMouseUpAction=["' + path_to_executable +'"]' + "\n")
#         fichier.write("" + "\n")########################################################
#         fichier.write("[Rainmeter]" + "\n")#############################################
#         fichier.write("Update=1000" + "\n")#############################################
#         fichier.write("" + "\n")########################################################
#         fichier.write("[Metadata]" + "\n")##############################################
#         fichier.write("Name=" + name_of_shortcut_file + "\n")
#         fichier.write("Author=" + "\n")#################################################
#         fichier.write("Information=" + "\n")############################################
#         fichier.write("License=" + "\n")################################################
#         fichier.write("Version=" + "\n")################################################

#     thisFile = current_location + "ini files\\" + name_of_shortcut + "\\" + name_of_shortcut_file + ".txt"
#     base = os.path.splitext(thisFile)[0]
#     os.rename(thisFile, base + ".ini")

#     print("file created")
#     return "success"


#mainloop
#while 1:
#    a = input("Create a new shortcut ? Y/N")
#    if a == "Y" or a == "y":
#        b = new_shortcut()
#        if b != "success":
#            print("Error: " + b)
#    else:
#        break