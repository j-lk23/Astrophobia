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
    print("\"Certain collision, capable of causing global climatic catastrophe that may threaten the future of civilization as we know it.\"")
    time.sleep(1)
    print("In the early years of the 21st century, mankind learned that even something as pure as the heavens could harbor certain doom. In December of 2004, Asteroid 99942 Apophis was discovered – an aimlessly wandering leviathan of stone, destined to cross our path. With each new calculation, the outcome grew more dire – an impact which once seemed improbable began to take the shape of inevitability. World-renowned strategists and brilliant mathematicians did nothing but watch in grim silence as the numbers converged into a single, and inevitable outcome: global climatic catastrophe.")
    time.sleep(3)
    print("For nearly 25 relentless years, the brightest minds on the planet raced against time, producing life-changing technological advancements at an unprecedented pace. As the threat of global annihilation grew, hope became as scarce as a clear sky in the fallout of despair. The forecast of devastation was clear – the collision would not only shatter the world we once knew, but guide us to abandon our crumbling cradle of a planet. When all options to save Earth had been exhausted, humanity's salvation became a desperate diaspora into the stars.")
    time.sleep(3)
    print("Engineers worked around the clock. Not in a futile bid to save a doomed planet, but to forge humanity’s final exit ticket. The brightest minds all over the world intertwined, culminating into a radical plan. By 2029, a select five-hundred souls – the minimum viable population – were to be launched into the cosmos, carrying with them the last ember of our civilization, destined to seed the stars with the future of mankind.")
    time.sleep(3)
    print("Thus,")
    time.sleep(1)
    print("in the shadow of the impending apocalypse,")
    time.sleep(1)
    print("the greatest exodus in human history was born.")
    time.sleep(1)
    print("That's all, folks. (for now...)")

# Continue
if title_action == "continue":
    print("Soooooooooooo... this doesn't actually exist yet. *boowomp-womp-womp-wowowowowomp*")
