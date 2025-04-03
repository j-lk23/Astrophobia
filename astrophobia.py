import math
import time
import sys
import random

# Title menu
print("""
                                                                                                                                                                               
       █████        ██████████████ ██████████████ ██████████████     ████████████    ██████████████   ████       ███    ████████████    ██████████████   ████       ██████      
     ████████      ████                 ████      ████       █████ █████       ████  ███        ████  ████       ███  █████       ████  ████       ████  ████      ████████     
    ████   ████     █████████████       ████      ████       ████  ████         ███  ███        ████  ██████████████  ████         ████ ██████████████   ████    ████   ████    
   █████████████              ████      ████      █████████████    █████       ████  ███ █████████    ████       ███  █████       ████  ████        ███  ████   ██████████████  
 █████        ████ ██████████████       ████      ████      ██████   ████████████    ███              ████       ███    █████████████   ██████████████   ████ ████         ████ 
                                                                                                                                                                               """)
print("Welcome to Astrophobia.\n")

while True:
    title_action = input("Would you like to start a new game (new), continue a previous game (continue), or quit (quit)?\n").strip().lower()
    print()  # Line break after user input for better readability

    if title_action == "new":
        print("Forming a new galaxy...\n")
        time.sleep(3)
        break
    elif title_action == "continue":
        print("Launching back into dead space...\n")
        time.sleep(3)
        break
    elif title_action == "quit":
        print("Quitting...\n")
        sys.exit()
    else:
        print("Please choose a valid option. (new) (continue) (quit)\n")
# New game
print("space_epilogue_part1\n")
time.sleep(10)
print("space_epilogue_part2\n")
time.sleep(10)
print("space_epilogue_part3\n")
time.sleep(10)

# playerrace = input("Race?\n\n")

# playerage = input("Age?\n\n")

# playername = input("Alias?\n\n")

# Continue

