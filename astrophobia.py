import math
import time
import sys
import random

# Visual adjustments for command-line

# Save the original print and input functions
ns_print = print  # The original print (non-scrolling) function
ns_input = input  # The original input function

# Scrolling text implementation for print
def scrolling_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    ns_print()  # Adds a line break after the scrolling text
    ns_print()  # Adds another line break for spacing

# Scrolling text implementation for input
def scrolling_input(prompt, delay=0.05):
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    result = ns_input()  # Capture user input normally (non-scrolling input)
    ns_print()  # My *attempt* to use the non-scrolling print (ns_print) for a line break after input()
    return result

# Override print and input
print = scrolling_print  # Redefine print to use scrolling text
input = scrolling_input  # Redefine input to handle scrolling input

# This is where the fun begins...

# Title menu
ns_print("""
       █████        ██████████████ ██████████████ ██████████████     ████████████    ██████████████   ████       ███    ████████████    ██████████████   ████       ██████      
     ████████      ████                 ████      ████       █████ █████       ████  ███        ████  ████       ███  █████       ████  ████       ████  ████      ████████     
    ████   ████     █████████████       ████      ████       ████  ████         ███  ███        ████  ██████████████  ████         ████ ██████████████   ████    ████   ████    
   █████████████              ████      ████      █████████████    █████       ████  ███ █████████    ████       ███  █████       ████  ████        ███  ████   ██████████████  
 █████        ████ ██████████████       ████      ████      ██████   ████████████    ███              ████       ███    █████████████   ██████████████   ████ ████         ████ 
""")
print("Welcome to Astrophobia.")

while True:
    title_action = input("Would you like to start a new game (new), continue a previous game (continue), or quit (quit)?").strip().lower()

    if title_action == "new":
        print("Forming a new galaxy...")
        time.sleep(3)
        break
    elif title_action == "continue":
        print("Launching back into dead space...")
        time.sleep(3)
        break
    elif title_action == "quit":
        print("Quitting...")
        sys.exit()
    else:
        print("Please choose a valid option. (new) (continue) (quit)")

# New game
if title_action == "new":
    print("space_epilogue_part1")
    time.sleep(10)
    print("space_epilogue_part2")
    time.sleep(10)
    print("space_epilogue_part3")
    time.sleep(10)
    print("And that's where it ends! (for now...)")

# playerrace = input("Race?\n\n")

# playerage = input("Age?\n\n")

# playername = input("Alias?\n\n")

# Continue
if title_action == "continue":
    print("Soooooooooooo... this doesn't actually exist yet. *boowomp-womp-womp-wowowowowomp*")
