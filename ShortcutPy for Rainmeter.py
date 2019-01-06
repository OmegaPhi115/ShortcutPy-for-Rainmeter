#startup
import os, sys, winsound

def path_exist(path):
    if os.path.exists(path):
        pass
    else:
        raise OSError
# function that create the new shortcurt
def new_shortcut():
    name_of_shortcut = input("Name of the Shortcut")
    image_name = "#@#Images\\" + input("Image Name ?")
    path_to_executable = input("Path to the executable")




#mainloop
while 1:
    print("Create a new shortcut ? Y/N")
    a = input("")
    if a == "Y" or a == "y":
        new_shortcut()
    else:
        break