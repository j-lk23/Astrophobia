import math
import time
import sys
import random

# Preserve original print and input functions
ns_print = print
ns_input = input

def slow_print(text, delay=0.05):
    ns_print()  # Blank line before output
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    ns_print()

def slow_input(prompt, delay=0.05):
    slow_print(prompt, delay)
    return ns_input()

# Override built-in print and input
print = slow_print
input = slow_input

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

# Continue
if title_action == "continue":
    print("Soooooooooooo... this doesn't actually exist yet. *boowomp-womp-womp-wowowowowomp*")
